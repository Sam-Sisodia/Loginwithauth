
from distutils.log import info
from venv import create
from rest_framework import serializers,validators
from . models import *
from dataclasses import field, fields
from django.contrib.auth.hashers import make_password


class Registerserilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password","usertype"]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name= validated_data['last_name'],
            email = validated_data['email'],
            password = make_password(validated_data['password']),
            usertype = validated_data['usertype']
            )
      
    
        user.save()
        return user

class LogSerializer(serializers.Serializer):
   username = serializers.CharField(max_length=40)
   password =serializers.CharField(max_length=40)



class Assi_serializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id','title','description','course_chapter']



class chepter_serializer(serializers.ModelSerializer):

    course_chapter_assignments = Assi_serializer(read_only=True, many=True)
    class Meta:
        model = CourseChapter
        
        fields = ['course_id','order','course','name','modified_utc','course_chapter_assignments']


class course_serializer(serializers.ModelSerializer):
    #course_assignments= Assi_serializer(read_only=True, many=True)
    course_chapter  = chepter_serializer(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['name','description','order','created_utc','modified_utc','course_chapter']






class CourserChapterJoinSerializer(serializers.Serializer):
    course_name = serializers.CharField(required=True)
    course_description = serializers.CharField(required=True)
    chepter_name = serializers.CharField(required=True)
    Assignment_title= serializers.CharField(required=True)
    Assignment_description =  serializers.CharField(required=True)
    





    # title = serializers.CharField(required = True)
    


  #  course_assignments = serializers.ListField(required=True)

    # def create(self,validated_data):
    '''        info = Course.objects.create(
                name = validated_data['name'],
                description = validated_data['description'], 
                )
            print(info)

            chep_info =  CourseChapter.objects.create(
                        course=info,
                        name=validated_data['name'] )

            print("hllo")
            Assignment.objects.create(
                        title=validated_data['title'],
                        description=validated_data['title_description'] ,
                        course_chapter = chep_info   )

            return info '''


             
       
        







        
 
         
    

        


        
     
        


   


        
  
 
                
        





        
        

 

    

