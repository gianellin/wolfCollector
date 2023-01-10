from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Wolf, Toy, Photo
import uuid
import boto3
from .forms import FeedingForm
# Add these "constant" variables below the imports
S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'wolfcollector'


# Create your views here.

def wolfs_detail(request, wolf_id):
  wolf = Wolf.objects.get(id=wolf_id)
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  toy_wolf_doesnt_have = Toy.objects.exclude(id__in = wolf.toys.all().values_list('id'))
  return render(request, 'wolfs/detail.html', { 'wolf': wolf, 'feeding_form': feeding_form, 'toys': toy_wolf_doesnt_have })

def add_feeding(request, wolf_id):
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the wolf_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.wolf_id = wolf_id
    new_feeding.save()
    return redirect('detail', wolf_id=wolf_id)

class WolfCreate(CreateView):
  model = Wolf
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/wolfs/'

class WolfUpdate(UpdateView):
  model = Wolf
  # Let's disallow the renaming of a wolf by excluding the name field!
  fields = ['breed', 'description', 'age']

class WolfDelete(DeleteView):
  model = Wolf
  success_url = '/wolfs/'

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def wolfs_index(request):
  wolfs = Wolf.objects.all()
  return render(request, 'wolfs/index.html', { 'wolfs': wolfs })

class ToyList(ListView):
	model = Toy

class ToyDetail(DetailView):
	model = Toy

class ToyCreate(CreateView):
	model = Toy
	fields = '__all__'

class ToyUpdate(UpdateView):
	model = Toy
	fields = ['name', 'color']

class ToyDelete(DeleteView):
	model = Toy
	success_url = '/toys/'
  
def assoc_toy(request, wolf_id, toy_id):
	Wolf.objects.get(id=wolf_id).toys.add(toy_id)
	return redirect('detail', wolf_id=wolf_id)

def remove_toy(request, wolf_id, toy_id):
	Wolf.objects.get(id=wolf_id).toys.remove(toy_id)
	return redirect('detail', wolf_id=wolf_id)

def add_photo(request, wolf_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = 'wolfcollector/' + uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to wolf_id or wolf (if you have a wolf object)
            Photo.objects.create(url=url, wolf_id=wolf_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', wolf_id=wolf_id)



