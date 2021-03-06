# Generated by Django 3.1.1 on 2020-09-11 19:31

import appointment.models.doctor
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=appointment.models.doctor.doctor_image_upload_path)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?\\d(9,15)$')])),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('clinic_name', models.CharField(blank=True, max_length=200, null=True)),
                ('clinic_address', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_one', models.CharField(blank=True, max_length=200, null=True)),
                ('address_line_two', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postal_code', models.CharField(blank=True, max_length=5, null=True)),
                ('pricing', models.CharField(choices=[('F', 'Free'), ('CP', 'CUSTOM PRICE')], default='F', max_length=2)),
                ('services', models.TextField(blank=True, null=True)),
                ('specialization', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Memberships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=200)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('designation', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('MBBS', 'Bachelor of Medicine / Bachelor of Surgery (MBBS, BMBS, MBChB, MBBCh)'), ('MD', 'Doctor of Medicine (MD, Dr.MuD, Dr.Med)'), ('DO', 'Doctor of Osteopathic Medicine (DO)'), ('MDRes', 'Doctor of Medicine by research (MD(Res), DM)'), ('PhD', 'Doctor of Philosophy (PhD, DPhil)'), ('MCM', 'Master of Clinical Medicine (MCM)'), ('MMSc', 'Master of Medical Science (MMSc, MMedSc)'), ('MM', 'Master of Medicine (MM, MMed)'), ('MPhil', 'Master of Philosophy (MPhil)'), ('MSurg', 'Master of Surgery (MS, MSurg, MChir, MCh, ChM, CM)'), ('MSc', 'Master of Science in Medicine or Surgery (MSc)'), ('DCM', 'Doctor of Clinical Medicine (DCM)'), ('DClinSurg', 'Doctor of Clinical Surgery (DClinSurg)'), ('DMSc', 'Doctor of Medical Science (DMSc, DMedSc)'), ('DS', 'Doctor of Surgery (DS, DSurg)')], max_length=15)),
                ('college', models.CharField(max_length=200)),
                ('year_of_completion', models.PositiveIntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='ClinicImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=appointment.models.doctor.clinic_image_file_path)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
            ],
        ),
    ]
