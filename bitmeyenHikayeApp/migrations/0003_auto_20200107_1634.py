# Generated by Django 2.1.7 on 2020-01-07 13:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bitmeyenHikayeApp', '0002_auto_20200107_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cevaplar',
            name='hikayeCevapTarih',
            field=models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Hikaye Devam Metni Yayın Tarihi'),
        ),
        migrations.AlterField(
            model_name='cevaplar',
            name='hikayeDurum',
            field=models.CharField(default=0, max_length=50, verbose_name='Hikaye Devam Metni Yayın Durumu'),
        ),
        migrations.AlterField(
            model_name='hikayeler',
            name='hikayeDurum',
            field=models.CharField(default=1, max_length=50, verbose_name='Hikaye Yayın Durumu'),
        ),
        migrations.AlterField(
            model_name='hikayeler',
            name='hikayeGorsel',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Hikaye Görseli'),
        ),
        migrations.AlterField(
            model_name='hikayeler',
            name='hikayeTarih',
            field=models.DateField(default=django.utils.timezone.now, editable=False, verbose_name='Hikaye Yayın Tarihi'),
        ),
    ]