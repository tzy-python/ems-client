from django.db import models

# Create your models here.

class User(models.Model):

    gender_choices = (
        (0,"male"),
        (1,"female")
    )
    username = models.CharField(max_length=20)
    real_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices,default=0)
    status = models.SmallIntegerField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "bz_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class Employee(models.Model):
    emp_name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="pic",default="pic/1.jpg")
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    age = models.IntegerField()

    def age_range(self):
        if self.age<20:
            return "少年"
        elif 20<=self.age<=30:
            return "青年"
        elif 30<self.age<=40:
            return "中年"
        else:
            return "老年"

    class Meta:
        db_table = "bz_employee"
        verbose_name = "员工"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name