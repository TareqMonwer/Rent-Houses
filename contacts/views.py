from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from btre.email_details import myemail


def contact(request):
    if request.method == 'POST':
        cd = request.POST
        listing = cd.get('listing')
        listing_id = cd.get('listing_id')
        user_id = cd.get('user_id')
        realtor_email = cd.get('realtor_email')
        name = cd.get('name')
        email = cd.get('email')
        phone = cd.get('phone')
        message = cd.get('message')

        # missing date from contact
        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            message=message,
            contact_id=user_id,
            realtor_email=realtor_email
        )
        if request.user.is_authenticated:
            current_user_id = request.user.id
            is_contacted = Contact.objects.all().filter(contact_id=current_user_id,
                                                        listing_id=listing_id)
            if is_contacted:
                messages.error(
                    request, 'You already made an inquery for this property.')
                return redirect('/listings/'+listing_id)
            else:
                contact.save()
                send_mail('You have set an inquery on btre',
                          'Please keep noticed, you have an inquery for ' +
                          listing + ' at ' + str(contact.contact_date),
                          myemail,
                          [email, realtor_email, 'tareqmonwer137@gmail.com'],
                          fail_silently=False)
                return redirect('dashboard')

