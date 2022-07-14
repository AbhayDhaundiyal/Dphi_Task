from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views import generic
from django.shortcuts import render , get_object_or_404
from .models import student, Educator, course
from django.urls import reverse
import simplejson as json

def std_signup(request):
    new_user = json.loads(request.body)
    std = student(Name = new_user['name'], Password = new_user["password"])
    std.save()
    return HttpResponse("200")


def login_std(request):
    data = json.loads(request.body)
    std = student.objects.filter(Name = data['name'], Password = data['password'])
    if std.count() == 0:
        response = HttpResponse("Wrong Credentials")
        response.delete_cookie("Is_student")
        return response
    response = HttpResponse('Logged In')
    response.set_cookie("Is_student", 'True')
    response.set_cookie("id", std[0].Id)
    return response


def edu_signup(request):
    new_user = json.loads(request.body)
    edu = Educator(Name = new_user['name'], Password = new_user["password"])
    edu.save()
    return HttpResponse("200")


def login_edu(request):
    data = json.loads(request.body)
    edu = Educator.objects.filter(Name = data['name'], Password = data['password'])
    if edu.count() == 0:
        response = HttpResponse("Wrong Credentials")
        response.delete_cookie("Is_student")
        response.delete_cookie("id")
        return response
    response = HttpResponse('Logged In')
    response.set_cookie("Is_student", 'False')
    response.set_cookie("id", edu[0].Id)
    return response


def add_course(request):
    try:
        val = request.COOKIES["Is_student"]
    except:
        return HttpResponse("Try Logging In First")
    if val == "False":
        data = json.loads(request.body)
        edu = Educator.objects.get(pk = request.COOKIES["id"])
        new_course = course(Name = data['name'], Desc = data["desc"], content = data['content'], creator = edu)
        new_course.save()
        return HttpResponse("200")
    else:
        return HttpResponse("This page is for Educators only")


def list_course(request):
    try:
        val = request.COOKIES["Is_student"]
    except:
        return HttpResponse("Try Logging In First")
    if val == "True":
        courses = course.objects.all()
        list = []
        for Course in courses:
            list.append(Course.Name)
        data = json.dumps({"Name" : list})
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("This Page is for student only")


def list_course_detail(request, id):
    try:
        val = request.COOKIES["Is_student"]
    except:
        return HttpResponse("Try Logging In First")
    if val == "True":
        courses = course.objects.get(pk = id)
        print(courses.Name)
        list = {}
        list['Name'] = courses.Name
        list['Desc'] = courses.Desc
        list['By'] = (courses.creator).Name

        data = json.dumps(list)
        return HttpResponse(data, content_type="application/json")
    else:
        return HttpResponse("This Page is for student only")


def enroll(request, id):
    try:
        val = request.COOKIES["Is_student"]
    except:
        return HttpResponse("Try Logging In First")
    if val == "True":
        std_id = request.COOKIES['id']
        std = student.objects.get(pk = std_id)
        courses = course.objects.get(pk = id)
        try:
            x = courses.enrolled.filter(std)
            return HttpResponse("Already Enrolled")
        except:
            courses.enrolled.add(std)
            courses.save()
            return HttpResponse("Student Enrolled")
    else:
        return HttpResponse("This Page is for student only")


def view_enrolled_user(request, id):
    try:
        val = request.COOKIES["Is_student"]
    except:
        return HttpResponse("Try Logging In First")
    if val == "False":
        e_id = request.COOKIES["id"]
        edu = Educator.objects.get(pk = e_id)
        Course = get_object_or_404(course, pk = id, creator = edu)
        list = []
        for std in Course.enrolled.all():
            list.append(std.Name)
        # if len(list) != 0:
        resp = json.dumps({"Student Name" : list})
        return HttpResponse(resp, content_type="application/json")
    else:
        return HttpResponse("This page is for Educators only")