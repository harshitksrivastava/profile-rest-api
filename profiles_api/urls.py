from django.urls import path
from profiles_api import views

urlpatterns =[
    path('hello-views/',views.HelloApiView.as_view()),
]
