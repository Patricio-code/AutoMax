"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from main import urls as main_app_urls
from users import urls as users_app_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(main_app_urls)),
    path('',include(users_app_urls)),
]

#Sirvo a urlpatterns de una url que comienza con MEDIA_URL y busca en MEDIA_ROOT. Esto no se puede lograr con path, porque este espera como segundo parámetro un view
# Hacer esto con static solo se usa para la etapa develop, no para produccion. En produccion se guardan en el host los archivos staticos, por eso agrego el siguiente if
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)