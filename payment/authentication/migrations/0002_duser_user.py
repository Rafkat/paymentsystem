# Generated by Django 2.2.4 on 2019-11-03 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_auto_20191005_1221'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.Customer'),
        ),
    ]
