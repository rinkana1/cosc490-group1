from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('upload/', views.upload_audio, name='upload_audio'),
    path('record/', views.record_audio, name='record_audio'),
    path('analyze/', views.analyze_audio, name='analyze_audio'),
    path('text/', views.submit_text, name='submit_text')
]
