# Generated by Django 4.2 on 2025-03-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Logiapp', '0003_transaction_delete_zip'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('service', models.CharField(choices=[('store', 'Storage'), ('logistics', 'Logistics'), ('cargo', 'Cargo'), ('trucking', 'Trucking'), ('packaging', 'Packaging'), ('warehousing', 'Warehousing')], default='web_dev', max_length=20)),
                ('request_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
