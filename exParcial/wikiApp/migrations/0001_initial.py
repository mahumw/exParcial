# Generated by Django 5.1 on 2024-08-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='temaWiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=128, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=512, null=True)),
            ],
        ),
    ]
