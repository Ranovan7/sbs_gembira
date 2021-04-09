# Generated by Django 3.1.7 on 2021-04-06 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.EmailField(max_length=255, null=True, verbose_name='email address')),
                ('role', models.IntegerField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Antar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=3, unique=True)),
                ('nama', models.TextField()),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kota', models.TextField(blank=True, null=True)),
                ('telepon', models.CharField(blank=True, max_length=13, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'antar',
            },
        ),
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.TextField()),
                ('expired_date', models.DateTimeField()),
                ('stock', models.IntegerField()),
            ],
            options={
                'db_table': 'barang',
            },
        ),
        migrations.CreateModel(
            name='InfoPajak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('npwp', models.TextField()),
                ('ppn', models.BooleanField(blank=True, null=True)),
                ('pkp', models.TextField(blank=True, null=True)),
                ('nama', models.TextField(blank=True, null=True)),
                ('alamat', models.TextField(blank=True, null=True)),
                ('obj_type', models.TextField(blank=True, null=True)),
                ('obj_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'info_pajak',
            },
        ),
        migrations.CreateModel(
            name='Obat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField()),
                ('jenis', models.TextField()),
            ],
            options={
                'db_table': 'obat',
            },
        ),
        migrations.CreateModel(
            name='Pabrik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.TextField(unique=True)),
                ('nama', models.TextField()),
            ],
            options={
                'db_table': 'pabrik',
            },
        ),
        migrations.CreateModel(
            name='Pelanggan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.TextField(unique=True)),
                ('nama', models.TextField()),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kota', models.TextField(blank=True, null=True)),
                ('telepon', models.CharField(blank=True, max_length=13, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('limits', models.IntegerField(blank=True, null=True)),
                ('toleransi', models.IntegerField(blank=True, null=True)),
                ('diskon', models.FloatField(blank=True, null=True)),
                ('info_pajak', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.infopajak')),
            ],
            options={
                'db_table': 'pelanggan',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.TextField(unique=True)),
                ('nama', models.TextField()),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kota', models.TextField(blank=True, null=True)),
                ('telepon', models.CharField(blank=True, max_length=13, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('info_pajak', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.infopajak')),
            ],
            options={
                'db_table': 'supplier',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode', models.CharField(max_length=3, unique=True)),
                ('nama', models.TextField()),
                ('alamat', models.TextField(blank=True, null=True)),
                ('kota', models.TextField(blank=True, null=True)),
                ('telepon', models.CharField(blank=True, max_length=13, null=True)),
                ('keterangan', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sales',
            },
        ),
        migrations.CreateModel(
            name='PesananOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateTimeField()),
                ('accepted', models.BooleanField()),
                ('pelanggan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.pelanggan')),
                ('sales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.sales')),
            ],
            options={
                'db_table': 'pesanan_out',
            },
        ),
        migrations.CreateModel(
            name='PesananIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl', models.DateTimeField()),
                ('accepted', models.BooleanField()),
                ('pelanggan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.pelanggan')),
                ('sales', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.sales')),
            ],
            options={
                'db_table': 'pesanan_in',
            },
        ),
        migrations.AddField(
            model_name='pelanggan',
            name='sales',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.sales'),
        ),
        migrations.CreateModel(
            name='ItemPesananOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('satuan', models.CharField(blank=True, max_length=10, null=True)),
                ('diskon', models.FloatField(blank=True, null=True)),
                ('barang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.barang')),
                ('pesanan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.pesananout')),
            ],
            options={
                'db_table': 'item_pesanan_out',
            },
        ),
        migrations.CreateModel(
            name='ItemPesananIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(blank=True, null=True)),
                ('satuan', models.CharField(blank=True, max_length=10, null=True)),
                ('diskon', models.FloatField(blank=True, null=True)),
                ('barang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.barang')),
                ('pesanan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.pesananin')),
            ],
            options={
                'db_table': 'item_pesanan_in',
            },
        ),
        migrations.AddField(
            model_name='barang',
            name='obat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.obat'),
        ),
        migrations.AlterUniqueTogether(
            name='barang',
            unique_together={('batch', 'expired_date', 'obat')},
        ),
    ]
