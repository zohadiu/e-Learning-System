from django.contrib import admin
from django.urls import path
from myapp import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="Home_view"),
    path("course/", views.course, name="course"),
    path("category/", views.category, name="category"),
    path("login/", views.login_view, name="login_view"),
    path("about/", views.about, name="about"),
    path("search/", views.search, name="search"),
    path("logout/", views.logout_view, name="logout"),
    path("lecturerinfo/", views.lecturer, name="lecturerinfo"),
    path("registration/", views.registration, name="form_test"),
    path("contact/", views.contact, name="contact"),
    path("course-single/", views.singlecourse, name="singlecourse"),
    path("profile/", views.profile, name="profile")
]
