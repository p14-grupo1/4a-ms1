# Generated by Django 3.2.7 on 2021-11-19 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('H', 'Hotel'), ('M', 'Motel'), ('R', 'Resort'), ('B', 'Boutique'), ('G', 'Gastronomic')], default='H', max_length=2)),
                ('qualification', models.PositiveSmallIntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='turismo.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Turista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('name', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TuristaHotelRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turismo.hotel')),
                ('tourist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='turismo.turista')),
            ],
        ),
    ]
