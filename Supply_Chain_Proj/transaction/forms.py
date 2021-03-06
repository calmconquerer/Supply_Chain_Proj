from user.models import Company_info, Branch
from .models import ChartOfAccount
from django import forms


class CompanyUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    company_address = forms.CharField(widget=forms.Textarea, required=False)
    company_logo = forms.CharField(widget=forms.Textarea, required=False)
    phone_no = forms.CharField(required=False)
    mobile_no = forms.CharField(required=False)
    website = forms.CharField(required=False)
    ntn = forms.CharField(required=False)
    stn = forms.CharField(required=False)
    cnic = forms.CharField(required=False)

    class Meta:
        model = Company_info
        fields = ['company_name',
                  'company_address',
                  'company_logo',
                  'phone_no',
                  'mobile_no',
                  'email',
                  'website',
                  'ntn',
                  'stn',
                  'cnic']


class BranchUpdateForm(forms.ModelForm):
    branch_email = forms.EmailField(required=False)
    branch_address = forms.CharField(widget=forms.Textarea, required=False)
    branch_name = forms.CharField(widget=forms.Textarea, required=False)
    branch_phone = forms.CharField(required=False)
    branch_mobile = forms.CharField(required=False)

    class Meta:
        model = Branch
        fields = ['branch_name',
                  'branch_address',
                  'branch_phone_no',
                  'branch_mobile_no',
                  'branch_email']


class COAUpdateForm(forms.ModelForm):
    email_address = forms.EmailField(required=False)
    account_id = forms.CharField(required=False)
    parent_id = forms.CharField(widget=forms.NumberInput, required=False)
    opening_balance = forms.DecimalField(required=False)
    phone_no = forms.CharField(required=False)
    ntn = forms.CharField(required=False)
    stn = forms.CharField(required=False)
    cnic = forms.CharField(required=False)
    Address = forms.CharField(required=False)
    remarks = forms.CharField(required=False)
    credit_limit = forms.DecimalField(required=False)
    active = forms.BooleanField(required=False)

    class Meta:
        model = ChartOfAccount
        fields = ['account_id',
                  'account_title',
                  'parent_id',
                  'opening_balance',
                  'phone_no',
                  'email_address',
                  'ntn',
                  'stn',
                  'cnic',
                  'Address',
                  'remarks',
                  'credit_limit',
                  'active'
                  ]
