from django.urls import path
from .views import index, login_view, register, user_profile, change_password, logout_view
#from . import views


# urlpatterns = [
#     path('home/', views.index, name='home'),
#     path('register/', views.register, name='register'),
#     path('profile/', views.user_profile, name='user_profile'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('change-password/', views.change_password, name='change_password'),
#
# ]


urlpatterns = [
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('profile/', user_profile, name='user_profile'),
    path('change_password/', change_password, name='change_password'),
    path('logout/', logout_view, name='logout'),

]