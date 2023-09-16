from django.db import models

# Create your models here.

#this is for all users and their information
class UserData(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30)
    user_password=models.CharField(max_length=20)
    user_gmail=models.EmailField( max_length = 30)
    user_address=models.CharField(max_length=50)
    user_phone= models.CharField(max_length=10)

    def __str__(self):
          return self.user_name

#this is for all the problems submitted by the users
class UserProblem(models.Model):
        UserProblem_title=models.CharField(max_length=30)
        UserProblem_photo=models.ImageField(upload_to="user/problemimage", default="")
        UserProblem_location=models.CharField(max_length=50)
        UserProblem_description=models.CharField(max_length=100)
        UserProblem_status= models.CharField(max_length=50, choices=(
              ('solved','solved'),
              ('pending','pending'),
              ('uderprogress','underprogress')
        ))

        user=models.ForeignKey(UserData, on_delete=models.CASCADE)