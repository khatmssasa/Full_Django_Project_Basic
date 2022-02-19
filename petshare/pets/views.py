from unicodedata import category
from django.shortcuts import render
from .models import PetCategorey , PetDetails




def index(request):
    category = PetCategorey.objects.all()
    pets = PetDetails.objects.all()
    return render(request , 'index.html', {'category':category,'pets':pets})


def one_category(request , str):
    category = PetCategorey.objects.get(category=str)
    pets_in_category = category.objects.all()
    return render(request , 'one_category.html', {'pets_in_category':pets_in_category})