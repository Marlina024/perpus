from django.urls import path
from . import views

urlpatterns = [
    path('prodi/', views.ProdiListView.as_view(), name='prodi-list'),
    path('mahasiswa/', views.MahasiswaListView.as_view(), name='mahasiswa-list'),
    path('nohp/', views.NoHpListView.as_view(), name='nohp-list'),
    path('anggota/', views.AnggotaListView.as_view(), name='anggota-list'),
    path('buku/', views.BukuListView.as_view(), name='buku-list'),
    path('peminjaman/', views.PeminjamanListView.as_view(), name='peminjaman-list'),
    path('detail-peminjaman/', views.DetPinListView.as_view(), name='detail-peminjaman-list'),
    path('kategori/', views.KategoriListView.as_view(), name='kategori-list'),
    path('katbuk/', views.KatBukListView.as_view(), name='katbuk-list'),
]
