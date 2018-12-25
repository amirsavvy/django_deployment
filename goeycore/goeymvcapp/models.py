from django.db import models
from django.contrib.auth.models import User

# Admin models
class UserProfileInfo(models.Model):
    # one to one field
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # additions fields
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username


# FrontEnd Models.
class Page(models.Model):
    heading = models.CharField(max_length=256, unique=True)
    title = models.CharField(max_length=256, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    details = models.TextField(null=True, blank=True)
    meta_title = models.CharField(max_length=256, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.heading


class Contact(models.Model):
    contact_name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=500)
    email = models.EmailField(max_length=120, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.contact_name

class Client(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Team(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=150)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    email = models.EmailField(max_length=120, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=100)
    facebook_url= models.URLField(max_length=256, null=True, blank=True,unique=True)
    twitter_url= models.URLField(max_length=256, null=True, blank=True,unique=True)
    linkedin_url= models.URLField(max_length=256, null=True, blank=True,unique=True)
    github_url= models.URLField(max_length=256,null=True, blank=True,unique=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.full_name

class SocialNetwork(models.Model):
    name = models.CharField(max_length=100, unique=True)
    link_url= models.URLField(max_length=256, null=True, blank=True,unique=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.CharField(max_length=256, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    details = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.client_name

class Gallery(models.Model):
    title = models.CharField(max_length=256, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    details = models.TextField(null=True, blank=True)
    # Encapsulation for choices
    # GRAPHICS = 'gr'
    # WEBSITE = 'web'
    # APP = 'ap'
    # MARKETING = 'mar'
    # TYPE_CHOICES = (
    #     (GRAPHICS, 'graphics'),
    #     (WEBSITE, 'website'),
    #     (APP, 'app'),
    #     (MARKETING, 'marketing'),
    # )
    # gallery_type = models.CharField(max_length=5, choices=TYPE_CHOICES, default= WEBSITE)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Banner(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to='uploads/')
    details = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CompanyStats(models.Model):
    number_stat = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    font_awesome_class = models.CharField(max_length=150, null=True, blank=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CompanySkills(models.Model):
    number_stat = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=150)
    details = models.TextField()
    font_awesome_class = models.CharField(max_length=150, null=True, blank=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=8)
    vpassword = models.CharField(max_length=8)
    # status = models.BooleanField(default=True)
    # create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
