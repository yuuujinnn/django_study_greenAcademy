
from django.contrib import admin
from django.urls import path, include
from board import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index), #http://127.0.0.1:8000/
    path('board/', include('board.urls')), #http://127.0.0.1:8000/board
    path('common/', include('common.urls')), #http://127.0.0.1:8000/common
]
