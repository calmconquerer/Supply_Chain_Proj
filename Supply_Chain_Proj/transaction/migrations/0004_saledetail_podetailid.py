# Generated by Django 2.2 on 2019-10-28 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_saledetail_po_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledetail',
            name='podetailid',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]