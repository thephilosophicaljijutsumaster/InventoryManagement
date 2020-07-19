# Generated by Django 2.2.12 on 2020-07-12 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('InvManage', '0033_auto_20200712_1231'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invoice',
            new_name='PurchaseInvoice',
        ),
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InvManage.Company')),
                ('shippingaddress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InvManage.ShippingAddress')),
                ('so', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InvManage.SalesOrder')),
            ],
        ),
    ]
