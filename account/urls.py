from django.urls import path
from . import views
app_name ="account"
urlpatterns=[
  path("login",views.s_login,name="login"),
  path('signin',views.s_signin,name="signin"),
  path("logout",views.s_logout,name="logout"),
  path("profile",views.s_profile,name="profile"),
  path("edit",views.edit_user,name="edit")
]