from . import views
from django.urls import path
from .views import music
from .views import music_detail

urlpatterns = [
    path('', views.music),
    path('<int:pk>', views.music_detail),

]