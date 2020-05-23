from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .profile_forms import PasswordChangeForm, UserCreationForm
from .models import hikayeler, kategoriler, cevaplar
from django.http import HttpResponse, JsonResponse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['user'] = username
            return redirect('/index')
        else:
            messages.error(request, 'Hata : Kullanıcı Adı veya Şifre Hatalı. Lütfen Tekrar Deneyiniz..')
    return render(request, 'giris.html', {})


def register(request):

    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        auth_login(request, user)
        return redirect('/index')
    else:
        if request.method == 'POST':
            messages.error(request,'Hata! Lütfen oluşan hataları gideriniz.')
    return render(request, 'kayit.html',{'form':form})

def logout(request):
    auth_logout(request)
    return redirect('/login')
    return render(request, 'giris.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Şifreniz başarı ile güncellendi!')
            return redirect('/profilim')
        else:
            messages.error(request, 'Lütfen oluşan hataları gideriniz!!!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profilim.html', {
        'form': form, 'sayfaBaslik': 'Şifre Değiştirme', 'kategori': kategoriler.objects.all()

    })


def anasayfa(request):
    sonHikaye = hikayeler.objects.last()

    context = {
        'hikayeler': cevaplar.objects.filter(hikayeId=sonHikaye.id, hikayeDurum=1).order_by('-hikayeCevapTarih')[0:3],
        'sonhikaye': sonHikaye,
        'soncevap': cevaplar.objects.filter(hikayeDurum=1).last(),
        'toplamHikaye': hikayeler.objects.filter(hikayeDurum=1).count(),
        'toplamCevap': cevaplar.objects.filter(hikayeDurum=1).count(),
        'enpopulerHikaye': hikayeler.objects.filter(hikayeDurum=1).order_by('-hit')[:1],
        'enpopulerBolum': cevaplar.objects.filter(hikayeDurum=1).order_by('-hit')[:1],
        'toplamYazar': User.objects.all().count(),
        'toplamKategori': kategoriler.objects.all().count(),
        'kategori': kategoriler.objects.all(),
        'sayfaBaslik': 'Anasayfa'
    }
    return render(request, 'anaorta.html', context)


def kategori(request, id):
    kategoris = kategoriler.objects.get(id=id)
    context = {
        'hikayeler': hikayeler.objects.filter(anakategoriId=id, hikayeDurum=1).order_by('-id'),
        'kategori': kategoriler.objects.all(),
        'sayfaBaslik': kategoris.kategoriAdi
    }
    return render(request, 'kategori.html', context)


def hikaye(request, id):
    hikaye = hikayeler.objects.get(id=id)
    context = {
        'hikaye': hikaye,
        'cevap': cevaplar.objects.filter(hikayeId=id, hikayeDurum=1),
        'kategori': kategoriler.objects.all(),
        'sayfaBaslik': hikaye.hikayeAdi
    }
    return render(request, 'hikaye.html', context)

def cevapla(request, id):
    hikaye = hikayeler.objects.get(id=id)
    if request.method == 'POST':
        cevapla = cevaplar(hikayeId_id=id, hikayeCevapMetni=request.POST['hikayeCevap'], uyeId_id=request.user.id, hit=0, hikayeDurum=0)
        cevapla.save()
        messages.success (request, 'Devam metniniz başarı ile kayıt edildi. Seçilirse en kısa zamanda yayına alınacaktır. Hikayeye katkılarınızdan dolayı teşekkürler...')
    context = {
        'hikaye': hikaye,
        'kategori': kategoriler.objects.all(),
        'sayfaBaslik': hikaye.hikayeAdi+' Adlı Hikayeye Devam Metni Yaz!'
    }
    return render(request, 'cevap.html', context)

def begen(request, idh,idc):
    if request.is_ajax():
        if(idc == 0 and request.POST['islem'] == '+1'):
            hikayeler.objects.filter(id=idh).update(hit= int(hikayeler.objects.get(id=idh).hit) + 1)
        elif(idc == 0 and request.POST['islem'] == '-1'):
            hikayeler.objects.filter(id=idh).update(hit= int(hikayeler.objects.get(id=idh).hit) - 1)
        elif(idc != 0 and request.POST['islem'] == '+1'):
            cevaplar.objects.filter(id=idc).update(hit= int(cevaplar.objects.get(id=idc).hit) + 1)
        elif(idc != 0 and request.POST['islem'] == '-1'):
            cevaplar.objects.filter(id=idc).update(hit= int(cevaplar.objects.get(id=idc).hit) - 1)
        else:
            return JsonResponse({'messages': 'Hatalı bir işlemde bulunmaya çalıştınız!'})
        return JsonResponse({'messages': 'Oy verdiğiniz için teşekkürler, Oyunuz Kayıt Edildi.'})
    else:
        return redirect('/hikaye/'+str(idh))