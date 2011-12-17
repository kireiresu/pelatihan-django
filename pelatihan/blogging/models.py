from django.db import models

# Create your models here.

class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    tgl_post = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Daftar Artikel'
        verbose_name = 'Artikel'
   
    def __unicode__(self):
        return self.judul
