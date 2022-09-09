
# Create your views here.
from functools import partial
from django.shortcuts import render
from rest_framework .views import APIView
from . serializer import *
from . models import *
from rest_framework import status
 
from  rest_framework.viewsets import ModelViewSet
 
from rest_framework.response import Response  
from django.contrib.auth import authenticate , login , logout
from rest_framework.generics import ListCreateAPIView,GenericAPIView, RetrieveUpdateDestroyAPIView,CreateAPIView

from . custom import *

class registerUsereView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Registerserilizer
    def post(self,request,*args, **kwargs):
        serializer = Registerserilizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            #password = serializer.validated_data['password']
            user = serializer.save()
    
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class (CreateView):


class Loginview(CreateAPIView):
    queryse = User.objects.all()
    serializer_class  = LogSerializer
    
    def post(self,request, *args, **kwargs):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            if user:
               login(request,user)
               return Response( status=status.HTTP_200_OK)

            if user is  None:
                 return Response( status=status.HTTP_400_BAD_REQUEST,)
            

        

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from . custom import *

class CourseApi_Apiview(ModelViewSet):
    authentication_classes = [SessionAuthentication] 
    permission_classes =[ UserPermission,IsAuthenticated]
    
    queryset = Course.objects.all()
    serializer_class = course_serializer
    




class Chapter_apiview(ModelViewSet):
    authentication_classes = [SessionAuthentication] 
    permission_classes =[ UserPermission,IsAuthenticated]
  
    queryset = CourseChapter.objects.all()
    serializer_class = chepter_serializer
   

class Assi_view(ModelViewSet):
    authentication_classes = [SessionAuthentication] 
    permission_classes =[ UserPermission,IsAuthenticated]
    queryset = Assignment.objects.all()
    serializer_class = Assi_serializer




class all_view(ListCreateAPIView):
    authentication_classes = [SessionAuthentication] 
    permission_classes =[ UserPermission,IsAuthenticated]

    queryset = ""
    serializer_class = CourserChapterJoinSerializer
    def post(self,request):
        serializer =  CourserChapterJoinSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data['course_name']
            description = serializer.validated_data['course_description']
            info = Course.objects.create(
                name = name,
                description = description
                )
            print(info)

            chep_info =  CourseChapter.objects.create(
                        course=info,
                        name=serializer.validated_data['chepter_name'] )
            print(chep_info)

            Assignment.objects.create(
                        course_chapter=chep_info,
                        title = serializer.validated_data['Assignment_title'],
                        description = serializer.validated_data['Assignment_description']
                )

        return Response(status=status.HTTP_200_OK)

    # def patch(self,request,id):
    #     serializer =  CourserChapterJoinSerializer(data=request.data,partial= True)
    #     if serializer.is_valid(raise_exception=True):
    #         name = serializer.validated_data['course_name']
    #         description = serializer.validated_data['course_description']
    #         info = Course.objects.create(
    #             name = name,
    #             description = description
    #             )
    #         print(info)

    #         chep_info =  CourseChapter.objects.create(
    #                     course=info,
    #                     name=serializer.validated_data['chepter_name'] )
    #         print(chep_info)

    #         Assignment.objects.create(
    #                     course_chapter=chep_info,
    #                     title = serializer.validated_data['Assignment_title'],
    #                     description = serializer.validated_data['Assignment_description']
    #             )

    #     return Response(status=status.HTTP_200_OK)
        

    
      
            

    
    






























'''
{
    "course_name": "mmmmm",
    "description": "mmdissss",
    "course_chapter": [{"name": "sajl"}],
    "course_assignments": [{"name":"9808"}]
}'''
















































# class CourseChepterApiview(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseChapterserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]



# class CourseChepterupdate(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseChapterserializer
#     lookup_field = 'id'
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]







# class Assignment_APIview(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = Assignmentserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]

# class Assignment_update(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = Assignmentserializer
#     lookup_field = 'id'
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]



# class CourseApi_Apiview(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = Courseserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]


# class CourseApi_update(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = Courseserializer
#     lookup_field = 'id'
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]






# class stuaddapiview(generics.ListCreateAPIView):
#     queryset = Stu.objects.all()
#     serializer_class = stuserilizser
#     authentication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]






# class CourseApi_Apiview(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = Courseserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]


    
    

# class CourseChepterApiview(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = CourseChapterserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]
  




# class Assignment_APIview(viewsets.ModelViewSet):
#     queryset = Course.objects.all()
#     serializer_class = Assignmentserializer
#     authentication_classes = [SessionAuthentication]
#     permission_classes =[ UserPermission,IsAuthenticated]


 #permission_classes = [IsAuthenticated, OnlyAdminsCanEdit]
