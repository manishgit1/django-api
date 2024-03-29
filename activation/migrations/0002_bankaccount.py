# Generated by Django 5.0.2 on 2024-03-03 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=25)),
                ('account_number', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
