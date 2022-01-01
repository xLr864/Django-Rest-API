from django.contrib import admin
from django.urls import path
from api import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='api/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/', views.Review_api),
    path('api/<int:pk>', views.Review_api),
]

