from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'front_end'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="front_end/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
]
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'front_end'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name="front_end/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.Signup.as_view(), name='signup'),
]

#urls mainly for front end i.e signup,login ans logout are routed here