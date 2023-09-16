from django.contrib import admin
from UserData.models import UserData,UserProblem

# Register your models here.


#this is to show all users and their information in database
class userdetailsAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','user_password','user_gmail','user_address','user_phone')

admin.site.register(UserData,userdetailsAdmin)



#this is to show all the problems submitted by the users in database
class userproblemdetailsAdmin(admin.ModelAdmin):
    list_display=('user','UserProblem_title','UserProblem_photo','UserProblem_location','UserProblem_description','UserProblem_status')

admin.site.register(UserProblem,userproblemdetailsAdmin)