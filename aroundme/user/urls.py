from django.urls import path
from .views import *

urlpatterns=[
    path('uh/',Uhome.as_view(),name='uh'),
    path('pro/',Profile.as_view(),name='pro'),
    path('abio/',Addbio.as_view(),name='abio'),
    path('editbio/<int:pk>', Editbio.as_view(),name="editbio"),
    path('cpw/',Cpassword.as_view(),name='cpw'),
    path('mb/',Myblog.as_view(),name='mb'),
    path('eb/<int:pk>',Eblog.as_view(),name='eb'),
    path('db/<int:pk>',Dblog.as_view(),name='db'),
    path('addc/<int:pid>',addcomment,name='addc'),
    path('addl/<int:pid>',addlike,name='addl'),

    

    
    
    ]