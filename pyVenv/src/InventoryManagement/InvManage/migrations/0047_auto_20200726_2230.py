# Generated by Django 2.2.12 on 2020-07-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0046_auto_20200726_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventtype',
            name='label',
            field=models.CharField(default='old', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='objectmodel',
            name='label',
            field=models.CharField(default='old', max_length=30),
            preserve_default=False,
        ),
    ]