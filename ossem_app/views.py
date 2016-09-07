from django.shortcuts import render
from ossem_app.models import Device


# Create your views here.
def device_details(request, id):
    device = Device.objects.get(id=id)
    return render(request, 'device_details.html', {'device': device})


def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})
