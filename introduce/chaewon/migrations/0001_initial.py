# Generated by Django 3.2.3 on 2021-07-30 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Porfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]