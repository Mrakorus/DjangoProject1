from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('post/<int:postId>/', views.detail, name='detail'),  # регуль виражение, захватывает цифры и передает в views.detail
    # path('<int:postId>/', views.detail, name='detail')
    path('page/<int:page>/', views.index, name='page')
]


