from django.shortcuts import render
from .forms import ImageForm
from .models import Image
# Create your views here.


def Home(request):
	
	return render(request,'home.html')

def Upload(request):
	if request.method == "POST":
		form = ImageForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
	form = ImageForm()
	img = Image.objects.all()
	return render(request, 'upload.html',{'img':img,'form': form})


def Contact(request):	
	return render(request,'contact.html')

def Gallery(request):	
	return render(request,'gallery.html')
def Bg(request):
	return render(request,'bg.html')
