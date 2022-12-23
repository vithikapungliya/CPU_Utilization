from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('exec',views.exec,name='exec'),
    path('dis',views.dis,name='dis'),
    path('execu',views.execu,name='execu'),
    path('grp',views.grp,name='grp'),
    path('stat/',views.stat,name='stat'),
    path('scrap',views.scrap,name='scrap'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]