# Generated by Django 5.1.6 on 2025-02-24 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.PositiveBigIntegerField()),
                ('rating', models.PositiveIntegerField(default=5)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]
