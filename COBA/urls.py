from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import reverse  # Untuk mendapatkan URL dari view yang sudah didefinisikan
from pustaka import views  # Pastikan pustaka adalah nama aplikasi Anda

# Fungsi untuk halaman beranda
def home(request):
    # Menggunakan reverse untuk mendapatkan URL view berdasarkan nama URL
    laporan_buku_populer_url = reverse('laporan_buku_populer')
    laporan_anggota_per_prodi_url = reverse('laporan_anggota_per_prodi')
    laporan_peminjaman_per_prodi_url = reverse('laporan_peminjaman_per_prodi')

    return HttpResponse(f"""
        <html>
        <head>
            <title>Selamat Datang</title>
            <style>
                body {{
                    margin: 0;
                    padding: 0;
                    font-family: 'Arial', sans-serif;
                    background-color: #f4f4f9;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }}
                .header {{
                    background-color: #32CD32;
                    width: 100%;
                    padding: 20px 0;
                    position: fixed;
                    top: 0;
                    left: 0;
                    text-align: center;
                    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
                }}
                .header h1 {{
                    color: white;
                    font-size: 2.5em;
                    margin: 0;
                    letter-spacing: 1px;
                }}
                .content {{
                    margin-top: 120px;  /* Menghindari overlap dengan header */
                    padding: 20px;
                    max-width: 800px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                }}
                .intro {{
                    font-size: 1.2em;
                    color: #333;
                    margin-bottom: 40px;
                }}
                .button-container {{
                    display: flex;
                    gap: 20px;
                    justify-content: center;
                    flex-wrap: wrap;
                }}
                .button-container a {{
                    text-decoration: none;
                    background-color: #4CAF50;
                    color: white;
                    padding: 15px 30px;
                    border-radius: 8px;
                    font-size: 1.4em;
                    transition: background-color 0.3s, transform 0.3s ease;
                }}
                .button-container a:hover {{
                    background-color: #45a049;
                    transform: translateY(-5px);
                }}
                .button-container a:active {{
                    transform: translateY(2px);
                }}
                .footer {{
                    position: absolute;
                    bottom: 20px;
                    font-size: 1em;
                    color: #bbb;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Selamat Datang di Sistem Informasi Perpustakaan</h1>
            </div>
            <div class="content">
                <div class="intro">
                    <p>Selamat datang di platform yang memudahkan Anda untuk mengakses informasi perpustakaan kami. Melalui sistem ini, Anda dapat memantau buku-buku populer, laporan anggota berdasarkan program studi, dan laporan peminjaman yang dapat membantu Anda dalam mengelola koleksi perpustakaan dengan lebih efektif.</p>
                </div>
                <div class="button-container">
                    <a href="{laporan_buku_populer_url}">Buku Populer</a>
                    <a href="{laporan_anggota_per_prodi_url}">Anggota Prodi</a>
                    <a href="{laporan_peminjaman_per_prodi_url}">Laporan Peminjaman Prodi</a>
                </div>
            </div>
            <div class="footer">
                <p>&copy; 2024 Perpustakaan Universitas X | Semua Hak Cipta Dilindungi</p>
            </div>
        </body>
        </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Halaman utama
    path('peminjaman-prodi/', views.laporan_peminjaman_per_prodi, name='laporan_peminjaman_per_prodi'),
    path('buku-populer/', views.laporan_buku_populer, name='laporan_buku_populer'),
    path('anggota-prodi/', views.laporan_anggota_per_prodi, name='laporan_anggota_per_prodi'),
]
