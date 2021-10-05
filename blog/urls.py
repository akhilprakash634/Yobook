from django.contrib import admin
from django.urls import path
from .import views


urlpatterns=[
    path('',views.task_view,name='task_view'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('task/',views.Tasklistview.as_view(),name='task'),
    path('detail/<int:pk>/', views.Taskdetailview.as_view(), name='detail'),
    path('update2/<int:pk>/', views.Taskupdateview.as_view(), name='update2'),
    path('delete2/<int:pk>/', views.Taskdeleteview.as_view(), name='delete2')

]
