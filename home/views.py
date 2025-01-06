from django.shortcuts import render
from home.models import Contact, Image
from django.contrib import messages

# from django.http import HttpResponse


def home(request):
    image= Image.objects.all().reverse()
    context={'image': image}
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def goal(request):
   return render(request, 'goal.html')

def vision(request):
   return render(request, 'vision.html')

def contact(request):
     
     if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone)<10 or len(content)<4:
            messages.error(request, "<p style='background-color:#daa6a6; color:black;text-align:center;padding:8px;border-radius:22px;width:80%;margin:auto;font-size:21px'><b>FAIL! : </b>message has not been sent, please try again with valid detail</p>",extra_tags='safe')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request,"<p style='background-color:#83f687; color:black;text-align:center;padding:8px;border-radius:22px;width:80%;margin:auto;font-size:21px'><b>SUCCESS! : </b>Your message has been successfully send to the developer</p>",extra_tags='safe')
     return render(request, 'contact.html')