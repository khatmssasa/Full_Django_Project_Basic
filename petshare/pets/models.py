from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class PetCategorey(models.Model):
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category
    
    
    
    


gender_choice = [('Male','Male'),('Female','Female')]

def imgupload(instance,filename):
    imagename,extension = filename.split(".")
    return "pets/%s.%s"%(instance.id,extension)

class PetDetails(models.Model):
    category = models.ForeignKey(PetCategorey , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.FloatField(max_length=4)
    gender = models.CharField(max_length=20 ,choices=gender_choice)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to=imgupload)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_py = models.ForeignKey(User , on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True , unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self , *args , **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "_" + str(self.created_py))
        super(PetDetails , self).save(*args , **kwargs)