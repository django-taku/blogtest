# Generated by Django 3.2.3 on 2021-08-14 06:27

from django.db import migrations, models

# データベースにデータを反映させる
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SampeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
