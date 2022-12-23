"""xmlproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from . import views
from django.conf import settings #add this
from django.conf.urls.static import static #add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),        
    path('validate_dtd',views.validate_xml_with_DTD),
    path('validate_xsd',views.validate_xml_with_XSD),
    path('xml_json',views.Xml_to_Json_convert),
    path('dtd_xsd',views.dtd_to_xsd),
    path('xslt_html',views.xslt_to_html_transfer)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
