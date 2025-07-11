from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Photo, Tag
from .forms import PhotoForm

def home_view(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    tags = Tag.objects.all()
    return render(request, 'home.html', {'photos': photos, 'tags': tags})

def detail_view(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'detail.html', {'photo': photo})

@login_required
def upload_view(request):
    form = PhotoForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        photo = form.save(commit=False)
        photo.user = request.user
        photo.save()
        form.save_m2m()
        return redirect('gallery:home')
    return render(request, 'upload.html', {'form': form})

def filter_view(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    photos = Photo.objects.filter(tags=tag)
    return render(request, 'filter.html', {'photos': photos, 'tag': tag})