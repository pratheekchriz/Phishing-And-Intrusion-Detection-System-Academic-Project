from django.shortcuts import render
from django.http import HttpResponse
from .models import CapturedPacket

def upload_packet(request):
    if request.method == 'POST' and 'packet' in request.FILES and 'prediction' in request.POST:
        packet_file = request.FILES['packet']
        packet_data = packet_file.read()
        prediction = request.POST['prediction']

        
        captured_packet = CapturedPacket(
            packet_data=packet_data,
            prediction=prediction
        )
        captured_packet.save()

        return HttpResponse('Packet uploaded and stored successfully.')
    else:
        return HttpResponse('Invalid request.')

