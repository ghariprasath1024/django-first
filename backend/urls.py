from .views import *
from django.urls import path


urlpatterns=[
    path("index/",index),
    path("apply_list/",apply_list),
    path("event_list/",event_list),
    path("test1/",test1),
    path("test2/",test2),   
    path("test3/",test3),
    path("test4/",test4),
    path("test5/",test5),
    path("delete/<int:id>/",delete, name="test1"),
    path("delete2/<int:id>/",delete2, name="test2"),
    path("delete3/<int:id>/",delete3, name="test3"),
    path("delete4/<int:id>/",delete4, name="test4"),
    path("delete5/<int:id>/",delete5, name="test5"),
    path("update1/<int:id>/",update1, name="update1"),
    path("update2/<int:id>/",update2, name="update2"),
    path("update3/<int:id>/",update3,name="update3"),
]