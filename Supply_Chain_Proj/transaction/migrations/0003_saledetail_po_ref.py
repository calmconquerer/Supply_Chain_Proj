# Generated by Django 2.2 on 2019-10-28 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_chartofaccount_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='saledetail',
            name='po_ref',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
