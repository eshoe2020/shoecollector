from django.contrib import admin

from .models import Shoe
from .models import Photo

admin.site.register(Shoe)
admin.site.register(Photo)