from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from projectmanager.models import Permit, Project,Sale

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email']

@admin.register(Permit)
class PermitAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'regulator', 'creator', 'created', 'updated', 'start_date', 'end_date', 'description')
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'country', 'creator', 'start_date', 'end_date','partner_1','partner_2','partner_3','project_size','partner_share', 'description', 'cost')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('project', 'company', 'status', 'probability', 'license_area', 'unit_rate', 'estimated_value', 'sale_date', 'weighted_value')


admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.
