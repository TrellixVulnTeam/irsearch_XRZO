# Generated by Django 3.1.1 on 2020-10-02 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_sach', models.CharField(max_length=255)),
                ('ten_tac_gia', models.CharField(max_length=255)),
                ('nam_xuat_ban', models.CharField(max_length=4)),
                ('so_trang', models.IntegerField()),
                ('noi_dung', models.TextField()),
            ],
        ),
    ]
