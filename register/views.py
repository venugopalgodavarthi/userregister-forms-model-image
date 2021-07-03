from django.shortcuts import render
from register.forms import USERFORM
from register.models import USERMODEL
from django.core.files.storage import FileSystemStorage
# Create your views here.
def register_request(request):
    if request.method=='POST':
        form=USERFORM(request.POST,request.FILES)
        if form.is_valid():
            upload_image=request.FILES.get("img")
            fs=FileSystemStorage()
            file=fs.save(upload_image.name,upload_image)
            firstname1 = form.cleaned_data['firstname']
            lastname1 = form.cleaned_data['lastname']
            email1= form.cleaned_data['email']
            phone1= form.cleaned_data['phone']
            dob1= form.cleaned_data['dob']
            address1= form.cleaned_data['address']
            gender1=form.cleaned_data['gender']
            var= USERMODEL.objects.create(firstname=firstname1,
                                          lastname=lastname1,
                                          email=email1,
                                          address=address1,
                                          phone=phone1,
                                          gender=gender1,
                                          dob=dob1,
                                          img=file)
            var.save()
    form= USERFORM
    return render(request,"register.html",{'form':form})

def read_request(request):
    var=USERMODEL.objects.all()
    return render(request,"display.html",{'data':var})
    