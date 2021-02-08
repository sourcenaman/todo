from django.urls import path
from . import views

app_name = 'to_do'
urlpatterns = [
    path('', views.index, name='index'),
    #path('addtodo/', views.addtodo, name='addtodo'),
    path('deletetodo/', views.deletetodo, name='deletetodo'),
    #path('edittodo/', views.edittodo, name='edittodo'),
    path('updatetodo/<int:task_id>/', views.updatetodo, name='updatetodo'),

]
