from django.urls import path,include
from .models import *
from .views import *

urlpatterns=[path("students/",StudentCreateView.as_view(),name="students"),
path("student/<int:pk>/",StudentDetailView.as_view(),name="student"),
path("Attendances/",AttendanceCreateView.as_view(),name="Attendances"),
path("Attendance/<int:pk>/",AttedanceDetailsView.as_view(),name="Attendance"),




]