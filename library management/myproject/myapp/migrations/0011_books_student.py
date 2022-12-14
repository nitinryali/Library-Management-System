# Generated by Django 4.0.3 on 2022-11-18 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_delete_image_delete_image1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('dept', models.CharField(max_length=10)),
                ('availability', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.CharField(max_length=10)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('b1', models.CharField(max_length=50)),
                ('due1', models.DateField()),
                ('b2', models.CharField(max_length=50)),
                ('due2', models.DateField()),
                ('b3', models.CharField(max_length=50)),
                ('due3', models.DateField()),
            ],
        ),
    ]
