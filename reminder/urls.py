from django.urls import path

from reminder import views


app_name = 'reminder'

urlpatterns = [
    path('reminder/', views.reminder, name='reminder'),
    path('', views.home, name='home'),

]
