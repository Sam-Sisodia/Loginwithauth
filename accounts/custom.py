

from rest_framework.permissions import BasePermission
from . models import *

from rest_framework.response import Response
class UserPermission(BasePermission):
        def has_permission(self, request, view):
            try:
                user = request.user
                #print(request)
                obj = User.objects.get(username=user)
                print(obj.first_name)
                usertype = obj.usertype
            
                if request.method == "GET":
                    return True

                if request.method =="POST"  or  request.method =="PUT"  or   request.method=="DELETE": 
                    if usertype == "TEACHER":
                        return True
                return False
                
            except:
                pass
    


















            













'''
from rest_framework.permissions import BasePermission

class OnlyAdminsCanEdit(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False'''






# class UserPermission(BasePermission):
#     def has_permission(self, request, view):
#         try:
#             user = request.user
#             #print(request)
#             obj = User.objects.get(username=user)
#         # print(obj.first_name)
#             usertype = obj.usertype
        
#             if request.method == "GET":
#                 return True

#             if request.method =="POST"  or  request.method =="PUT"  or   request.method=="DELETE": 
#             #  print(usertype)
#                 if usertype == "TEACHER":
#                     return True
#             return False
#         except:
#             pass
            










# '''from rest_framework.permissions import BasePermission
# from . models import *
# from rest_framework import permissions

# class UserPermission(BasePermission):
#         def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#            if request.method in permissions.SAFE_METHODS:
#             return True

#         # Instance must have an attribute named `owner`.
#             return obj.usertype == request.user

# '''









         
#         '''user = request.user
#         obj = User.objects.get(username=user)
#         usertype = obj.usertype

#         if usertype == "STUDENT" and request.method == 'GET': 
#             return True
        
#         if request.method == 'POST' or request.method == 'PUT' or request.method == 'PATCH' or request.method == 'DELETE':
#              if usertype == "TEACHER":
#                 return True
#         return False'''


        
        
#         # if request.method == 'GET': 
#         #     return True
