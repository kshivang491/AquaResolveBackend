from django.http import HttpResponse,JsonResponse


def index(request):
    return HttpResponse("ok so this is the backend server for our app. i have created three api keys that are <br><br>  1.http://127.0.0.1:8000/api/users/ <br> if you are on local host then it will work or otherwise just add /api/users/ in your website url and then you will be able to see all the users , you can add (signup) users <br><br>  2.http://127.0.0.1:8000/api/userproblems/ <br> use it if you are on localhost or add /api/userproblems/ in url and you will be able to see all the problems and add problems <br> <br>  3.http://127.0.0.1:8000/api/users/1/problems/<br>  this url can be used to show all problems submitted by oa specific user, you just have to type user id in place if 1 in url and it will show all his/her submitted problems<br> <br> now if you wanna see the admin pannel just go to http://127.0.0.1:8000/admin/ or add /admin/ in your url and the username is shivang and password is shivang@2023 or you can create your own superuser")