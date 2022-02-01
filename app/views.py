from django.shortcuts import render,redirect
from .models import Talaba
from django.core.files.storage import FileSystemStorage
# Create your views here.
def main(request):
    if request.method=="POST" and request.FILES['rasm']:
        image=request.FILES['rasm']
        fss = FileSystemStorage()
        file = fss.save(image.name, image)
        ism=request.POST['ism']
        familiya=request.POST['familiya']
        yosh=request.POST['yosh']
        kasb=request.POST['kasb']
      
        new=Talaba.objects.filter(id=1).update(image=image,ism=ism,familiya=familiya,yosh=yosh,kasb=kasb)
        
        
        return redirect('/')
    talaba=Talaba.objects.all()
    return render(request,'index.html',{"talabas":talaba})
