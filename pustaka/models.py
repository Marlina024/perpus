from django.db import models

# Create your models here.
class Prodi(models.Model):
    idProdi = models.CharField(max_length=12, null=False, primary_key=True, verbose_name="ID Program Studi")
    namaProdi = models.CharField(max_length=100, verbose_name="Nama Program Studi")

    class Meta:
        verbose_name_plural = 'Prodi'
    def __str__(self):
        return f'{self.idProdi} - {self.namaProdi}'
    
    
class Mahasiswa(models.Model):
    nim = models.CharField(max_length=12, null=False, primary_key=True, verbose_name="NIM")
    idProdi = models.ForeignKey(Prodi, on_delete=models.CASCADE, verbose_name="Program Studi")
    namaDepan = models.CharField(max_length=50, null=False, verbose_name="Nama Depan")
    namaBelakang = models.CharField(max_length=30, null=False, verbose_name="Nama Belakang")
    alamat =  models.CharField(max_length=30,null=False, verbose_name="Alamat")
    tglLahir =models.DateField(null=False,verbose_name= 'Tanggal Lahir')
    class Meta:
        verbose_name_plural = 'Mahasiswa'

    @property
    def nama_Prodi(self):
        # Mengambil nama anggota peminjam dari model terkait
        return self.idProdi.namaProdi
    def __str__(self):
        return f'{self.nim} - {self.namaDepan} {self.namaBelakang}- {self.idProdi.namaProdi} '
    
class NoHp(models.Model):
    idNo = models.AutoField(primary_key=True, null=False, verbose_name="ID Nomor HP")
    nim = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, verbose_name="Mahasiswa")
    noHp = models.CharField(max_length=12, null=False, verbose_name="Nomor HP")

    class Meta:
        verbose_name_plural = 'NoHP'

    def __str__(self):
        return f'{self.idNo} - {self.nim} {self.noHp}'


# Model Anggota
class Anggota(models.Model):
    idAng = models.AutoField(primary_key=True, null=False, verbose_name="ID Anggota")
    nim = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE, verbose_name="Mahasiswa")
    nama = models.CharField(max_length=30, null=False, verbose_name="Nama Anggota")

    class Meta:
        verbose_name_plural = 'Anggota'
 
    def __str__(self):
        return f'{self.nim}'

class Buku(models.Model):
    idBuku = models.CharField(max_length=30, primary_key=True, null=False, verbose_name="ID Buku")
    namaBuku = models.CharField(max_length=30, null=False, verbose_name="Judul Buku")
    juHal = models.PositiveIntegerField( null=False, verbose_name="Jumlah Halaman")

    class Meta:
        verbose_name_plural ='Buku'
    def __str__(self):
        return f'{self.idBuku}- {self.namaBuku}- Jumlah Halaman: {self.juHal}'
    
class Peminjaman(models.Model):
    idPin = models.AutoField(primary_key=True, null=False, verbose_name="ID Peminjaman")
    idAng = models.ForeignKey(Anggota, on_delete=models.CASCADE, verbose_name="Anggota")
    tglPinjam = models.DateField(verbose_name="Tanggal Pinjam")
    tglKembali = models.DateField(verbose_name="Tanggal Kembali")

    class Meta:
        verbose_name_plural = 'Peminjam'

    def __str__(self):
        return f'{self.idPin} - {self.idAng}'

class DetPin(models.Model):
    idDetPin = models.AutoField(primary_key=True, null=False, verbose_name="ID Detail Peminjaman")
    idPin = models.ForeignKey(Peminjaman, on_delete=models.CASCADE, verbose_name="Peminjaman")
    idBuku = models.ForeignKey(Buku, on_delete=models.CASCADE, verbose_name="Buku")

    class Meta:
        verbose_name_plural = 'DetailPinjaman'

    @property
    def nama_peminjam(self):
        # Mengambil nama anggota peminjam dari model terkait
        return self.idPin.idAng.nama

    def __str__(self):
        # Menampilkan nama peminjam langsung tanpa ID
        return f'{self.nama_peminjam} -{self.idBuku.namaBuku}'

class Kategori(models.Model):
    idKat = models.CharField(max_length=30, primary_key=True, null=False, verbose_name="ID Kategori")
    namaKat = models.CharField(max_length=100, null=False, verbose_name="Nama Kategori")

    class Meta:
        verbose_name_plural = 'NamaKategori'

    def __str__(self):
        return f'{self.idKat}- {self.namaKat}'

class KatBuk(models.Model):
    idKatBuk = models.AutoField(primary_key=True, null=False, verbose_name="ID Kategori Buku")
    idBuku = models.ForeignKey(Buku, on_delete=models.CASCADE, verbose_name="Buku")
    idKat = models.ForeignKey(Kategori, on_delete=models.CASCADE, verbose_name="Kategori")
    jlhBuku = models.PositiveSmallIntegerField (null=False, verbose_name="Jumlah Buku")

    class Meta:
        verbose_name_plural = 'Detail Ketersediaan Buku'

    def __str__(self):
        return f'{self.idKatBuk} - {self.idKat.namaKat}- Ketersediaan : {self.jlhBuku}'