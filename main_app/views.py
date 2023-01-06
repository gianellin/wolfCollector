from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wolf
from .forms import FeedingForm

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
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'wolfs/detail.html', { 'wolf': wolf, 'feeding_form': feeding_form })

def add_feeding(request, wolf_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.wolf_id = wolf_id
    new_feeding.save()
    return redirect('detail', wolf_id=wolf_id)

class WolfCreate(CreateView):
  model = Wolf
  fields = '__all__'
  success_url = '/wolfs/'

class WolfUpdate(UpdateView):
  model = Wolf
  # Let's disallow the renaming of a wolf by excluding the name field!
  fields = ['breed', 'description', 'age']

class WolfDelete(DeleteView):
  model = Wolf
  success_url = '/wolfs/'




