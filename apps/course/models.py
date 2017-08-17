# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors["name"] = "Course First Name should be more than 5 characters"
        if len(postData['desc']) < 16:
            errors["desc"] = "Course description should be more than 15 characters"
        return errors;

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()
    def __repr__(self):
        return "<Course object: name = {} desc = {}>".format(self.name, self.desc)