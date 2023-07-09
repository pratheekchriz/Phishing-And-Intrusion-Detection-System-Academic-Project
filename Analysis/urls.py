from django.urls import path
from Analysis.views import upload_packet

urlpatterns = [
    path('packet_analysis/upload/', upload_packet, name='upload_packet'),
]
