import json
from django.contrib.auth import authenticate,login

import requests
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from Logiapp.models import *
from Logiapp.credentials import LipanaMpesaPpassword, MpesaAccessToken
from django.shortcuts import render, redirect,get_object_or_404
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse






# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        contactme = Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        contactme.save()
        return redirect('/contact')

    else:
        return render(request, 'contact.html')



def pricing(request):
    return render(request,'pricing.html')

def servicedetails(request):
    return render(request,'service-details.html')

def services(request):
    return render(request,'services.html')

def starter(request):
    return render(request,'starter-page.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        # Check if the user exists
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, "You are now logged in!")
            return redirect('/home')
        else:
            messages.error(request, "Invalid login credentials")

    return render(request, 'login.html')


def register(request):
    """ Show the registration form """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check the password
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Display a message
                messages.success(request, "Account created successfully")
                return redirect('/login')
            except:
                # Display a message if the above fails
                messages.error(request, "Username already exist")
        else:
            # Display a message saying passwords don't match
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')




def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')


def stk(request):
    if request.method == "POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request_data = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request_data, headers=headers)

        # Parse response
        response_data = response.json()
        transaction_id = response_data.get("CheckoutRequestID", "N/A")
        result_code = response_data.get("ResponseCode", "1")  # 0 is success, 1 is failure

        # Save transaction to database
        transaction = Transaction(
            phone_number=phone,
            amount=amount,
            transaction_id=transaction_id,
            status="Success" if result_code == "0" else "Failed"
        )
        transaction.save()

        return HttpResponse(
            f"Transaction ID: {transaction_id}, Status: {'Success' if result_code == '0' else 'Failed'}")


def transactions_list(request):
    transactions = Transaction.objects.all().order_by('-date')
    return render(request, 'transactions.html', {'transactions': transactions})



def book(request):
    if request.method == "POST":

        image = request.FILES.get('image')

        if image:  # Log file upload
            print(f"Uploaded File Name: {image.name}")
            print(f"File Size: {image.size} bytes")

            # Optional: Save to disk manually (debugging)
            path = default_storage.save(f"bookings/{image.name}", ContentFile(image.read()))
            print(f"File saved at: {path}")

        serviceme = ServiceRequest1(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            service=request.POST['service'],
            request_date=request.POST['request_date'],
            image = image  # Assign image

        )
        serviceme.save()
        return redirect('/bookings')

    else:
        return render(request, 'booksevice.html')


def bookings(request):
    all = ServiceRequest1.objects.all()
    return render(request,'bookings.html',{'all':all})


def delete(request,id):
    deleteservice = ServiceRequest1.objects.get(id=id)
    deleteservice.delete()
    return redirect('/bookings')


def edit(request,id):
    booking = get_object_or_404(ServiceRequest1,id=id)
    if request.method == "POST":
        booking.full_name = request.POST.get('full_name')
        booking.email = request.POST.get('email')
        booking.phone_number = request.POST.get('phone_number')
        booking.request_date = request.POST.get('request_date')
        booking.service= request.POST.get('service')
        # Handle image update
        if 'image' in request.FILES:
            if booking.image:  # Delete old image
                booking.image.delete()
            booking.image = request.FILES['image']

        booking.save()
        return redirect('/bookings')
    else:
        return render(request,'edit.html',{'booking':booking})


def admin_dashboard(request):
    all1 = ServiceRequest1.objects.all()
    return render(request,'admindashboard.html',{'all1':all1})


def admin_login(request):
    # Admin credentials
    admin_username = "eddy"
    admin_email = "mwanziaedwin5@gmail.com"
    admin_password = "eddamax141#"

    # Ensure admin user exists
    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(username=admin_username, email=admin_email, password=admin_password)
        print("Superuser created successfully!")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.username == admin_username:
            login(request, user)
            messages.success(request, "Welcome Admin!")
            return redirect('/admindashboard')  # Redirect to transactions page
        else:
            messages.error(request, "Invalid credentials! Only admin can log in.")
            return redirect('/adminlogin')  # Redirect back to login page

    return render(request, 'adminlogin.html')