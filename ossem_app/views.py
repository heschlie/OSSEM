from django.shortcuts import render
from ossem_app.models import Device


# Create your views here.
def device_details(request, id):
    device = Device.objects.get(id=id)
    return render(request, 'device_details.html', {'device': device})
