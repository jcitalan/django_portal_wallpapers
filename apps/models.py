from configparser import Interpolation
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import cv2
import os

# Create your models here.
class Wallpaper(models.Model):
  title=models.CharField(max_length=100)
  description=models.CharField(max_length=100)
  price=models.DecimalField(max_digits=6, decimal_places=2)
  status=models.BooleanField(default='null')
  photo = models.ImageField(default='null',upload_to='imgs')
  created_at=models.DateTimeField(auto_now_add=True)
  update_at=models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name="Wallpaper"
    verbose_name_plural ="Wallpapers"
    ordering = ['id']
  def __str__(self):
    if self.status:
      activo=('Activo')
    else:
      activo=('Inactivo')

    return f'Wallpaper {self.title} | Estado:  {activo}'
  
  def name_photo(self):
    name_original=self.photo.name
    only_name_photo=name_original.replace('.','/').split('/')
    nuevo_nombre=('{}.{}'.format(only_name_photo[1],'webp'))
    return nuevo_nombre

  def save(self,*args,**kwargs):
    super().save(*args,**kwargs)

    name_original=self.photo.name
    path_original=self.photo.path

    new_format=name_original.split('/')

    only_name_photo=name_original.replace('.','/').split('/')

    path_image=path_original.split('/imgs')
    if not os.path.exists(os.path.join('code',path_image[0],'imgs','download')):
      os.makedirs(os.path.join('code',path_image[0],'imgs','download'))
    if not os.path.exists(os.path.join('code',path_image[0],'imgs','preview')):
      os.makedirs(os.path.join('code',path_image[0],'imgs','preview'))
      

    
    firt_path_size=os.path.join(path_image[0],'imgs','download',new_format[1])
    second_path_size=os.path.join(path_image[0],'imgs','preview',new_format[1])
 

    img = cv2.imread(self.photo.path)

    img_preview=cv2.resize(img,(136,76),interpolation=cv2.INTER_CUBIC)
    img_download=cv2.resize(img,(1366,768),interpolation=cv2.INTER_CUBIC)


    cv2.imwrite(firt_path_size,img_download)
    cv2.imwrite(second_path_size,img_preview)
    
    
    photo_small=('{}.{}'.format(only_name_photo[1],'webp'))
    last_path_psmall=os.path.join(path_image[0],'imgs','preview',photo_small)
    path_psmall=os.path.join(path_image[0],'imgs','preview',new_format[1])

    photo_large=('{}.{}'.format(only_name_photo[1],'webp'))
    last_path_plarge=os.path.join(path_image[0],'imgs','download',photo_large)
    path_plarge=os.path.join(path_image[0],'imgs','download',new_format[1])

    photo_one = Image.open(path_psmall)
    new_pone = photo_one.convert('RGB')
    new_pone.save(last_path_psmall, 'webp')

    photo_two = Image.open(path_plarge)
    new_ptwo = photo_two.convert('RGB')
    new_ptwo.save(last_path_plarge, 'webp')
