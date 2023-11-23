from django import forms
from django_countries.fields import CountryField
from .models import Permit, Project, Sale
from django.forms.widgets import TextInput, Select, DateInput
from djmoney.forms import MoneyWidget

class PermitForm(forms.ModelForm):
    
    class Meta:
        model = Permit
        fields = ['name', 'country', 'regulator', 'start_date', 'end_date', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'regulator': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['permit','name', 'status', 'country', 'survey_type', 'project_type', 'start_date', 
                  'end_date', 'description', 'cost','partner_1','partner_2','partner_3','project_size']

        widgets = {
            'permit': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'survey_type': forms.Select(attrs={'class': 'form-select'}),
            'project_type': forms.Select(attrs={'class': 'form-select'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cost': MoneyWidget(attrs={'class': 'form-control', 'rows': 3}),            
            'partner_1': forms.Select(attrs={'class': 'form-select'}),
            'partner_2': forms.Select(attrs={'class': 'form-select'}),
            'partner_3': forms.Select(attrs={'class': 'form-select'}),
            'project_size': forms.NumberInput(attrs={'class': 'form-control'}),
        }
  

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = [
            'project',
            'company',
            'status',
            'probability',
            'license_area',
            'unit_rate',
            'estimated_value',
            'sale_date',
            'weighted_value'
        ]
        widgets = {
            'project': Select(attrs={'class': 'form-control', 'id':'id_project'}),
            'company': Select(attrs={'class': 'form-control'}),            
            'status': Select(attrs={'class': 'form-control'}),
            'probability': TextInput(attrs={'class': 'form-control', 'id':'id_probability'}),
            'license_area': TextInput(attrs={'class': 'form-control', 'id': 'id_license_area'}),
            'unit_rate': MoneyWidget(attrs={'class': 'form-control', 'rows': 3, 'id': 'id_unit_rate'}),
            'estimated_value': MoneyWidget(attrs={'class': 'form-control', 'rows': 3, 'id': 'id_estimated_value'}),
            'sale_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'weighted_value': MoneyWidget(attrs={'class': 'form-control', 'rows': 3, 'id': 'id_weighted_value'}),
        }