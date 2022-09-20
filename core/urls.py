from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('signup', views.signup, name='signup'),
  path('signin', views.signin, name='signin'),
  path('logout', views.logout, name='logout'),
  path('upload', views.upload, name='upload'),
  path('like-post', views.like_post, name='like-post'),
  path('follow', views.follow, name='follow'),
  path('setting', views.setting, name='setting'),
  path('profile/<str:pk>', views.profile, name='profile'),
]