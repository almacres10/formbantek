from django.db import models

# Create your models here.
class modelsPegawai(models.Model):
    id_pegawai = models.AutoField(primary_key=True, null=False)
    NAMA = models.CharField(max_length=255, null=True)
    NIP = models.CharField(max_length=255, null=True)
    IP = models.CharField(max_length=255, null=True)
    JABATAN = models.FloatField(null=True)

    class Meta:
        db_table = 'pegawai'

    def __str__(self):
        return self.NAMA
