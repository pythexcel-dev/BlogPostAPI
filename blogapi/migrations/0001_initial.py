# Generated by Django 4.1.5 on 2023-02-08 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
