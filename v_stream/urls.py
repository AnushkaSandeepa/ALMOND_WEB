from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('features/', views.features, name="features"),
    path('form/', views.form, name="form"),
    path('stream/', views.stream, name="stream"),
    path('sbinary/', views.sbinary, name="sbinary"),
    path('sgray/', views.sgray, name="sgray"),
    path('video_feed', views.video_feed, name="video_feed"),
    # path('grey_scale', views.grey_scale, name='grey_scale'),
    # path('binary_scale', views.binary_scale, name='binary_scale'),
    path('zoom/', views.zoom, name="zoom"),
    path('model/', views.model, name="model"),
    path('history/', views.history, name="history"),
    path('tour/', views.tour, name="tour"),
    path('insertrec/', views.Insertrecord, name="insertrec"),
    path('insertmod/', views.Insertmodel, name="insertmod"),
    path(r'^tempmeasure/$', views.Tempmeasure, name="tempmeasure"),
    path(r'^insertmeasure/$', views.InsertMeasure, name="insertmeasure"),
    
    
]
