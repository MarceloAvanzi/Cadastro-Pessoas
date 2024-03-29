from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('api.urls')),
    path('pessoas/', include('pessoa.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]