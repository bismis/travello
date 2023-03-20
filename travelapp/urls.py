from django.urls import path
from .import views

urlpatterns = [
    path('',views.fun,name='fun'),
    path('place/<int:place_id>',views.detail,name='detail')

]