from django.shortcuts import render
from django.http import HttpResponse
from.models import Soz,H_or_X

def index(request):
    return render(request,'H_va_x/index.html')

def result(request):
        html = request.GET.get("search")
        if Soz.objects.filter(correct=html):
            soz = Soz.objects.filter(correct=html)
            n_soz = H_or_X.objects.filter(soz_id=soz[0].id)
            return render(request, "H_va_x/result.html", {"t_soz": soz[0].correct, "n_soz": n_soz})
        elif H_or_X.objects.filter(wrong=html):
            ww = H_or_X.objects.filter(wrong=html)
            cw = Soz.objects.filter(correct=ww[0].soz_id)
            ww=H_or_X.objects.filter(soz_id=cw[0].id)
            return render(request, "H_va_x/result.html", {"n_soz": ww, "t_soz": cw[0].correct})
        else:
            a="Bazada bunday so'z yoq"
            return render(request,"H_va_x/result.html",{"t_soz":a})
