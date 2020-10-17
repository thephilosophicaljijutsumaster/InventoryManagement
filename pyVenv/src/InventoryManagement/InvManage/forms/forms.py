from django import forms
from InvManage.models import Product, Vendor, PurchaseOrder, Consumer
from django.utils import timezone

class ProductBasicInfoForm(forms.Form):
    prefix = "basic"
    context={
        "class": "form-control",
    }
    # Basic Information form fields
    name = forms.CharField(widget=forms.TextInput(attrs=context))
    item_type = forms.CharField(widget=forms.TextInput(attrs=context))
    category = forms.CharField(widget=forms.TextInput(attrs=context))
    description = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 3
        }
    ))

class ProductDetailedInfoForm(forms.Form):
    prefix = "detailed"
    context={
        "class": "form-control",
    }
    # Dimensions form fields
    length = forms.CharField(widget=forms.TextInput(attrs=context))
    width = forms.CharField(widget=forms.TextInput(attrs=context))
    height = forms.CharField(widget=forms.TextInput(attrs=context))
    weight = forms.CharField(widget=forms.TextInput(attrs=context))


class ThumbnailForm(forms.Form):
    prefix = "thumbnail"
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "upload"}))

class ProductStorageInfoForm(forms.Form):
    prefix = "storage"
    barcode = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    context={
        "class": "form-control",
        "type": "date"
    }
    expiry = forms.DateField(widget=forms.widgets.DateInput(attrs=context),initial=timezone.now)

class ProductPricingForm(forms.Form):
    prefix = "pricing"
    context={
        "class": "form-control",
    }
    price = forms.FloatField(label="MRP",widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1", "class": "form-control"}))
    discount = forms.FloatField(widget=forms.NumberInput(attrs={'id': 'form_homework', 'step': "1", "class": "form-control"}))

class ProductStatusForm(forms.Form):
    context={
        "class": "form-control",
    }
    prefix = "status"
    quantity = forms.IntegerField(label="Quantity", widget=forms.NumberInput(attrs={"class": "score form-control"}))
    identifier = forms.CharField(label="Identifier", widget=forms.TextInput(attrs={"class": "score form-control"}))
    location = forms.CharField(label="Location",widget=forms.TextInput(attrs={"class": "score form-control"}))

####### Purchase Order Forms #########
class PurchaseOrderBasicInfo(forms.Form):
    prefix = "po"
    context={
        "class": "form-control",
    }
    product_choices = [(p.id, p.name) for p in Product.objects.all()]
    vendor_choices = ((v.id,v.name) for v in Vendor.objects.all())
    # Vendor details
    vendor = forms.ModelChoiceField(queryset= Vendor.objects.all(),required=True, widget=forms.Select(attrs=context))
    # Order details
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date","class":"form-control"}), initial=timezone.now)
    po = forms.IntegerField(label="PO", widget=forms.TextInput(attrs=context))
    # Pricing details
    discount = forms.FloatField(widget=forms.TextInput(attrs=context))
    tax = forms.FloatField(widget=forms.TextInput(attrs=context))
    paid = forms.FloatField(widget=forms.TextInput(attrs=context))
    balance = forms.FloatField(widget=forms.TextInput(attrs=context))
    subtotal = forms.FloatField(widget=forms.TextInput(attrs=context),initial=0.0)
    taxtotal = forms.FloatField(widget=forms.TextInput(attrs=context),initial=0.0)
    ordertotal = forms.FloatField(widget=forms.TextInput(attrs=context),initial=0.0)
    
    
####### GRN Forms #########
class GRNInfo(forms.Form):
    prefix = "grn"
    context={
        "class": "form-control",
    }
    product_choices = [(p.id, p.name) for p in Product.objects.all()]
    vendor_choices = ((v.id,v.name) for v in Vendor.objects.all())
    vendor = forms.ModelChoiceField(queryset= Vendor.objects.all(),required=True, widget=forms.Select(attrs=context))
    TYPE_CHOICES = [
        ('manual', 'Blank'),
        ('auto', 'PO Reference')
    ]
    poRef = forms.MultipleChoiceField(label="PO References", required=False, widget=forms.SelectMultiple(attrs=context))
    identifier = forms.CharField(label="GRN Number",widget=forms.TextInput(attrs=context)) 
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date","class":"form-control"}), initial=timezone.now)
    grnType = forms.ChoiceField(choices=TYPE_CHOICES, label="Receipt Type", widget=forms.Select(attrs=context))
    amendNumber = forms.IntegerField(label="Amendment Number", widget=forms.TextInput(attrs=context))
    amendDate = forms.DateField(label="Amendment Date", widget=forms.widgets.DateInput(attrs={"type": "date","class":"form-control"}), initial=timezone.now)
    vehicleNumber = forms.CharField(label="Vehicle Number", widget=forms.TextInput(attrs=context))
    gateInwardNumber = forms.CharField(label="Inward Number", widget=forms.TextInput(attrs=context))
    preparedBy = forms.CharField(label="Prepared By", widget=forms.TextInput(attrs=context))   
    checkedBy = forms.CharField(label="Checked By", widget=forms.TextInput(attrs=context))   
    inspectedBy = forms.CharField(label="Inspected By", widget=forms.TextInput(attrs=context))   
    approvedBy = forms.CharField(label="Approved By ", widget=forms.TextInput(attrs=context))   
    

####### Sales Order Forms #########
class SalesOrderBasicInfo(forms.Form):
    prefix = "so"
    context={
        "class": "form-control",
    }
    product_choices = [(p.id, p.name) for p in Product.objects.all()]
    consumer_choices = ((c.id,c.name) for c in Consumer.objects.all())
    # Vendor details
    consumer = forms.ModelChoiceField(queryset= Consumer.objects.all(),required=True, widget=forms.Select(attrs=context))
    # Order details
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={"type": "date","class":"form-control"}), initial=timezone.now)
    so = forms.IntegerField(label="SO", widget=forms.TextInput(attrs=context))
    # Pricing details
    discount = forms.FloatField(widget=forms.TextInput(attrs=context))
    tax = forms.FloatField(widget=forms.TextInput(attrs=context))
    paid = forms.FloatField(widget=forms.TextInput(attrs=context))
    balance = forms.FloatField(widget=forms.TextInput(attrs=context))
    subtotal = forms.FloatField(widget=forms.TextInput(attrs=context),initial=0.0)
    taxtotal = forms.FloatField(widget=forms.TextInput(attrs=context),initial=0.0)
    ordertotal = forms.FloatField(widget=forms.TextInput(attrs=context),initial=0.0)

    
class ConsumerForm(forms.Form):
    prefix = "consumer"
    context={
        "class": "form-control",
    }
    name = forms.CharField(widget=forms.TextInput(attrs=context))
    identifier = forms.CharField(widget=forms.TextInput(attrs=context))
    phone = forms.CharField(widget=forms.TextInput(attrs=context))
    address = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 3
        }
    ))
    email = forms.CharField(widget=forms.TextInput(attrs=context))
    location = forms.CharField(widget=forms.TextInput(attrs=context))


class GRNEntryForm(forms.Form):
    prefix = "form"
    context = {
        "class": "form-control",
    }
    product = forms.ModelChoiceField(
                    queryset= Product.objects.all(),
                    widget=forms.Select(attrs={
                                            "class": "form-control",
                                            "onchange":"setIdentifier(this)"}))
    grne_id = forms.IntegerField(widget=forms.TextInput(attrs={"value":""}))
    ppe = forms.IntegerField(widget=forms.TextInput(attrs=context))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs=context))
    remark = forms.CharField(widget=forms.TextInput(attrs=context))
    receivedQty = forms.CharField(widget=forms.TextInput(attrs=context))
    acceptedQty = forms.CharField(widget=forms.TextInput(attrs=context))
    rejectedQty = forms.CharField(widget=forms.TextInput(attrs=context))
    

class ProductPurchaseEntryForm(forms.Form):
    prefix = "form"
    context={
        "class": "form-control",
    }
    # product_choices = [(p.id, p.name) for p in Product.objects.all()]
    ppe_id = forms.IntegerField(widget=forms.TextInput(attrs={"value":""}))
    product = forms.ModelChoiceField(
                    queryset= Product.objects.all(),
                    widget=forms.Select(attrs={
                                            "class": "form-control",
                                            "onchange":"setIdentifier(this)"}))
    # identifier = forms.CharField(widget=forms.)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs=context))
    price = forms.FloatField(widget=forms.TextInput(attrs=context))
    discount = forms.FloatField(widget=forms.TextInput(attrs=context))
    
    
class ProductSalesEntryForm(forms.Form):
    prefix = "form"
    context={
        "class": "form-control",
    }
    # product_choices = [(p.id, p.name) for p in Product.objects.all()]
    pse_id = forms.IntegerField(widget=forms.TextInput(attrs={"value":""}))
    product = forms.ModelChoiceField(
                    queryset= Product.objects.all(),
                    widget=forms.Select(attrs={
                                            "class": "form-control",
                                            "onchange":"setIdentifier(this)"}))
    # identifier = forms.CharField(widget=forms.)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs=context))
    price = forms.FloatField(widget=forms.TextInput(attrs=context))
    discount = forms.FloatField(widget=forms.TextInput(attrs=context))
    

class CompanyForm(forms.Form):
    prefix = "comp"
    context={
        "class": "form-control",
    }
    name = forms.CharField(widget=forms.TextInput(attrs=context))
    owner = forms.CharField(widget=forms.TextInput(attrs=context))
    phone = forms.CharField(widget=forms.TextInput(attrs=context))
    address = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 3
        }
    ))
    email = forms.CharField(widget=forms.TextInput(attrs=context))
    location = forms.CharField(widget=forms.TextInput(attrs=context))


    
class HistoryForm(forms.Form):
    prefix = 'history'
    context={
        "class": "form-control",
    }
    qlen = forms.IntegerField(widget=forms.TextInput(attrs=context))