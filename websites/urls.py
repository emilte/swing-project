from django.urls import path, include
from websites import views

urlpatterns = [
    path('external', views.external, name="external"),
    path('english', views.english, name="english"),
    path('contact', views.contact, name="contact"),
    path('music', views.music, name="music"),
    path('about', views.about, name="about"),
    path('courses', views.courses, name="courses"),
    path('faq', views.faq, name="faq"),

]
