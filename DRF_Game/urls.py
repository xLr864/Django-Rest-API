from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.Review_api),
    path('api/<int:pk>', views.Review_api),
]

