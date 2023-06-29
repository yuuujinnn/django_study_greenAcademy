from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'), # 목록
    path('<int:post_id>/', views.detail, name='detail'), # 상세 페이지
    path('post/create/', views.post_create, name='post_create'),
    path('category/<str:slug>/', views.category_page,
         name='category_page'), # 카테고리별 페이지
]