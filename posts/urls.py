from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:postId>/', views.detail, name='detail')  # регуль виражение, захватывает цифры и передает в views.detail
]


