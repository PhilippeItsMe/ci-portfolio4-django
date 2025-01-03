# Generated by Django 4.2.17 on 2024-12-27 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pet_businesses', '0003_alter_pet_businesses_contact_mobile_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pet_businesses',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='Service_Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('pet_business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_service_types', to='pet_businesses.pet_businesses')),
            ],
        ),
        migrations.CreateModel(
            name='Pet_Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(max_length=150)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('pet_business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='business_pet_types', to='pet_businesses.pet_businesses')),
            ],
        ),
    ]
