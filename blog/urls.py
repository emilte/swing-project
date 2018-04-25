from django.urls import path, include
from blog import views

urlpatterns = [
    #path('logout', views.logout, name="logout"),
    path('<int:post_id>', views.detail, name="detail"),
]
