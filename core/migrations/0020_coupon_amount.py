# Generated by Django 2.2.8 on 2020-06-09 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20200609_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(default=15),
            preserve_default=False,
        ),
    ]
