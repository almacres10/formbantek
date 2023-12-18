from django.shortcuts import render
from .models import modelsPegawai
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
