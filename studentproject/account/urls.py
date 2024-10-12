from django.urls import path,include
from .views import *

urlpatterns=[path("register/",RegisterCreate.as_view(),name="register"),
path("login/",Loginview.as_view(),name="login"),
]