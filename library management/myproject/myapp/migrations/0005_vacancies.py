# Generated by Django 4.0.3 on 2022-11-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='vacancies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vac', models.BigIntegerField(max_length=1000)),
            ],
        ),
    ]
