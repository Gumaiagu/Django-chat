from django.urls import path
from . import views

app_name = "groups"
urlpatterns = [
   path('group/', views.defining_groups, name='group'),
   path('group/create', views.create_group, name='create'),
   path('group/enter', views.enter_group, name='enter'),

   path('group/groupname/<str:group_name>', views.entred_group, name='group_entered'),
]