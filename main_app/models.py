from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse

# fs = FileSystemStorage(location='/media/photos')

COLORS = (
    ('A', 'Animal'),
    ('B', 'Black'),
    ('Bl', 'Blue'),
    ('Cl', 'Clear'),
    ('G', 'Green'), 
    ('Go', 'Gold'),
    ('Gr', 'Grey'),
    ('Mu', 'Multi'),
    ('Ne', 'Neon'),
    ('O', 'Orange'),
    ('P', 'Purple'),
    ('Ra', 'Rainbow'),
    ('R', 'Red'),
    ('Si', 'Silver'),
    ('T', 'Teal'),
    ('Y', 'Yellow'),
)

SIZES = (
    ('4', '4'),
    ('4.5', '4.5'),
    ('5', '5'),
    ('5.5', '5.5'),
    ('6', '6'),
    ('6.5', '6.5'),
    ('7', '7'),
    ('7.5', '7.5'),
    ('8', '8'),
    ('8.5','8.5'),
    ('9', '9'),
    ('9.5','9.5'),
    ('10', '10'),
    ('10.5', '10.5'),
    ('11', '11')
)


STYLES = (
    ('An', 'Ankle-High/Booties'),
    ('Fl', 'Flats'),
    ('HH', 'High Heels'),
    ('Kn', 'Knee-High Boots'),
    ('Ru', 'Running Shoes'),
    ('Sa', 'Sandals'),
    ('Th', 'Thigh-High Boots'),
    ('We', 'Wedges/Platforms')
)

class Replica(models.Model):
    name = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('replicas_detail', kwargs={'pk': self.id}) 

class Shoe(models.Model):
    name = models.CharField(
        max_length=250, default='Please enter name of shoe'
    )
    designer = models.BooleanField(
        'Designer:',
        default=False, 
    )
    brand = models.CharField(
        max_length=250
    )
    style = models.CharField(
        max_length=2,
        choices=STYLES,
        default=STYLES[0][0]   
    )
    size = models.CharField(
        'Size:',
        max_length=4,
        choices=SIZES,
        default=SIZES[0][0]
    )
    color = models.CharField(
        'Color:',
        max_length=2,
        choices =COLORS,
        default=COLORS[0][0]
    )
    description = models.TextField(
        'Description:',
        max_length=1000
    )

    def __str__(self):
        return self.brand
        return self.name
    
    def get_absolute_url(self):
        return reverse('shoes_detail', kwargs={'shoe_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=200)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for shoe_id: {self.shoe_id} @ {self.url}"

    