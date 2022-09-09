from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser

import uuid

class User(AbstractUser):
    TYPR_CHOICES  = (
        ("TEACHER", "Teacher"),
        ("STUDENT", 'Student'),
        ("UNKNOWN", 'Unknown')
         )
    usertype = models.CharField(max_length=10 , choices= TYPR_CHOICES)


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=5000)
    order = models.IntegerField(default=0, blank=False, null=False)
    created_utc = models.DateTimeField(null=True, blank=True)
    modified_utc = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
    



class CourseChapter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey(Course, related_name='course_chapter',  on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    order = models.IntegerField(default=0, blank=False, null=False)
    created_utc = models.DateField(auto_now=True)
    modified_utc = models.DateTimeField(auto_now=True)
   
    

    

 


class Assignment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(blank=True, null=True, max_length=5000)
    #course = models.ForeignKey(Course, related_name='course_assignments', on_delete=models.CASCADE)
    course_chapter = models.ForeignKey(CourseChapter, related_name='course_chapter_assignments', on_delete=models.CASCADE)


   



























'''

# class UserProfile(models.Model):
#         user = models.OneToOneField(User, on_delete=models.CASCADE)
#         type = models.CharField(choices=TYPE_CHOICES, default=TYPE_UNKNOWN)



class Course(models.Model):
   # id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=1000)
    description = models.CharField(blank=True, null=True, max_length=5000)
    order = models.IntegerField(default=0, blank=False, null=False)
    created_utc = models.DateTimeField(null=True, blank=True)
    modified_utc = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name




class CourseChapter(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    course = models.ForeignKey('Course', related_name='course_chapter',
    on_delete=models.CASCADE)
    name = models.CharField(max_length=256, null=False, blank=False)
    order = models.IntegerField(default=0, blank=False, null=False)
    created_utc = models.DateTimeField()
    modified_utc = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
       return self.name



class Assignment(models.Model):
  #  id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.CharField(blank=True, null=True, max_length=5000)
    course = models.ForeignKey('Course', related_name='course_assignments',
    on_delete=models.CASCADE)
    course_chapter = models.ForeignKey('CourseChapter',
    related_name='course_chapter_assignments', on_delete=models.CASCADE)

    def __str__(self):
        return self.title



'''





