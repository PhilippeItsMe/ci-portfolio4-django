# Generated by Django 4.2.17 on 2024-12-27 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pet_businesses', '0007_remove_pet_businesse_business_pet_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pet_businesse',
            options={'ordering': ['-last_modified']},
        ),
        migrations.AlterModelOptions(
            name='pet_type',
            options={'ordering': ['pet_type']},
        ),
        migrations.AlterModelOptions(
            name='service_type',
            options={'ordering': ['service_type']},
        ),
    ]
