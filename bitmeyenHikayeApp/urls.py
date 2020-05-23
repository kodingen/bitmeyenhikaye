
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('anasayfa', views.anasayfa, name='anasayfa'),
    path('index', views.anasayfa, name='anasayfa'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profilim', views.change_password, name='profilim'),
    path('kategori/<int:id>/', views.kategori, name='kategori'),
    path('begen/<int:idh>/<int:idc>/', views.begen, name='begen'),
    path('hikaye/<int:id>/', views.hikaye, name='hikaye'),
    path('cevap-yaz/<int:id>/', views.cevapla, name='cevap-yaz'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='sifresifirla/password_reset_form.html', subject_template_name='sifresifirla/password_reset_subject.txt', email_template_name='sifresifirla/password_reset_email.html', ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='sifresifirla/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='sifresifirla/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='sifresifirla/password_reset_complete.html'), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


