# forms.py
from django import forms
from .models import modelsPegawai

BANTEK_CHOICES =( 
    ("0", "Pilih Jenis Masalah"), 
    ("1", "Software"), 
    ("2", "Hardware"), 
    ("3", "Jaringan Internet/Intranet"), 
    ("4", "Join Domain"), 
    ("5", "Permintaan Data"), 
)

class BantuanTeknisForm(forms.Form):
    nama_field = forms.ChoiceField(
        choices=[('', 'Pilih Nama Pegawai')] + list(modelsPegawai.objects.values_list('NAMA', 'NAMA').distinct()),
        label='Nama',
        widget=forms.Select(attrs={'class': 'border p-2 rounded-md'}),
    )
    bidang_field = forms.ChoiceField(
        choices=[('', 'Pilih Unit')] + list(modelsPegawai.objects.values_list('BIDANG', 'BIDANG').distinct()),
        label='Bidang',
        widget=forms.Select(attrs={'class': 'border w-80 p-2 rounded-md'}),
    )
    jenis_permasalahan = forms.ChoiceField(
        choices= BANTEK_CHOICES,
        label='Jenis Masalah',
        widget=forms.Select(attrs={'class': 'border w-80 p-2 rounded-md'}),
    )
    permasalahan = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'border p-2 rounded-md'}),
        required=True,
    )


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['unit'].label = 'Unit'
    #     self.fields['unit'].label_tag(attrs={'class': 'your-custom-class'})