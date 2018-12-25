from django.contrib import admin
from goeymvcapp .models import UserProfileInfo,Page, Customer,Service, CompanyStats, CompanySkills, Contact, Client, Team, Category,Project,SocialNetwork, Testimonial, Gallery, Banner, Certificate

# Register your models here.
# Admin models
admin.site.register(UserProfileInfo)

# Register all frontend models hereProject
admin.site.register(Page)
admin.site.register(Contact)
admin.site.register(Client)
admin.site.register(Team)
admin.site.register(SocialNetwork)
admin.site.register(Testimonial)
admin.site.register(Gallery)
admin.site.register(Banner)
admin.site.register(Certificate)
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(CompanyStats)
admin.site.register(CompanySkills)
admin.site.register(Service)
admin.site.register(Customer)
