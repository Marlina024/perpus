from django.shortcuts import render
from .models import Peminjaman, Buku, Anggota
from django.db.models import Count

# View untuk laporan anggota prodi yang sering meminjam
def laporan_peminjaman_per_prodi(request):
    hasil_peminjaman = (
        Peminjaman.objects
        .values('idAng__nim__idProdi__namaProdi')  # Pastikan relasi ini benar
        .annotate(jumlah_peminjaman=Count('idPin'))
        .order_by('-jumlah_peminjaman')
    )
    return render(request, 'laporan_peminjaman_per_prodi.html', {'hasil_peminjaman': hasil_peminjaman})

# View untuk laporan buku yang sering dipinjam
def laporan_buku_populer(request):
    laporan_buku_populer = (
        Buku.objects
        .annotate(jumlah_peminjaman=Count('detpin'))  # Pastikan relasi detpin sudah benar
        .values('namaBuku', 'jumlah_peminjaman')
        .order_by('-jumlah_peminjaman')
    )
    return render(request, 'laporan_buku_populer.html', {'laporan_buku_populer': laporan_buku_populer})

# View untuk laporan anggota terbanyak dari prodi mana
def laporan_anggota_per_prodi(request):
    laporan_anggota_per_prodi = (
        Anggota.objects
        .values('nim__idProdi', 'nim__idProdi__namaProdi')  # Pastikan relasi ini benar
        .annotate(total_anggota=Count('idAng'))
        .order_by('-total_anggota')
    )
    return render(request, 'laporan_anggota_per_prodi.html', {'laporan_anggota_per_prodi': laporan_anggota_per_prodi})
