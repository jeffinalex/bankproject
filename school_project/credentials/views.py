
from django.shortcuts import render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('button')
        else:
            messages.info(request,'Invalid Crendentials')
            return redirect('login')
    return render(request,('login.html'))
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if not username or not password or not cpassword:
            messages.error(request, 'Please fill all the fields')
            return redirect('register')
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')

    return render(request,('register.html'))
def details(request):
    if request.method=='POST':
        name=request.POST['Name']
        dob = request.POST['DOB']
        # address = request.POST['Address']
        # phone = request.POST['Phone']
        # email = request.POST['Email']
        # dept = request.POST.get('Dept',False)
        # purpose = request.POST('Purpose',False)
        if not name or not dob :
            messages.error(request, 'Please fill all fields')
            return redirect('details')
        else:
            return redirect('details1')
    return render(request,'details.html')
def button(request):
    return render(request,'button.html')
def details1(request):
    message = "Order Confirmed"
    return render(request, 'submit.html', {'message': message})