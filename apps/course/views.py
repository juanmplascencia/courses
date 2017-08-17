# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from .models import *
# Create your views here.

#GET
def index(request):
    courses = Course.objects.all()
    context = {'courses' : courses}
    return render(request,'course/index.html', context = context)
def destroy(request,number):
    course = Course.objects.get(id = number)
    context = {'course' : course}
    return render(request,'course/message.html', context = context)

#POST
def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('course_index'))
        new = Course.objects.create( name = request.POST['name'], desc = request.POST['desc'])
        return redirect(reverse('course_index'))


def remove(request,number):
    if request.method == "POST":
        Course.objects.get(id = number).delete()
        return redirect(reverse('course_index'))