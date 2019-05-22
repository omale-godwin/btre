from django.shortcuts import render, redirect
from  django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id= user_id)
            if has_contacted:
                messages.error(request, 'you have already make and enquiry')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)
        contact.save()
        #send mail

        send_mail(
            'property listing enquiry',
            'there has been an aquiry for ' + listing + '. sign into the admin panel for more info',
            'godwinpeace3@gmail.com',
            [realtor_email, 'techguyinfo@gmail.com'],
            fail_silently=True
        )

        messages.success(request, 'you request has been submited , a reator will get back to you soon')
        return redirect('/listings/'+listing_id)