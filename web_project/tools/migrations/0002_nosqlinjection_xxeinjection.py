# Generated by Django 4.1.5 on 2023-01-02 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='nosqlinjection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='xxeinjection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload', models.CharField(max_length=255)),
            ],
        ),
    ]
