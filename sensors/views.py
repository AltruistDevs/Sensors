from django.shortcuts import render, get_object_or_404,redirect
from .models import Sensor, User
from .forms import SensorForm

def userProfile(request):
    user = get_object_or_404(User, username=request.user.username)
    sensor_list = user.sensor_set.all()

    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            sensor_id = request.POST.get('sensor_id')
            sensor = get_object_or_404(Sensor, id=sensor_id, user=user)
            form = SensorForm(request.POST, instance=sensor)
            if form.is_valid():
                form.save()
                return redirect('/')
    else:
        form = SensorForm()

    context = {
        'form': form,
        'sensor_list': sensor_list
    }
    
  
    return render(request, 'user.html', context)
