from django.shortcuts import render
from.forms import QRCodeForm
import qrcode
import os
from django.conf import settings



def generate_qr(request):
    if request.method == 'POST':
        form=QRCodeForm(request.POST)
        if form.is_valid():
            res_name=form.cleaned_data['restaurant_name']
            url=form.cleaned_data['url']
            #generating QR
            qr = qrcode.make(url)
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            file_path=os.path.join(settings.MEDIA_ROOT,file_name)#png's
            qr.save(file_path)
            #creating img url
            qr_url=os.path.join(settings.MEDIA_URL,file_name)

            context={
                'res_name':res_name,
                'qr_url':qr_url
            }
            return render(request,'qr_result.html',context)
    else:
        form=QRCodeForm()
        context={
            'form':form
        }
        return render(request,'qr_generator.html',context)
