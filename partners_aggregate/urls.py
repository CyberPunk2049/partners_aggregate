from django.conf import settings
from django.conf.urls.static import static
"""partners_aggregate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.generic.base import RedirectView
from django.contrib import admin

from general.views import BanksList, StoresList

from discounts.views import DiscountsList

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^banks/', BanksList.as_view(), name='banks'),
                  url(r'^stores/', StoresList.as_view(), name='stores'),
                  url(r'^discounts/', DiscountsList.as_view(), name='discounts'),
                  url(r'^$', RedirectView.as_view(pattern_name='banks', permanent=False)),
              ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)