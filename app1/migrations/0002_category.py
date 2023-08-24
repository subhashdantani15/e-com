# Generated by Django 4.1.2 on 2023-08-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='categoryimg')),
            ],
        ),
    ]
