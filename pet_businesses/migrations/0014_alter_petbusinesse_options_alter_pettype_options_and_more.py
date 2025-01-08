# Generated by Django 4.2.17 on 2025-01-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_businesses', '0013_rename_pet_businesse_petbusinesse_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='petbusinesse',
            options={'ordering': ['-last_modified'], 'verbose_name': 'Pet Business', 'verbose_name_plural': 'Pet Businesses'},
        ),
        migrations.AlterModelOptions(
            name='pettype',
            options={'ordering': ['pet_type'], 'verbose_name': 'Pet Type', 'verbose_name_plural': 'Pet Types'},
        ),
        migrations.AlterModelOptions(
            name='servicetype',
            options={'ordering': ['service_type'], 'verbose_name': 'Service Type', 'verbose_name_plural': 'Service Types'},
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='petbusinesse',
            name='business_pet_type',
            field=models.ManyToManyField(related_name='business_pet_types', to='pet_businesses.pettype'),
        ),
        migrations.AlterField(
            model_name='petbusinesse',
            name='business_service_type',
            field=models.ManyToManyField(related_name='business_service_types', to='pet_businesses.servicetype'),
        ),
        migrations.AddConstraint(
            model_name='like',
            constraint=models.UniqueConstraint(fields=('pet_business', 'author'), name='unique_like'),
        ),
    ]
