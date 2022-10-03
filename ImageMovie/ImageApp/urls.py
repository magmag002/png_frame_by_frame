from django.urls import path
from. import views

app_name = 'image_app'

urlpatterns =[
    path('index/', views.index, name='index'),
    path('upload/', views.uploadfunc, name='upload'),
    path('movie/', views.ImageMovie, name='movie'),
]