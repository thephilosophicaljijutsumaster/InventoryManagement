# Generated by Django 2.2.12 on 2020-05-02 10:28

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0029_auto_20200502_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='FilterColumn',
            name='state',
            field=models.ForeignKey('ProductFilterState',on_delete=models.CASCADE)
        ),
    ]
