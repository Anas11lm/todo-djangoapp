from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('update_task/<int:pk>/',views.update,name='update'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.delete,name='delete'),
]