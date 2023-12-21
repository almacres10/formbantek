from django.shortcuts import render, redirect
from .models import modelsPegawai, modelsTiket
from .forms import BantuanTeknisForm

# Create your views here.

def index(request):
    return render(request, "core/index.html")


def formBantek(request):
    form = BantuanTeknisForm()
    context = {
        'form': form,
    }

    return render(request, 'core/index.html', context)

def tiketBantek(request):
    if request.method == 'POST':
        form = BantuanTeknisForm(request.POST)

        if form.is_valid():
            nama = form.cleaned_data['nama_field']
            bidang = form.cleaned_data['bidang_field']
            jenis_masalah = form.cleaned_data['jenis_permasalahan']
            permasalahan = form.cleaned_data['permasalahan']

            # Simpan data di model
            tiket = modelsTiket(NAMA=nama, BIDANG=bidang, JENIS_MASALAH=jenis_masalah, PERMASALAHAN=permasalahan)
            tiket.save()
                
            return redirect('core:daftarTiket')

    
    else:
        form = BantuanTeknisForm()


def daftarTiket(request):
    tiket_list = modelsTiket.objects.all()

    return render(request, 'core/tiket.html', {'tiket_list': tiket_list})