"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# import debug_toolbar

# 1
# http://127.0.0.1:8000/pollss
# http://127.0.0.1:8000/upload/
# 2
# http://127.0.0.1:8000/pollssupup
# http://127.0.0.1:8000/upload/upup

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'pollss', include('polls.urls')),

    path(r'upload/', include('polls.urls')),

    # path(r'^__debug__/', include(debug_toolbar.urls)),
]

from django.conf import settings
from django.conf.urls import include, url
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

from polls import views as error_views
handler404 = error_views.error_404
handler500 = error_views.error_500

# handler404 = "polls.views.error_404"
# handler500 = "polls.views.error_500"