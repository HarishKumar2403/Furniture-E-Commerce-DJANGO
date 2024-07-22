"""
AdminURL 
  
"""
from django.urls import path

from . import views
urlpatterns = [
    path('',views.user_admin_register,name='user_admin_register'),
    path('login/',views.user_admin_login,name='user_admin_login'),
    path('admin/',views.user_admin,name='user_admin'),
    path('logout/',views.user_admin_logout,name='user_admin_logout'),
    # path('post/',views.admin_post,name='admin_post'),
    
    path('profile/<int:id>',views.admin_profile,name='admin_profile'),
    path('delete/Bed',views.admin_post_delete,{'category': 'Bed'},name='Delete-Bed'),
    path('delete/Gamming_Chair',views.admin_post_delete,{'category': 'Gamming_Chair'},name='Delete-Gamming_Chair'),

    path('post/Upload-Bed/',views.admin_post,{'category': 'Bed'},name='Upload_Bed'),
    path('name/Bed/', views.admin_post_name, {'category': 'Bed'}, name='Bed'),
    path('name/Bed/<int:id>',views.admin_post_details,{'category': 'Bed'},name='Bed_details'),

    path('post/Upload-Gaming_Chair/',views.admin_post,{'category': 'Gaming_Chair'},name='Upload_Gaming_Chair'),
    path('name/Gaming-Chair/', views.admin_post_name, {'category': 'Gaming_Chair'}, name='Gaming_Chair'),
    path('name/Gaming-Chair/<int:id>',views.admin_post_details,{'category': 'Gaming_Chair'},name='Gaming_Chair_details'),
   
]
