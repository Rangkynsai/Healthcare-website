from django.shortcuts import render
from django.core.mail import send_mail
from .models import Contact,Feedback,Postblog,Appointment,Medicine
from django.http import HttpResponseRedirect
def home_page(request):
    context = {
        'posts': Postblog.objects.all().order_by("-id")
    }
    return render(request,'index.html',context)

def book_appointment(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_no = request.POST['phone_no']
        email = request.POST['email']
        options = request.POST['options']
        date_1 = request.POST['date_1']
        time_1 = request.POST['time_1']
        info = Appointment(first_name=first_name,last_name=last_name,phone_no=phone_no,email=email,options=options,date_1=date_1,time_1=time_1)
        print('submited')
        info.save()
        #send mail
        messages = first_name+" "+last_name+" has booked an appointment on "+date_1+" at "+time_1+" with "+options+" Thankyou"
        send_mail(
            'Appointment',
            messages,
            email,
            ['vtu10669@veltechuniv.edu.in'],
            fail_silently=False,)
        
        return render(request,'appointment.html',{'first_name':first_name})
    else:
        return render(request,'appointment.html',{})

def About(request):
    return render(request,'about.html')

def medi(request):
    if request.method == 'POST':
        name = request.POST['name']
        mail = request.POST['mail']
        content = request.POST['content']
        store = Medicine(name=name,mail=mail,content=content)
        store.save()
        print('succesfully')
        return render(request,'medicine.html',{'name':name})
    else:
        return render(request,'medicine.html')

def Doct(request):
    if request.method == 'POST':
        name = request.POST['name']
        doc_store = {'headache':'Dr.A','stomach pain':'Dr.B','pain in join':'Dr.C'}
        if name in doc_store:
            finding = doc_store[name]
            print(finding)
            return render(request,'doctor.html',{'name':finding})
        return render(request,'doctor.html')
    else:
        return render(request,'doctor.html')

def AddContact(request):
    name = request.POST['name']
    email = request.POST['email']
    content = request.POST['content']
    detail = Contact(name=name,email=email,content=content)
    print('Submited')
    detail.save()
    return HttpResponseRedirect('/')

def AddFeedback(request):
    name = request.POST['name']
    email = request.POST['email']
    content = request.POST['content']
    feed = Feedback(name=name,email=email,content=content)
    print("submited")
    feed.save()
    return HttpResponseRedirect('/')

def blogpost(request,task_id):
    context = Postblog.objects.get(id=task_id)
    con = {
        'context':context
    }
    return render(request,'blogpost.html',con)

def Acknowledge(request):
    return render(request,'acknowledge.html')
