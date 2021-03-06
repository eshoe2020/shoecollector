import uuid
import boto3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shoe, Replica, Photo

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'shoecollector-hsu' 


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def shoes_index(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/index.html', {'shoes': shoes}) 

def shoes_detail(request, shoe_id):
    shoe = Shoe.objects.get(id=shoe_id)
    replicas_shoe_doesnt_have = Replica.objects.exclude(id__in = shoe.replicas.all().values_list('id'))
    return render(request, 'shoes/detail.html', 
    {'shoe': shoe,
    'available_replicas':replicas_shoe_doesnt_have
    })


def add_photo(request, shoe_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, shoe_id=shoe_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('shoes_detail', shoe_id=shoe_id)

class ShoeCreate(CreateView):
    model = Shoe
    fields = '__all__'

class ShoeDelete(DeleteView):
    model = Shoe
    success_url = '/shoes/'

class ShoeUpdate(UpdateView):
    model = Shoe
    fields = ['name', 'designer', 'brand','style', 'size', 'color', 'description']


class ReplicaList(ListView):
  model = Replica

class ReplicaDetail(DetailView):
  model = Replica

class ReplicaCreate(CreateView):
  model = Replica
  fields = '__all__'

class ReplicaUpdate(UpdateView):
  model = Replica
  fields = '__all__'

class ReplicaDelete(DeleteView):
  model = Replica
  success_url = '/replicas/'



def assoc_replica(request, shoe_id, replica_id):
  Shoe.objects.get(id=shoe_id).replicas.add(replica_id)
  return redirect('shoes_detail', shoe_id=shoe_id)


def unassoc_replica(request, shoe_id, replica_id):
  Shoe.objects.get(id=shoe_id).replicas.remove(replica_id)
  return redirect('shoes_detail', shoe_id=shoes_id)