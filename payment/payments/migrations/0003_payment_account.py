# Generated by Django 2.2.4 on 2019-09-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20190917_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='account',
            field=models.DecimalField(decimal_places=10, max_digits=19, null=True),
        ),
    ]
