from django.urls import path
from . import views

urlpatterns = [
    path('venues', views.VenueList.as_view(), name='venue-list'),
    path('events/', views.EventList.as_view(), name='event-list'),
    path('venues/<int:pk>', views.VenueDetail.as_view(), name='venue-detail'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
]