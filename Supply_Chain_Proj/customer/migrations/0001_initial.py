# Generated by Django 2.2.5 on 2019-09-27 18:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transaction', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RfqCustomerHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfq_no', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('attn', models.CharField(max_length=100)),
                ('follow_up', models.DateField(blank=True)),
                ('show_notification', models.BooleanField(default=True)),
                ('footer_remarks', models.TextField()),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transaction.ChartOfAccount')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Branch')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Company_info')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RfqCustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Add_products')),
                ('rfq_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.RfqCustomerHeader')),
            ],
        ),
        migrations.CreateModel(
            name='QuotationHeaderCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quotation_no', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('attn', models.CharField(max_length=100)),
                ('prc_basis', models.CharField(max_length=100)),
                ('leadtime', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('yrref', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('exchange_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('follow_up', models.DateField(blank=True)),
                ('show_notification', models.BooleanField(default=True)),
                ('footer_remarks', models.TextField()),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transaction.ChartOfAccount')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Branch')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Company_info')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuotationDetailCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('remarks', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Add_products')),
                ('quotation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.QuotationHeaderCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='PoHeaderCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_no', models.CharField(max_length=100, unique=True)),
                ('date', models.DateField(default=datetime.date.today)),
                ('attn', models.CharField(max_length=100)),
                ('prc_basis', models.CharField(max_length=100)),
                ('po_client', models.CharField(max_length=100)),
                ('leadtime', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('payment', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('currency', models.CharField(max_length=100)),
                ('exchange_rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('follow_up', models.DateField(blank=True)),
                ('show_notification', models.BooleanField(default=True)),
                ('footer_remarks', models.TextField()),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transaction.ChartOfAccount')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Branch')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Company_info')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PoDetailCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('remarks', models.CharField(max_length=100)),
                ('quotation_no', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Add_products')),
                ('po_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.PoHeaderCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='DcHeaderCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dc_no', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('footer_remarks', models.TextField()),
                ('show_notification', models.BooleanField(default=True)),
                ('follow_up', models.DateField(blank=True)),
                ('cartage_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('po_no', models.CharField(max_length=100)),
                ('account_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transaction.ChartOfAccount')),
                ('branch_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Branch')),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Company_info')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DcDetailCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('accepted_quantity', models.IntegerField()),
                ('returned_quantity', models.IntegerField()),
                ('po_no', models.CharField(max_length=100)),
                ('dc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.DcHeaderCustomer')),
                ('item_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Add_products')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('company_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.Company_info')),
            ],
        ),
    ]
