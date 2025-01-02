from django.urls import path
from .views import *


urlpatterns = [
    path('movies/', MovieListCreate.as_view(), name='movie-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-view'),
    path('movies/stats/', MovieStatsView.as_view(), name='movie-stats-view'),
]
