from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'ЕЭТК'
admin.site.index_title = 'Админка сайта'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('raspisanie.urls'))
]
