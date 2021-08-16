from django.urls import path
from apps.imagesprocessor.views import ImageProcessor

urlpatterns = [
    path('imagenproccessorAPI', ImageProcessor.as_view(), name='imageprocessorAPI'),
]