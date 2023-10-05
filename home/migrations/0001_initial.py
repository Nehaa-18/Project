# Generated by Django 4.1.5 on 2023-01-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('htl_name', models.CharField(max_length=100)),
                ('htl_rate', models.BigIntegerField(verbose_name=10000)),
            ],
        ),
    ]