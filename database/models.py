# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

role_str = [
    'admin', # 1
    'sales', # 2
    'gudang' # 3
]


class Antar(models.Model):
    kode = models.CharField(unique=True, max_length=3)
    nama = models.TextField()
    alamat = models.TextField(blank=True, null=True)
    kota = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=13, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'antar'


class Barang(models.Model):
    batch = models.TextField()
    expired_date = models.DateTimeField()
    stock = models.IntegerField()
    obat = models.ForeignKey('Obat', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'barang'
        unique_together = (('batch', 'expired_date', 'obat'),)


class InfoPajak(models.Model):
    npwp = models.TextField()
    ppn = models.BooleanField(blank=True, null=True)
    pkp = models.TextField(blank=True, null=True)
    nama = models.TextField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)
    obj_type = models.TextField(blank=True, null=True)
    obj_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'info_pajak'


class ItemPesananIn(models.Model):
    qty = models.IntegerField(blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    diskon = models.FloatField(blank=True, null=True)
    pesanan = models.ForeignKey('PesananIn', models.DO_NOTHING, blank=True, null=True)
    barang = models.ForeignKey(Barang, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'item_pesanan_in'


class ItemPesananOut(models.Model):
    qty = models.IntegerField(blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    diskon = models.FloatField(blank=True, null=True)
    pesanan = models.ForeignKey('PesananOut', models.DO_NOTHING, blank=True, null=True)
    barang = models.ForeignKey(Barang, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'item_pesanan_out'


class Obat(models.Model):
    nama = models.TextField()
    jenis = models.TextField()

    class Meta:
        db_table = 'obat'


class Pabrik(models.Model):
    kode = models.TextField(unique=True)
    nama = models.TextField()

    class Meta:
        db_table = 'pabrik'


class Pelanggan(models.Model):
    kode = models.TextField(unique=True)
    nama = models.TextField()
    alamat = models.TextField(blank=True, null=True)
    kota = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=13, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    limits = models.IntegerField(blank=True, null=True)
    toleransi = models.IntegerField(blank=True, null=True)
    diskon = models.FloatField(blank=True, null=True)
    sales = models.ForeignKey('Sales', models.SET_NULL, blank=True, null=True)
    info_pajak = models.ForeignKey(InfoPajak, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'pelanggan'


class PesananIn(models.Model):
    tgl = models.DateTimeField()
    accepted = models.BooleanField()
    sales = models.ForeignKey('Sales', models.DO_NOTHING, blank=True, null=True)
    pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'pesanan_in'


class PesananOut(models.Model):
    tgl = models.DateTimeField()
    accepted = models.BooleanField()
    sales = models.ForeignKey('Sales', models.DO_NOTHING, blank=True, null=True)
    pelanggan = models.ForeignKey(Pelanggan, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        db_table = 'pesanan_out'


class Sales(models.Model):
    kode = models.CharField(unique=True, max_length=3)
    nama = models.TextField()
    alamat = models.TextField(blank=True, null=True)
    kota = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=13, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    user = models.ForeignKey('Users', models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'sales'


class Supplier(models.Model):
    kode = models.TextField(unique=True)
    nama = models.TextField()
    alamat = models.TextField(blank=True, null=True)
    kota = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=13, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    info_pajak = models.ForeignKey(InfoPajak, models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'supplier'


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
            role=3
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
        )
        user.role = 1
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=30)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True
    )
    role = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return True

    @property
    def is_admin(self):
        return True if self.role == 1 else False

    @property
    def role_tag(self):
        return role_str[self.role - 1]
