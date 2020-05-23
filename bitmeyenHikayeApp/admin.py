from django.contrib import admin
from .models import hikayeler,kategoriler,cevaplar

admin.site.site_header = "Bitmeyen Hikaye Yönetici Paneli"
admin.site.site_title = "Bitmeyen Hikaye Yönetici Paneli"
admin.site.index_title = "Bitmeyen Hikaye Yönetim Paneline Hoşgeldiniz!"

# Register your models here.
admin.site.register(hikayeler)
admin.site.register(kategoriler)
admin.site.register(cevaplar)
