from . import views
from django.urls import path


urlpatterns = [
    path('', views.music),
    path('<int:pk>', views.music_detail),

]