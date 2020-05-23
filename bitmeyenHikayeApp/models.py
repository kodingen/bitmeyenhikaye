from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class kategoriler(models.Model):
    kategoriAdi = models.CharField(blank=False, null=False, max_length=250, verbose_name='Kategori Adı')
    kategoriIcon = models.CharField(blank=False, null=False, max_length=250, verbose_name='Kategori Icon')
    class Meta:
        verbose_name_plural = "Kategori Listele ve Oluştur"
    def __str__(self):
        return "%s - %s" % (self.id, self.kategoriAdi)

class hikayeler(models.Model):
    yayindurum = (('0', 'Yanınlanmamış'),('1', 'Yayınlanmış'))
    anakategoriId = models.ForeignKey(kategoriler, blank=False, null=False, on_delete=models.CASCADE, verbose_name='Ana Kategori Adı')
    hikayeAdi = models.CharField(blank=False, null=False, max_length=250, verbose_name='Hikaye Adı')
    hikayeOzet = models.TextField(blank=False, null=False, verbose_name='Hikaye Özeti')
    hikayeMetni = models.TextField(blank=False, null=False, verbose_name='Hikaye Metni')
    hikayeGorsel = models.ImageField(blank=True, null=True, verbose_name='Hikaye Görseli')
    hikayeTarih = models.DateField(verbose_name='Hikaye Yayın Tarihi', editable=False, default=now)
    hikayeDurum = models.CharField(blank=False, null=False, max_length=50, choices=yayindurum, verbose_name='Hikaye Yayın Durumu', default=1)
    hit = models.CharField(blank=True, null=True, max_length=250,verbose_name='Hit', default=0)
    class Meta:
        verbose_name_plural = "Hikaye Listele ve Oluştur"
    def __str__(self):
        return "%s - %s" % (self.id, self.hikayeAdi)


class cevaplar(models.Model):
    yayindurum = (('0', 'Yanınlanmamış'),('1', 'Yayınlanmış'))
    hikayeId = models.ForeignKey(hikayeler,blank=False, null=False, on_delete=models.CASCADE, verbose_name='Hikaye Adı')
    uyeId = models.ForeignKey(User,blank=False, null=False, on_delete=models.CASCADE, verbose_name='Üye Adı')
    hikayeCevapMetni = models.TextField(blank=False, null=False, verbose_name='Hikaye Devam Metni')
    hikayeCevapTarih = models.DateField(verbose_name='Hikaye Devam Metni Yayın Tarihi', editable=False, default=now)
    hikayeDurum = models.CharField(blank=False, null=False, max_length=50, choices=yayindurum, verbose_name='Hikaye Devam Metni Yayın Durumu', default=0)
    hit = models.CharField(blank=True, null=True, max_length=250,verbose_name='Hit', default=0)
    class Meta:
        verbose_name_plural = "Hikaye Yanıtları Listesi"
    def __str__(self):
        return "%s - %s" % (self.hikayeCevapTarih, self.hikayeId.hikayeAdi)