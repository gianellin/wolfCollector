from django.shortcuts import render
# Add the following import
from django.http import HttpResponse
from .models import Wolf

# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wolfs_index(request):
  wolfs = Wolf.objects.all()
  return render(request, 'wolfs/index.html', { 'wolfs': wolfs })

def wolfs_detail(request, wolf_id):
  wolf = Wolf.objects.get(id=wolf_id)
  return render(request, 'wolfs/detail.html', { 'wolf': wolf })