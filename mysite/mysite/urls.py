"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from polls import views
from feedback.views import FeedbackView


urlpatterns = [
    path('healthcheck/',views.healthcheckview),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'), name='polls'),
    path('generate/', views.GenerateRandomUserView.as_view(), name='generate'),
    path('', views.UsersListView.as_view(), name='users_list'),
    path('feedback/', FeedbackView.as_view(), name="feedback"),
    path('image/', include('imageupload.urls')),
]

from django.conf import settings 
from django.conf.urls.static import static 
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                            document_root=settings.MEDIA_ROOT)