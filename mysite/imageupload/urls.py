from django.urls import path 
from .views import *

urlpatterns = [ 
    path('image_upload', hotel_image_view, name = 'image_upload'), 
    path('success', success, name = 'success'),
    path('hotel_images', display_hotel_images, name = 'hotel_images'),
]
