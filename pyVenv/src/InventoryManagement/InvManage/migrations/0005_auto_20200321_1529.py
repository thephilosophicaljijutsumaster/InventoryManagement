# Generated by Django 3.0.3 on 2020-03-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0004_auto_20200320_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='identifier',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]