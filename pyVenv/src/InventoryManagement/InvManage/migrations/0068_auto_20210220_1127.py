# Generated by Django 2.2.12 on 2021-02-20 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0067_auto_20210209_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='date',
            field=models.DateTimeField(blank=True, default='20 February, 2021', null=True),
        ),
    ]