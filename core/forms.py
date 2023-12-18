from django import forms
from .models import modelsPegawai

class BantuanTeknisForm(forms.Form):
    unit = forms.CharField(max_length=255, required=True)
    permasalahan = forms.CharField(widget=forms.Textarea, required=True)
    nama_field = forms.ChoiceField(
        choices=[('', 'Pilih Nama')] + list(modelsPegawai.objects.values_list('id_pegawai','NAMA').distinct()),
        label='Nama'
    )
