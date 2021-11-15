from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,CustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns=[
    path('login/',CustomLoginView.as_view(),name="login"),
     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
       path('register/', RegisterPage.as_view(), name='register'),
    path('',TaskList.as_view(),name='todo'),
    path('tasks/<int:pk>/',TaskDetail.as_view(),name='tasks'),
    path('createform',TaskCreate.as_view(),name='createform'),
    path('taskupdate/<int:pk>/',TaskUpdate.as_view(),name='taskupdate'),
    path('taskDelete/<int:pk>/',TaskDelete.as_view(),name='taskDelete'),
]