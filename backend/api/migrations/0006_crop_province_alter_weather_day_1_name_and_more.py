# Generated by Django 5.1 on 2024-08-29 06:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_weather_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_eng', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'crop',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'province',
            },
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_1_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_2_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_3_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_4_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_5_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_6_name',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day_7_name',
            field=models.CharField(max_length=10),
        ),
        migrations.CreateModel(
            name='CropCoefficient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jan', models.FloatField(blank=True, null=True)),
                ('feb', models.FloatField(blank=True, null=True)),
                ('mar', models.FloatField(blank=True, null=True)),
                ('apr', models.FloatField(blank=True, null=True)),
                ('may', models.FloatField(blank=True, null=True)),
                ('jun', models.FloatField(blank=True, null=True)),
                ('jul', models.FloatField(blank=True, null=True)),
                ('aug', models.FloatField(blank=True, null=True)),
                ('sep', models.FloatField(blank=True, null=True)),
                ('oct', models.FloatField(blank=True, null=True)),
                ('nov', models.FloatField(blank=True, null=True)),
                ('dec', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.crop')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.province')),
            ],
            options={
                'db_table': 'crop_coefficient',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('name_urdu', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('province', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.province')),
            ],
            options={
                'db_table': 'region',
            },
        ),
        migrations.CreateModel(
            name='DistrictCrop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.crop')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.region')),
            ],
            options={
                'db_table': 'district_crop',
            },
        ),
    ]
