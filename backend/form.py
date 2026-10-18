from django.forms import ModelForm
from .models import *

class test1form(ModelForm):
    class Meta:
        model=Test1
        fields="__all__"
class test2form(ModelForm):
    class Meta:
        model=Test2
        fields="__all__"
class test3form(ModelForm):
    class Meta:
        model=Test3
        fields="__all__"
class test4form(ModelForm):
    class Meta:
        model=Test4
        fields="__all__"
class test5form(ModelForm):
    class Meta:
        model=Test5
        fields="__all__"     