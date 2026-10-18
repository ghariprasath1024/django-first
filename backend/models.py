from django.db import models

# Create your models here.
class Test1(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    register_no =models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
class Test2(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    register_no =models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Test3(models.Model):
    name=models.CharField(max_length=20)
    department=models.CharField(max_length=20)
    register_no =models.CharField(max_length=20)
    email=models.CharField(max_length=100)
    language=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
class Test4(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    register_no = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Test5(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    register_no = models.CharField(max_length=20)
    email = models.EmailField()
    language = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name