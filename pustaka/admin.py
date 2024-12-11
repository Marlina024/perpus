from django.contrib import admin
from .models import Prodi,Mahasiswa, NoHp, Anggota,Buku,Peminjaman,DetPin,Kategori,KatBuk
# Register your models here.
admin.site.register (Prodi)
admin.site.register (Mahasiswa)
admin.site.register (NoHp)
admin.site.register (Anggota)
admin.site.register (Buku)
admin.site.register(Peminjaman)
admin.site.register(DetPin)
admin.site.register(Kategori)
admin.site.register(KatBuk)
