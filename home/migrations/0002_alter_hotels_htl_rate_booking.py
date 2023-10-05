# Generated by Django 4.1.5 on 2023-01-08 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='htl_rate',
            field=models.BigIntegerField(verbose_name=1000),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=255)),
                ('b_phone', models.CharField(max_length=10)),
                ('b_email', models.EmailField(max_length=254)),
                ('hotel_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('hotel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.hotels')),
            ],
        ),
    ]