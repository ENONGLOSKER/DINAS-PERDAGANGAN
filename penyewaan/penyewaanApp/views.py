from django.shortcuts import render,redirect
from . models import Pasar,Penyewa
from . forms import penyewaForm

# Create your views here.
def about(request):
    template_name='about.html'
    return render(request, template_name)

def sewa(request):
    # ambil semua isi dri tabel penyewa
    datas = Penyewa.objects.all().order_by('-id')

    # data forms
    sewa = penyewaForm(request.POST or None)
    if request.method == 'POST':
        if sewa.is_valid():
            sewa.save()
        return redirect('home:detail')

    # lempar data dari database ke tamplate
    context={
        'datas':datas,
        'sewa':sewa,
    }

    template_name='sewa.html'
    return render(request, template_name,context)

def detail(request):
    # ambil semua isi dri tabel penyewa
    datas = Penyewa.objects.all().order_by('-id')

    # lempar data dari database ke tamplate
    context={
        'datas':datas,
    }

    template_name='detail.html'
    return render(request, template_name,context)

def login(request):
    template_name='login.html'
    return render(request, template_name)