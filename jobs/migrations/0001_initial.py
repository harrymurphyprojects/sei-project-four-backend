# Generated by Django 4.0.1 on 2022-01-26 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('company_image', models.CharField(blank=True, max_length=300)),
                ('location', models.CharField(max_length=30)),
                ('salary', models.PositiveIntegerField(blank=True)),
                ('reference_number', models.PositiveIntegerField(unique=True)),
                ('description', models.TextField(max_length=800)),
                ('date_posted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('contact_email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='applications', to='jobs.job')),
            ],
        ),
    ]
