from django.shortcuts import render
from django.conf import settings
from qrcode import *
import time
from .util import generate_random_code

def qr_gen(request):
    if request.method == 'POST':
        data = request.POST['data']
        Data_to_be_encoded = generate_random_code(data)
        img = make(data + '@#$' + Data_to_be_encoded)
        img_name = 'qr' + data.strip() + str(time.time()//60) + '.png'
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)
        return render(request, 'index.html', {'img_name': img_name})
    return render(request, 'index.html')