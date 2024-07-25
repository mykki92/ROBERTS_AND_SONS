from django.contrib import admin
from django.urls import path
from home.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home')
]
