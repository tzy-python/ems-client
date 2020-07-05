from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer

from api.models import User, Employee


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            "username":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"用户名不能为空",
                    "min_length":"用户名至少为2个字符"
                }
            }
        }
    def validate(self, attrs):
        username = attrs.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise exceptions.ValidationError('用户名已存在')
        return attrs

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id","emp_name","img","salary","age","age_range")

        extra_kwargs = {
            "emp_name":{
                "required":True,
                "min_length":2,
                "error_messages":{
                    "required":"用户名不能为空",
                    "min_length":"用户名至少为2个字符"
                }
            }
        }