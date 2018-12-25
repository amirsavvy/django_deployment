from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from goeymvcapp.models import Contact, Page,Service, CompanySkills, CompanyStats, Gallery,SocialNetwork, Testimonial, Certificate
from django.core.mail import send_mail
from .forms import UserForm, UserProfileInfoForm,SendEmailContactForm, CustomerRegisterForm
from django.utils import translation
# For Login Libraries
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Admin Auth Methods
# User Registeration Get Method
def get_registeration(request):
    user_form_data = UserForm()
    user_profile_form_data = UserProfileInfoForm()
    list = {'user_form': user_form_data, 'user_profile_form': user_profile_form_data}

    return render(request, 'frontend/get_register.html', list)


# User Registeration Post Method
def post_registeration(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, user_profile_form.errors)

    else:
        user_form = UserForm()
        user_profile_form = UserProfileInfoForm()
        forms_list = {'user_form': user_form, 'user_profile_form': user_profile_form, 'registered': registered}
        return render(request, 'frontend/get_register.html', forms_list)

    return render(request,'frontend/index.html')

# User LOGIN
def get_login(request):
    user_form_data = UserForm()
    user_profile_form_data = UserProfileInfoForm()
    list = {'user_form': user_form_data, 'user_profile_form': user_profile_form_data}

    return render(request, 'frontend/login.html', list)

def post_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('User is not active')

        else:
            print('Someone tried to login and failed')
            print('Username: {} and password {}', format(username, password))
            HttpResponse('Invalid login details suplied')

    else:
        user_form_data = UserForm()
        user_profile_form_data = UserProfileInfoForm()
        list = {'user_form': user_form_data, 'user_profile_form': user_profile_form_data}
        return render(request, 'frontend/login.html', list)

# User logout
# For accuracy use decorators
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Test for login_required Page
@login_required
def login_testing(request):
    return HttpResponse('You are are login to our system, thanks :)')



# FrontEnd Views Functions.
def index(request):
    # Contact Data from Contact Model
    data = Contact.objects.all()
    # Social Network
    social_data = SocialNetwork.objects.all()
    #Testimonial
    testimonial_data = Testimonial.objects.all()
    #Certificate
    certificate_data = Certificate.objects.all()
    #Gallery
    gallery_data = Gallery.objects.all()
    #CompanyStats
    company_stats_data = CompanyStats.objects.all()
    #CompanySkills
    company_skills_data = CompanySkills.objects.all()
    #Service
    service_data = Service.objects.all()
    #page home_about
    home_about = Page.objects.get(heading="Home About")
    #page Why Work With Us home
    why_work_with_us_home = Page.objects.get(heading="Why Work With Us Home")
    #page Home Banner Image Heading
    home_banner_image_heading = Page.objects.get(heading="Home Banner Image Heading")
    # Import form for view
    form_obj = SendEmailContactForm()


    lists = {"contact_db_data": data,
     "social_networks_db_data": social_data,
     "testimonial_db_data": testimonial_data,
     "certificate_db_data": certificate_data,
     "gallery_db_data": gallery_data,
     "company_stats_db_data": company_stats_data,
     "company_skills_db_data": company_skills_data,
     "service_db_data": service_data,
     "home_about_db_data": home_about,
     "why_work_with_us_home_db_data": why_work_with_us_home,
     "home_banner_image_heading_db_data":home_banner_image_heading,
     "form": form_obj
     }
    return render(request,'frontend/index.html',lists)

def send_email_contact_form(request):
    if request.method == 'POST':
       form = SendEmailContactForm(request.POST)
       if form.is_valid():
          print("Valid form test passed")
          first_name = form.cleaned_data['first_name']
          last_name = form.cleaned_data['last_name']
          phone = form.cleaned_data['phone']
          email = form.cleaned_data['email']
          text_message = form.cleaned_data['text_message']
          # Email Sending Code
          subject = 'New Inquiry from ' + first_name + " " + last_name
          message = "First Name" + first_name + ", Last Name" + last_name + ", Phone" + phone + ", Message" + text_message
          from_email = settings.EMAIL_HOST_USER
          to_list = [settings.EMAIL_HOST_USER]
          send_mail(subject, message, from_email, to_list, fail_silently=False)
          messages.success(request, 'We have received your query we will get back to you soon!!')
          # return redirect('/index/')
          return HttpResponse('Wow, Email sent')
       else:
           # form = SendEmailContactForm(request.POST)
          return HttpResponse('Email not sent')

# get customer registeration form
def cusotmer_registeration(request):
    form_obj = CustomerRegisterForm()
    form_list = {"form": form_obj}
    return render(request, 'frontend/register.html', form_list)

# post customer registeration form
def post_cusotmer_registeration(request):
    print("Customer post method")
    form = CustomerRegisterForm()

    if request.method == "POST":
        form = CustomerRegisterForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Registered')
        else:
            return HttpResponse('Not registered')

    return render(request, 'frontend/index.html')
