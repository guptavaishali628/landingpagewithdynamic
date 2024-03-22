from django.urls import path
from .views import *

urlpatterns = [
    # path('home/',index,name='index'),
    path('home/<int:id>',index,name='index'),
    path('home/<str:id>',index,name='index'),
    path('home/<slug:id>',index,name='index'),
    path('home/<path:id>',index,name='index'),
    path('all/<path:id>/<slug:pk>/<str:idpk>/<int:pkid>',combination,name='combination'),
]