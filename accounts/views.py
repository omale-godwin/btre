from django.shortcuts import render, redirect
from  django.contrib import messages, auth
from django.contrib.auth.models import User
from cont.models import Contact


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check password matching
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username has already been taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email has already been taken')
                    return redirect('register')
                else:
                    #look good
                    user = User.objects.create_user(username=username, password=password,
                    first_name=first_name, last_name=last_name, email=email)
                    # auth.login(request, user)
                    # return redirect('index')
                    user.save()
                    messages.success(request, 'you have registered successfully')
                    return redirect('index')

        else:
            messages.error(request, 'Password do not match')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now login')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'you now logout succefully')
        return redirect('index')


def dashboard(request):
    user_contact = Contact.objects.order_by('-contact_date')

    context = {
        'contact': user_contact
    }
    return render(request, 'accounts/dashboard.html', context)