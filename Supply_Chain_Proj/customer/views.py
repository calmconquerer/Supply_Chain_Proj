from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, request
from .models import (RfqCustomerHeader, RfqCustomerDetail,
                     QuotationHeaderCustomer, QuotationDetailCustomer,
                     PoHeaderCustomer, PoDetailCustomer,
                     DcHeaderCustomer, DcDetailCustomer)
from user.models import Company_info, Branch
from inventory.models import Add_products
from transaction.models import ChartOfAccount, SaleDetail
from django.core import serializers
from django.forms.models import model_to_dict
import json
import datetime
from supplier.utils import render_to_pdf
from django.template.loader import get_template
from django.db import connection
from django.db.models import Q
from django.core import mail
from django.core.mail import EmailMessage
from user.models import UserRoles
from django.contrib.auth.decorators import user_passes_test, login_required
from supplier.views import customer_roles, supplier_roles, transaction_roles, inventory_roles, report_roles
from django.contrib import messages
from django.db import IntegrityError


def allow_rfq_display(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=11)
    display = Q(display=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, display)
    if allow_role:
        return True
    else:
        return False


def allow_rfq_add(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=11)
    add = Q(add=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, add)
    if allow_role:
        return allow_role
    else:
        return allow_role


def bool_allow_rfq_add(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=11)
    add = Q(add=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, add)
    if allow_role:
        return True
    else:
        return False


def allow_rfq_edit(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=11)
    edit = Q(edit=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, edit)
    if allow_role:
        return True
    else:
        return False


def allow_rfq_delete(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=11)
    delete = Q(delete=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, delete)
    if allow_role:
        return True
    else:
        return False


def allow_quotation_display(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=12)
    display = Q(display=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, display)
    if allow_role:
        return True
    else:
        return False


def allow_quotation_add(request):
    user_id = Q(user_id=request.user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=12)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form)
    if allow_role:
        return allow_role
    else:
        return allow_role


def bool_allow_quotation_add(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=12)
    add = Q(add=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, add)
    if allow_role:
        return True
    else:
        return False


def allow_quotation_edit(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=12)
    edit = Q(edit=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, edit)
    if allow_role:
        return True
    else:
        return False


def allow_quotation_delete(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=12)
    delete = Q(delete=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, delete)
    if allow_role:
        return True
    else:
        return False


def allow_quotation_print(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=12)
    r_print = Q(r_print=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, r_print)
    if allow_role:
        return True
    else:
        return False


def allow_purchase_order_display(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=13)
    display = Q(display=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, display)
    if allow_role:
        return True
    else:
        return False


def allow_purchase_order_add(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=13)
    add = Q(add=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, add)
    if allow_role:
        return True
    else:
        return False


def allow_purchase_order_edit(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=13)
    edit = Q(edit=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, edit)
    if allow_role:
        return True
    else:
        return False


def allow_purchase_order_delete(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=13)
    delete = Q(delete=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, delete)
    if allow_role:
        return True
    else:
        return False


def allow_purchase_order_print(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=13)
    r_print = Q(r_print=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, r_print)
    if allow_role:
        return True
    else:
        return False


def allow_delivery_challan_display(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=14)
    display = Q(display=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, display)
    if allow_role:
        return True
    else:
        return False


def allow_delivery_challan_add(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=14)
    add = Q(add=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, add)
    if allow_role:
        return True
    else:
        return False


def allow_delivery_challan_edit(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=14)
    edit = Q(edit=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, edit)
    if allow_role:
        return True
    else:
        return False


def allow_delivery_challan_delete(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=14)
    delete = Q(delete=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, delete)
    if allow_role:
        return True
    else:
        return False


def allow_delivery_challan_print(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=14)
    r_print = Q(r_print=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, r_print)
    if allow_role:
        return True
    else:
        return False


def allow_mrn_display(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=15)
    display = Q(display=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, display)
    if allow_role:
        return True
    else:
        return False


def allow_mrn_edit(user):
    user_id = Q(user_id=user.id)
    form_id = Q(form_id=1)
    child_form = Q(child_form=15)
    edit = Q(edit=1)
    allow_role = UserRoles.objects.filter(user_id, form_id, child_form, edit)
    if allow_role:
        return True
    else:
        return False


def rfq_roles(user):
    userid = str(user.id)
    user_id = Q(user_id=userid)
    child_form = Q(child_form=11)
    rfq_roles = UserRoles.objects.filter(user_id, child_form).first()
    return rfq_roles


def quotation_roles(user):
    userid = str(user.id)
    user_id = Q(user_id=userid)
    child_form = Q(child_form=12)
    quotation_roles = UserRoles.objects.filter(user_id, child_form).first()
    return quotation_roles


def purchase_order_roles(user):
    userid = str(user.id)
    user_id = Q(user_id=userid)
    child_form = Q(child_form=13)
    po_roles = UserRoles.objects.filter(user_id, child_form).first()
    return po_roles


def delivery_challan_roles(user):
    userid = str(user.id)
    user_id = Q(user_id=userid)
    child_form = Q(child_form=14)
    dc_roles = UserRoles.objects.filter(user_id, child_form).first()
    return dc_roles


def mrn_roles(user):
    userid = str(user.id)
    user_id = Q(user_id=userid)
    child_form = Q(child_form=15)
    mrn_roles = UserRoles.objects.filter(user_id, child_form).first()
    return mrn_roles


@login_required
@user_passes_test(allow_rfq_display)
def rfq_customer(request):
    company = request.session['company']
    branch = request.session['branch']
    branch = Branch.objects.get(branch_id=branch)
    company = Company_info.objects.get(id=company)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    permission = rfq_roles(request.user)
    company = Q(company_id=company, branch_id=branch)
    all_rfq = RfqCustomerHeader.objects.filter(company).all()
    return render(request, 'customer/rfq_customer.html', {'all_rfq': all_rfq,
                                                          'permission': permission,
                                                          'allow_customer_roles': allow_customer_roles,
                                                          'allow_supplier_roles': allow_supplier_roles,
                                                          'allow_transaction_roles': allow_transaction_roles,
                                                          'allow_inventory_roles': allow_inventory_roles,
                                                          'allow_report_roles': report_roles(request.user),
                                                          'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(bool_allow_rfq_add)
def new_rfq_customer(request):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    get_last_rfq_no = RfqCustomerHeader.objects.last()
    all_item_code = Add_products.objects.all()
    customer = Q(account_id="100")
    supplier = Q(account_id="200")
    all_accounts = ChartOfAccount.objects.filter(customer | supplier).all()
    if get_last_rfq_no:
        get_last_rfq_no = get_last_rfq_no.rfq_no
        get_last_rfq_no = get_last_rfq_no[-3:]
        num = int(get_last_rfq_no)
        num = num + 1
        get_last_rfq_no = 'RFQ/CU/' + str(num)
    else:
        get_last_rfq_no = 'RFQ/CU/101'
    item_code = request.POST.get('item_code', False)
    if item_code:
        data = Add_products.objects.filter(product_code=item_code)
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    if request.method == 'POST':
        customer = request.POST.get('customer', False)
        attn = request.POST.get('attn', False)
        follow_up = request.POST.get('follow_up', False)
        footer_remarks = request.POST.get('footer_remarks', False)
        items = json.loads(request.POST.get('items'))
        account_id = ChartOfAccount.objects.get(account_title=customer)
        company = request.session['company']
        branch = request.session['branch']
        branch = Branch.objects.get(branch_id=branch)
        company = Company_info.objects.get(id=company)
        date = datetime.date.today()
        if follow_up:
            follow_up = follow_up
        else:
            follow_up = '2010-06-22'
        rfq_header = RfqCustomerHeader(rfq_no=get_last_rfq_no, date=date, attn=attn, follow_up=follow_up,
                                       footer_remarks=footer_remarks, account_id=account_id, user_id=request.user,
                                       company_id=company, branch_id=branch)
        rfq_header.save()
        header_id = RfqCustomerHeader.objects.get(rfq_no=get_last_rfq_no)
        for value in items:
            item_id = Add_products.objects.get(id=value["id"])
            rfq_detail = RfqCustomerDetail(item_id=item_id, quantity=value["quantity"], rfq_id=header_id)
            rfq_detail.save()
        return JsonResponse({"result": "success"})
    return render(request, 'customer/new_rfq_customer.html',
                  {'get_last_rfq_no': get_last_rfq_no, 'all_item_code': all_item_code, 'all_accounts': all_accounts,
                   'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                   'allow_transaction_roles': allow_transaction_roles, 'allow_inventory_roles': allow_inventory_roles,
                   'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_rfq_edit)
def edit_rfq_customer(request, pk):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    rfq_header = RfqCustomerHeader.objects.filter(company, id=pk).first()
    rfq_detail = RfqCustomerDetail.objects.filter(rfq_id=rfq_header.id).all()
    all_accounts = ChartOfAccount.objects.all()
    all_item_code = list(Add_products.objects.values('product_code'))
    try:
        item_code = request.POST.get('item_code', False)
        if item_code:
            item_id = Add_products.objects.get(product_code=item_code)
            data = Add_products.objects.filter(id=item_id.id).first()
            print("here", data)
            item_code_exist = RfqCustomerDetail.objects.filter(item_id=data.id, rfq_id=pk).first()
            if item_code_exist:
                return HttpResponse(json.dumps({'message': "Item Already Exist"}))
            row = serializers.serialize('json', data)
            return JsonResponse({'row': row})
        if request.method == 'POST':
            rfq_detail.delete()
            edit_rfq_customer = request.POST.get('customer', False)
            edit_rfq_attn = request.POST.get('edit_rfq_attn', False)
            edit_rfq_follow_up = request.POST.get('edit_rfq_follow_up', False)
            footer_remarks = request.POST.get('footer_remarks')
            account_id = ChartOfAccount.objects.get(account_title=edit_rfq_customer)

            if edit_rfq_follow_up:
                edit_rfq_follow_up = edit_rfq_follow_up
            else:
                edit_rfq_follow_up = '2010-06-22'

            rfq_header.account_id = account_id
            rfq_header.attn = edit_rfq_attn
            rfq_header.follow_up = edit_rfq_follow_up
            rfq_header.footer_remarks = footer_remarks
            rfq_header.save()
            header_id = RfqCustomerHeader.objects.get(id=pk)
            items = json.loads(request.POST.get('items'))
            for value in items:
                item_id = Add_products.objects.get(id=value["id"])
                print(item_id)
                rfq_detail_update = RfqCustomerDetail(item_id=item_id, quantity=value["quantity"], rfq_id=header_id)
                rfq_detail_update.save()
            return JsonResponse({"result": "success"})
    except IntegrityError:
        print("Data Already Exist")
    return render(request, 'customer/edit_rfq_customer.html',
                  {'rfq_header': rfq_header, 'pk': pk, 'rfq_detail': rfq_detail, 'all_item_code': all_item_code,
                   'all_accounts': all_accounts, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'allow_inventory_roles': allow_inventory_roles, 'allow_report_roles': report_roles(request.user),
                   'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_rfq_delete)
def delete_rfq_customer(request, pk):
    RfqCustomerDetail.objects.filter(rfq_id_id=pk).all().delete()
    RfqCustomerHeader.objects.filter(id=pk).delete()
    messages.add_message(request, messages.SUCCESS, " Customer RFQ Deleted")
    return redirect('rfq-customer')


@user_passes_test(allow_quotation_display)
def quotation_customer(request):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    permission = quotation_roles(request.user)
    all_quotation = QuotationHeaderCustomer.objects.filter(company).all()
    allow_inventory_roles = inventory_roles(request.user)
    permission = quotation_roles(request.user)
    all_quotation = QuotationHeaderCustomer.objects.all()
    return render(request, 'customer/quotation_customer.html',
                  {'all_quotation': all_quotation, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'permission': permission, 'allow_inventory_roles': allow_inventory_roles,
                   'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(bool_allow_quotation_add)
def new_quotation_customer(request):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    all_item_code = Add_products.objects.all()
    get_last_quotation_no = QuotationHeaderCustomer.objects.last()
    all_accounts = ChartOfAccount.objects.all()
    if get_last_quotation_no:
        get_last_quotation_no = get_last_quotation_no.quotation_no
        get_last_quotation_no = get_last_quotation_no[-3:]
        num = int(get_last_quotation_no)
        num = num + 1
        get_last_quotation_no = 'QU/CU/' + str(num)
    else:
        get_last_quotation_no = 'QU/CU/101'
    item_code_quotation = request.POST.get('item_code_quotation', False)
    if item_code_quotation:
        data = Add_products.objects.filter(product_code=item_code_quotation)
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    if request.method == 'POST':
        company = request.session['company']
        company = Company_info.objects.get(id=company)
        branch = request.session['branch']
        branch = Branch.objects.get(branch_id=branch)
        customer = request.POST.get('customer', False)
        attn = request.POST.get('attn', False)
        prcbasis = request.POST.get('prcbasis', False)
        leadtime = request.POST.get('leadtime', False)
        validity = request.POST.get('validity', False)
        payment = request.POST.get('payment', False)
        yrref = request.POST.get('yrref', False)
        remarks = request.POST.get('remarks', False)
        currency = request.POST.get('currency', False)
        exchange_rate = request.POST.get('exchange_rate', False)
        follow_up = request.POST.get('follow_up', False)
        footer_remarks = request.POST.get('footer_remarks', False)
        account_id = ChartOfAccount.objects.get(account_title=customer)
        date = datetime.date.today()
        if follow_up:
            follow_up = follow_up
        else:
            follow_up = '2010-06-22'
        quotation_header = QuotationHeaderCustomer(quotation_no=get_last_quotation_no, date=date, attn=attn,
                                                   prc_basis=prcbasis,
                                                   leadtime=leadtime, validity=validity, payment=payment, yrref=yrref,
                                                   remarks=remarks, currency=currency,
                                                   exchange_rate=exchange_rate, follow_up=follow_up,
                                                   show_notification=True, footer_remarks=footer_remarks,
                                                   account_id=account_id, company_id=company, user_id=request.user, branch_id=branch)
        quotation_header.save()
        items = json.loads(request.POST.get('items'))
        header_id = QuotationHeaderCustomer.objects.get(quotation_no=get_last_quotation_no)
        for value in items:
            item_id = Add_products.objects.get(id=value["id"])
            quotation_detail = QuotationDetailCustomer(item_id=item_id, quantity=value["quantity"],
                                                       unit_price=value["unit_price"], remarks=value["remarks"],
                                                       quotation_id=header_id)
            quotation_detail.save()
        last_id = QuotationHeaderCustomer.objects.last()
        last_id = last_id.id
        return JsonResponse({'result': 'success', "last_id": last_id})
    return render(request, 'customer/new_quotation_customer.html',
                  {'all_item_code': all_item_code, 'get_last_quotation_no': get_last_quotation_no,
                   'all_accounts': all_accounts, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'allow_inventory_roles': allow_inventory_roles, 'allow_report_roles': report_roles(request.user),
                   'is_superuser': request.user.is_superuser})


@login_required
def send_email(request, pk, id):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    account_id = ChartOfAccount.objects.get(id=id)
    msg = EmailMessage('Quotation', 'This is Quotation for Valve', 'ah.awan33@gmail.com', [account_id.email_address])
    msg.attach_file('/Downloads/Quotation_Customer_QU_CU_150.pdf')
    msg.send()
    return redirect('new-quotation-customer')


@login_required
@user_passes_test(allow_quotation_edit)
def edit_quotation_customer(request, pk):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)

    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)

    quotation_header = QuotationHeaderCustomer.objects.filter(company, id=pk).first()
    quotation_detail = QuotationDetailCustomer.objects.filter(quotation_id=quotation_header.id).all()
    all_item_code = list(Add_products.objects.values('product_code'))
    all_accounts = ChartOfAccount.objects.all()
    item_code = request.POST.get('item_code', False)
    if item_code:
        item_id = Add_products.objects.get(product_code=item_code)
        item_code_exist = QuotationDetailCustomer.objects.filter(item_id=item_id, quotation_id=pk).first()
        data = Add_products.objects.filter(id=item_id.id)
        if item_code_exist:
            return HttpResponse(json.dumps({'message': "Item Already Exist"}))
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    if request.method == 'POST':
        quotation_detail.delete()
        edit_quotation = request.POST.get('customer', False)
        edit_quotation_attn = request.POST.get('attn', False)
        edit_quotation_prcbasis = request.POST.get('prcbasis', False)
        edit_quotation_yrref = request.POST.get('yrref', False)
        edit_quotation_leadtime = request.POST.get('leadtime', False)
        edit_quotation_validity = request.POST.get('validity', False)
        edit_quotation_payment = request.POST.get('payment', False)
        edit_quotation_remarks = request.POST.get('remarks', False)
        edit_quotation_currency_rate = request.POST.get('currency', False)
        edit_quotation_exchange_rate = request.POST.get('exchange_rate', False)
        edit_quotation_follow_up = request.POST.get('follow_up', False)
        footer_remarks = request.POST.get('footer_remarks', False)

        if edit_quotation_follow_up:
            edit_quotation_follow_up = edit_quotation_follow_up
        else:
            edit_quotation_follow_up = '2010-06-22'
        account_id = ChartOfAccount.objects.get(account_title=edit_quotation)

        quotation_header.attn = edit_quotation_attn
        quotation_header.prc_basis = edit_quotation_prcbasis
        quotation_header.yrref = edit_quotation_yrref
        quotation_header.leadtime = edit_quotation_leadtime
        quotation_header.validity = edit_quotation_validity
        quotation_header.payment = edit_quotation_payment
        quotation_header.remarks = edit_quotation_remarks
        quotation_header.currency = edit_quotation_currency_rate
        quotation_header.exchange_rate = edit_quotation_exchange_rate
        quotation_header.account_id = account_id
        quotation_header.follow_up = edit_quotation_follow_up
        quotation_header.footer_remarks = footer_remarks

        quotation_header.save()

        header_id = QuotationHeaderCustomer.objects.get(id=pk)
        items = json.loads(request.POST.get('items'))
        print(items)
        for value in items:
            item_id = Add_products.objects.get(id=value['id'])
            print(value['unit_price'])
            quotation_detail_update = QuotationDetailCustomer(item_id=item_id, quantity=value["quantity"],
                                                              unit_price=value["unit_price"], remarks=value["remarks"],
                                                              quotation_id=header_id)
            quotation_detail_update.save()
        return JsonResponse({"result": "success"})
    return render(request, 'customer/edit_quotation_customer.html',
                  {'quotation_header': quotation_header, 'pk': pk, 'quotation_detail': quotation_detail,
                   'all_item_code': all_item_code, 'all_accounts': all_accounts,
                   'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                   'allow_transaction_roles': allow_transaction_roles, 'allow_inventory_roles': allow_inventory_roles,
                   'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_quotation_print)
def print_quotation_customer(request, pk):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)

    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)

    lines = 0
    total_amount = 0
    company_info = Company_info.objects.filter(id=1)
    image = Company_info.objects.filter(id=1).first()
    header = QuotationHeaderCustomer.objects.filter(company, id=pk).first()
    detail = QuotationDetailCustomer.objects.filter(quotation_id=header.id).all()
    for value in detail:
        amount = float(value.unit_price * value.quantity)
        total_amount = total_amount + amount
    pdf = render_to_pdf('customer/quotation_customer_pdf.html',
                        {'company_info': company_info, 'image': image, 'header': header, 'detail': detail,
                         'total_amount': total_amount, 'allow_customer_roles': allow_customer_roles,
                         'allow_supplier_roles': allow_supplier_roles,
                         'allow_transaction_roles': allow_transaction_roles,
                         'allow_inventory_roles': allow_inventory_roles,
                         'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Quotation_Customer_%s.pdf" % (header.quotation_no)
        content = "inline; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


@login_required
@user_passes_test(allow_quotation_delete)
def delete_quotation_customer(request, pk):
    QuotationDetailCustomer.objects.filter(quotation_id_id=pk).all().delete()
    QuotationHeaderCustomer.objects.filter(id=pk).delete()
    messages.add_message(request, messages.SUCCESS, " Customer Quotation Deleted")
    return redirect('quotation-customer')


@login_required
@user_passes_test(allow_purchase_order_display)
def purchase_order_customer(request):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    permission = purchase_order_roles(request.user)

    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    all_po = PoHeaderCustomer.objects.all()
    return render(request, 'customer/purchase_order_customer.html',
                  {'all_po': all_po, 'permission': permission, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'allow_inventory_roles': allow_inventory_roles, 'allow_report_roles': report_roles(request.user),
                   'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_purchase_order_add)
def new_purchase_order_customer(request):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    branch = request.session['branch']
    branch = Branch.objects.get(branch_id=branch)
    get_last_po_no = PoHeaderCustomer.objects.last()
    all_item_code = Add_products.objects.all()
    customer = Q(account_id="100")
    supplier = Q(account_id="200")
    all_accounts = ChartOfAccount.objects.filter(customer | supplier).all()
    if get_last_po_no:
        get_last_po_no = get_last_po_no.po_no
        get_last_po_no = get_last_po_no[-3:]
        num = int(get_last_po_no)
        num = num + 1
        get_last_po_no = 'PO/CU/' + str(num)
    else:
        get_last_po_no = 'PO/CU/101'
    item_code_po = request.POST.get('item_code_po', False)
    if item_code_po:
        data = Add_products.objects.filter(product_code=item_code_po)
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    if request.method == 'POST':
        customer = request.POST.get('customer', False)
        attn = request.POST.get('attn', False)
        prcbasis = request.POST.get('prcbasis', False)
        po_client = request.POST.get('po_client', False)
        leadtime = request.POST.get('leadtime', False)
        validity = request.POST.get('validity', False)
        payment = request.POST.get('payment', False)
        remarks = request.POST.get('remarks', False)
        currency = request.POST.get('currency', False)
        exchange_rate = request.POST.get('exchange_rate', False)
        follow_up = request.POST.get('follow_up', False)
        footer_remarks = request.POST.get('footer_remarks', False)
        account_id = ChartOfAccount.objects.get(account_title=customer)

        date = datetime.date.today()
        if follow_up:
            follow_up = follow_up
        else:
            follow_up = '2010-06-22'
        company = request.session['company']
        company = Company_info.objects.get(id=company)
        po_header = PoHeaderCustomer(po_no=get_last_po_no, date=date, attn=attn, prc_basis=prcbasis,
                                     po_client=po_client,
                                     leadtime=leadtime, validity=validity, payment=payment, remarks=remarks,
                                     currency=currency,
                                     exchange_rate=exchange_rate, follow_up=follow_up, show_notification=True,
                                     footer_remarks=footer_remarks, account_id=account_id, user_id=request.user,
                                     company_id=company,branch_id = branch)
        po_header.save()
        items = json.loads(request.POST.get('items'))
        header_id = PoHeaderCustomer.objects.get(po_no=get_last_po_no)
        for value in items:
            item_id = Add_products.objects.get(id=value["id"])
            po_detail = PoDetailCustomer(item_id=item_id, quantity=value["quantity"], unit_price=value["unit_price"],
                                         remarks=value["remarks"], quotation_no="to be define", po_id=header_id)
            po_detail.save()
        return JsonResponse({'result': 'success'})
    return render(request, 'customer/new_purchase_order_customer.html',
                  {'get_last_po_no': get_last_po_no, 'all_item_code': all_item_code, 'all_accounts': all_accounts,
                   'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                   'allow_transaction_roles': allow_transaction_roles, 'allow_inventory_roles': allow_inventory_roles,
                   'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_purchase_order_edit)
def edit_purchase_order_customer(request, pk):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    po_header = PoHeaderCustomer.objects.filter(company, id=pk).first()
    po_detail = PoDetailCustomer.objects.filter(po_id=po_header.id).all()
    all_item_code = list(Add_products.objects.values('product_code'))
    customer = Q(account_id="100")
    supplier = Q(account_id="200")
    all_accounts = ChartOfAccount.objects.filter(customer | supplier).all()
    item_code = request.POST.get('item_code', False)
    if item_code:
        item_id = Add_products.objects.get(product_code=item_code)
        data = Add_products.objects.filter(id=item_id.id)
        item_code_exist = PoDetailCustomer.objects.filter(item_id=item_id, po_id=pk).first()
        if item_code_exist:
            return HttpResponse(json.dumps({'message': "Item Already Exist"}))
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    if request.method == 'POST':
        po_detail.delete()

        edit_po_customer = request.POST.get('customer', False)
        edit_po_attn = request.POST.get('attn', False)
        edit_po_prcbasis = request.POST.get('prcbasis', False)
        edit_po_client = request.POST.get('po_client', False)
        edit_po_leadtime = request.POST.get('leadtime', False)
        edit_po_validity = request.POST.get('validity', False)
        edit_po_payment = request.POST.get('payment', False)
        edit_po_remarks = request.POST.get('remarks', False)
        edit_po_currency_rate = request.POST.get('currency', False)
        edit_po_exchange_rate = request.POST.get('exchange_rate', False)
        edit_po_follow_up = request.POST.get('follow_up', False)
        footer_remarks = request.POST.get('footer_remarks', False)

        account_id = ChartOfAccount.objects.get(account_title=edit_po_customer)

        if edit_po_follow_up:
            edit_po_follow_up = edit_po_follow_up
        else:
            edit_po_follow_up = '2010-06-22'

        po_header.attn = edit_po_attn
        po_header.prc_basis = edit_po_prcbasis
        po_header.po_client = edit_po_client
        po_header.leadtime = edit_po_leadtime
        po_header.validity = edit_po_validity
        po_header.payment = edit_po_payment
        po_header.remarks = edit_po_remarks
        po_header.currency = edit_po_currency_rate
        po_header.exchange_rate = edit_po_exchange_rate
        po_header.account_id = account_id
        po_header.follow_up = edit_po_follow_up
        po_header.footer_remarks = footer_remarks

        po_header.save()

        header_id = PoHeaderCustomer.objects.get(id=pk)
        items = json.loads(request.POST.get('items'))
        print(items)
        for value in items:
            item_id = Add_products.objects.get(id=value["id"])
            po_detail_update = PoDetailCustomer(item_id=item_id, quantity=value["quantity"],
                                                unit_price=value["unit_price"], remarks=value["remarks"],
                                                po_id=header_id)
            po_detail_update.save()
        return JsonResponse({"result": "success"})
    return render(request, 'customer/edit_purchase_order_customer.html',
                  {'po_header': po_header, 'pk': pk, 'po_detail': po_detail, 'all_item_code': all_item_code,
                   'all_accounts': all_accounts, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'allow_inventory_roles': allow_inventory_roles, 'allow_report_roles': report_roles(request.user),
                   'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_purchase_order_print)
def print_po_customer(request, pk):
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    lines = 0
    total_amount = 0
    company_info = Company_info.objects.filter(id=1)
    header = PoHeaderCustomer.objects.filter(company, id=pk).first()
    detail = PoDetailCustomer.objects.filter(po_id=pk).all()
    for value in detail:
        amount = float(value.unit_price * value.quantity)
        total_amount = total_amount + amount
    pdf = render_to_pdf('customer/po_customer_pdf.html',
                        {'company_info': company_info, 'header': header, 'detail': detail, 'total_amount': total_amount,
                         'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                         'allow_transaction_roles': allow_transaction_roles,
                         'allow_inventory_roles': allow_inventory_roles,
                         'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Quotation_Supplier_%s.pdf" % ("123")
        content = "inline; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


@login_required
@user_passes_test(allow_purchase_order_delete)
def delete_po_customer(request, pk):
    PoDetailCustomer.objects.filter(po_id_id=pk).all().delete()
    PoHeaderCustomer.objects.filter(id=pk).delete()
    messages.add_message(request, messages.SUCCESS, " Customer Purchase Order Deleted")
    return redirect('purchase-order-customer')


@login_required
@user_passes_test(allow_delivery_challan_display)
def delivery_challan_customer(request):
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    permission = delivery_challan_roles(request.user)
    all_dc = DcHeaderCustomer.objects.filter(company).all()
    cursor = connection.cursor()
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    is_dc = cursor.execute('''Select Distinct id,dc_no,company_id_id From (
                        Select distinct dc_id_id, IP.product_code,IP.product_name,
                        DC.Quantity As DcQuantity,
                        ifnull(sum(SD.Quantity),0) As SaleQuantity,
                        (DC.Quantity-ifnull(Sum(SD.Quantity),0)) As RemainingQuantity
                        from customer_dcdetailcustomer DC
                        inner join inventory_add_products IP on DC.item_id_id = IP.id
                        Left Join transaction_saledetail SD on SD.dc_ref = DC.dc_id_id
                        And SD.item_id_id = IP.id
                        group by dc_id_id,IP.product_code,IP.product_name
                        ) As tblData
                        Inner Join customer_dcheadercustomer HD on  HD.id = tblData.dc_id_id
                        Where RemainingQuantity > 0 AND Company_id_id = %s
                        ''', [company.id])
    is_dc = is_dc.fetchall()
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    gst = Company_info.objects.filter(id=company.id).first()
    return render(request, 'customer/delivery_challan_customer.html',
                  {'gst': gst, 'all_dc': all_dc, 'is_dc': is_dc, 'permission': permission,
                   'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                   'allow_transaction_roles': allow_transaction_roles, 'allow_inventory_roles': allow_inventory_roles,
                   'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_delivery_challan_add)
def new_delivery_challan_customer(request):
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    branch = request.session['branch']
    branch = Branch.objects.get(branch_id=branch)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    row = []
    cursor = connection.cursor()
    all_item_code = Add_products.objects.all()
    all_po_code = PoHeaderCustomer.objects.all()
    get_last_dc_no = DcHeaderCustomer.objects.filter(company_id=company.id).last()
    customer = Q(account_id="100")
    supplier = Q(account_id="200")
    all_accounts = ChartOfAccount.objects.filter(customer | supplier).all()
    if get_last_dc_no:
        get_last_dc_no = get_last_dc_no.dc_no
        # get_last_dc_no = get_last_dc_no[-3:]
        num = int(get_last_dc_no)
        num = num + 1
        get_last_dc_no = num
    else:
        get_last_dc_no = 101
    item_code_dc = request.POST.get('item_code_dc', False)
    focus = request.POST.get('focus', False)
    if focus:
        data = Add_products.objects.all()
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    if item_code_dc:
        data = Add_products.objects.filter(product_code=item_code_dc)
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    item_code_po_dc = request.POST.get('item_code_po_dc', False)

    if item_code_po_dc:
        id = PoHeaderCustomer.objects.get(company, po_client=item_code_po_dc)
        item_id = PoDetailCustomer.objects.filter(po_id=id).all()
        for value in item_id:
            row.append(value.item_id.id)
        a = (str(row)[1:-1])
        row = cursor.execute(f'''select * from inventory_add_products where id in ({a})''')
        row = row.fetchall()
        return JsonResponse({'row': row, 'id': id.id})
    # get_item_code = request.POST.get('item_code', False)
    # quantity = request.POST.get('quantity', False)
    # if get_item_code:
    #     cursor.execute('''Select item_code, item_name,Item_description,Unit,SUM(quantity) As qty From (
    #                     Select 'Opening Stock' As TranType,Product_Code As Item_Code,Product_Name As Item_name,Product_desc As Item_description,Unit As unit,Opening_Stock as Quantity From inventory_add_products
    #                     where product_code = %s
    #                     union All
    #                     Select 'Purchase' As TranType,Item_Code,Item_name,Item_description,unit,Quantity From transaction_purchasedetail
    #                     where item_code = %s
    #                     union All
    #                     Select 'Purchase Return' As TranType,Item_Code,Item_name,Item_description,unit,Quantity * -1 From transaction_purchasereturndetail
    #                     where item_code = %s
    #                     union All
    #                     Select 'Sale' As TranType,Item_Code,Item_name,Item_description,unit,Quantity * -1 From transaction_saledetail
    #                     where item_code = %s
    #                     union All
    #                     Select 'Sale Return' As TranType,Item_Code,Item_name,Item_description,unit,Quantity  From transaction_salereturndetail
    #                     where item_code = %s
    #                     ) As tblTemp
    #                     Group by Item_Code''',[get_item_code,get_item_code,get_item_code,get_item_code,get_item_code])
    #     row = cursor.fetchall()
    #     print(row)
    #     a = row[0][4]
    #     b = quantity
    #     if int(a) >= int(b):
    #         return JsonResponse({"message":"True"})
    #     else:
    #         return JsonResponse({"message":"False"})
    if request.method == 'POST':
        dc_customer = request.POST.get('customer', False)
        po_client = request.POST.get('po_client', False)
        date = request.POST.get('date', False)
        follow_up = request.POST.get('follow_up', False)
        footer_remarks = request.POST.get('footer_remarks', False)
        account_id = ChartOfAccount.objects.get(account_title=dc_customer)
        # date = datetime.date.today()
        if follow_up:
            follow_up = follow_up
        else:
            follow_up = '2010-06-22'
        cartage_amount = 0.00
        dc_header = DcHeaderCustomer(dc_no=get_last_dc_no, date=date, follow_up=follow_up, cartage_amount=0.00,
                                     po_no=po_client, footer_remarks=footer_remarks, account_id=account_id,
                                     user_id=request.user, company_id=company, branch_id=branch)
        dc_header.save()
        items = json.loads(request.POST.get('items'))
        header_id = DcHeaderCustomer.objects.filter(company_id=company.id, branch_id=branch).get(dc_no=get_last_dc_no)
        for value in items:
            item_id = Add_products.objects.get(id=value["id"])
            dc_detail = DcDetailCustomer(item_id=item_id, description=value["description"], quantity=value["quantity"],
                                         accepted_quantity=0, returned_quantity=0, po_no=value["po_no"],
                                         dc_id=header_id)
            dc_detail.save()
        return JsonResponse({'result': 'success'})
    return render(request, 'customer/new_delivery_challan_customer.html',
                  {'all_item_code': all_item_code, 'get_last_dc_no': get_last_dc_no, 'all_accounts': all_accounts,
                   'all_po_code': all_po_code, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'allow_inventory_roles': allow_inventory_roles, 'allow_report_roles': report_roles(request.user),
                   'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_delivery_challan_edit)
def edit_delivery_challan_customer(request, pk):
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    branch = request.session['branch']
    branch = Branch.objects.get(branch_id=branch)
    company = Q(company_id=company)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    data = ''
    row = []
    cursor = connection.cursor()
    dc_header = DcHeaderCustomer.objects.filter(company, id=pk).first()
    dc_detail = DcDetailCustomer.objects.filter(dc_id=dc_header.id).all()
    all_po_code = PoHeaderCustomer.objects.filter(company).all()
    all_item_code = Add_products.objects.all()
    customer = Q(account_id="100")
    supplier = Q(account_id="200")
    all_accounts = ChartOfAccount.objects.filter(customer | supplier).all()
    item_code = request.POST.get('item_code')
    if item_code:
        item_id = Add_products.objects.get(product_code=item_code)
        data = Add_products.objects.filter(id=item_id.id)
        item_code_exist = DcDetailCustomer.objects.filter(item_id=item_id, dc_id=pk).first()
        if item_code_exist:
            return HttpResponse(json.dumps({'message': "Item Already Exist"}))
        row = serializers.serialize('json', data)
        return HttpResponse(json.dumps({'row': row}))
    # item_code_po_dc = request.POST.get('item_code_po_dc',False)
    # if item_code_po_dc:
    #     id = PoHeaderCustomer.objects.get(company, po_client = item_code_po_dc)
    #     item_id = PoDetailCustomer.objects.filter(po_id = id).all()
    #     for value in item_id:
    #         row.append(value.item_id.id)
    #     a = (str(row)[1:-1])
    #     row = cursor.execute(f'''select * from inventory_add_products where id in ({a})''')
    #     row = row.fetchall()
    #     return JsonResponse({'row':row,'id':id.id})
    if request.method == 'POST':
        dc_detail.delete()
        edit_dc_customer = request.POST.get('customer')
        date = request.POST.get('date')
        follow_up = request.POST.get('follow_up')
        po_no = request.POST.get('item_code_po_dc')
        footer_remarks = request.POST.get('footer_remarks')
        account_id = ChartOfAccount.objects.get(account_title=edit_dc_customer)
        header_id = DcHeaderCustomer.objects.get(id=pk)
        if follow_up:
            follow_up = follow_up
        else:
            follow_up = '2010-06-22'
        dc_header.account_id = account_id
        dc_header.date = date
        dc_header.po_no = po_no
        dc_header.follow_up = follow_up
        dc_header.footer_remarks = footer_remarks
        dc_header.save()

        items = json.loads(request.POST.get('items'))
        for value in items:
            item_id = Add_products.objects.get(id=value["id"])
            dc_detail_update = DcDetailCustomer(item_id=item_id, description=value["description"],
                                                quantity=value["quantity"], accepted_quantity=0, returned_quantity=0,
                                                po_no=value["po_no"], dc_id=header_id)
            dc_detail_update.save()
        return JsonResponse({"result": "success"})
    return render(request, 'customer/edit_delivery_challan_customer.html',
                  {'dc_header': dc_header, 'pk': pk, 'dc_detail': dc_detail, 'all_item_code': all_item_code,
                   'all_accounts': all_accounts, 'all_po_code': all_po_code,
                   'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                   'allow_transaction_roles': allow_transaction_roles, 'allow_inventory_roles': allow_inventory_roles,
                   'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_delivery_challan_print)
def print_dc_customer(request, pk):
    company = request.session['company']
    company_info = Company_info.objects.filter(id=company).all()
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    lines = 0
    total_amount = 0
    image = Company_info.objects.filter(id=1).first()
    header = DcHeaderCustomer.objects.filter(company, id=pk).first()
    detail = DcDetailCustomer.objects.filter(dc_id=header.id).all()
    pdf = render_to_pdf('customer/dc_customer_pdf.html',
                        {'company_info': company_info, 'image': image, 'header': header, 'detail': detail,
                         'allow_customer_roles': allow_customer_roles, 'allow_supplier_roles': allow_supplier_roles,
                         'allow_transaction_roles': allow_transaction_roles,
                         'allow_inventory_roles': allow_inventory_roles,
                         'allow_report_roles': report_roles(request.user), 'is_superuser': request.user.is_superuser})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "DC_Customer_%s.pdf" % (header.dc_no)
        content = "inline; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


@login_required
@user_passes_test(allow_delivery_challan_delete)
def delete_delivery_challan_customer(request, pk):
    if SaleDetail.objects.filter(dc_ref=pk).all():
        messages.add_message(request, messages.ERROR, "Permission to delete denied.")
    else:
        DcDetailCustomer.objects.filter(dc_id_id=pk).all().delete()
        DcHeaderCustomer.objects.filter(id=pk).delete()
        messages.add_message(request, messages.SUCCESS, "Customer Delivery Challan Deleted")

    return redirect('delivery-challan-customer')


@login_required
@user_passes_test(allow_mrn_display)
def mrn_customer(request):
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    permission = mrn_roles(request.user)
    all_dc = DcHeaderCustomer.objects.all()
    return render(request, 'customer/mrn_customer.html',
                  {'all_dc': all_dc, 'permission': permission, 'allow_customer_roles': allow_customer_roles,
                   'allow_supplier_roles': allow_supplier_roles, 'allow_transaction_roles': allow_transaction_roles,
                   'allow_inventory_roles': allow_inventory_roles, 'allow_report_roles': report_roles(request.user),
                   'is_superuser': request.user.is_superuser})


@login_required
@user_passes_test(allow_mrn_edit)
def edit_mrn_customer(request, pk):
    company = request.session['company']
    company = Company_info.objects.get(id=company)
    company = Q(company_id=company)
    allow_customer_roles = customer_roles(request.user)
    allow_supplier_roles = supplier_roles(request.user)
    allow_transaction_roles = transaction_roles(request.user)
    allow_inventory_roles = inventory_roles(request.user)
    dc_header = DcHeaderCustomer.objects.filter(company, id=pk).first()
    dc_detail = DcDetailCustomer.objects.filter(dc_id=dc_header.id).all()
    if request.method == 'POST':
        follow_up = request.POST.get('follow_up', False)
        dc_header.follow_up = follow_up
        dc_header.save()
        items = json.loads(request.POST.get('items'))
        for i, value in enumerate(dc_detail):
            value.accepted_quantity = items[i]["accepted_quantity"]
            value.save()
        return JsonResponse({"result": "success"})
    return render(request, 'customer/edit_mrn_customer.html', {'dc_header': dc_header, 'dc_detail': dc_detail, 'pk': pk,
                                                               'allow_customer_roles': allow_customer_roles,
                                                               'allow_supplier_roles': allow_supplier_roles,
                                                               'allow_transaction_roles': allow_transaction_roles,
                                                               'allow_inventory_roles': allow_inventory_roles,
                                                               'allow_report_roles': report_roles(request.user),
                                                               'is_superuser': request.user.is_superuser})
