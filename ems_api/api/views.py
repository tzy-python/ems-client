from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from api.models import User, Employee
from utils.response import APIResponse
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
from api.serializer import UserSerializer,EmployeeSerializer

class UserAPIView(APIView):



     def post(self,request,*args,**kwargs):
         request_data = request.data
         ser = UserSerializer(data=request_data)
         ser.is_valid(raise_exception=True)
         user_obj = ser.save()

         return APIResponse(200,True,results=UserSerializer(user_obj).data)


     def get(self,request,*args,**kwargs):

          username = request.query_params.get("username")
          password = request.query_params.get("password")
          user = User.objects.filter(username=username,password=password).first()
          if user:
               data = UserSerializer(user).data
               return APIResponse(200,True,results=data)

          return APIResponse(400,False,results='000')

class EmployeeView(GenericAPIView,
                   ListModelMixin,
                   CreateModelMixin,
                   RetrieveModelMixin,
                   DestroyModelMixin,
                   UpdateModelMixin):
     queryset = Employee.objects.all()
     serializer_class = EmployeeSerializer
     lookup_field = 'id'

     def get(self,request,*args,**kwargs):
          emp_id = kwargs.get("id")
          if emp_id:
               emp_obj = self.retrieve(request,*args,**kwargs)
               return APIResponse(200,True,results=emp_obj.data)
          else:
               user_list = self.list(request,*args,**kwargs)
               return APIResponse(200,True,results=user_list.data)

     def post(self,request,*args,**kwargs):
          emp_obj = self.create(request,*args,**kwargs)
          return APIResponse(200,True,results=emp_obj.data)

     def patch(self,request,*args,**kwargs):
          request_data = request.data
          print(request_data)
          emp_obj = self.partial_update(request,*args,**kwargs)
          return APIResponse(200,True,results=emp_obj.data)

     def delete(self,request,*args,**kwargs):
          emp_obj = self.destroy(request,*args,**kwargs)
          return APIResponse(200,True,results=emp_obj.data)
