from django.shortcuts import render,redirect
from .forms import PermitForm, ProjectForm, SaleForm
from django.contrib import messages
from django.http import JsonResponse
from .models import Project
# Create your views here.

def permit_create(request):
    if request.method == 'POST':
        form = PermitForm(request.POST)
        if form.is_valid():
            permit = form.save(commit=False)
            permit.creator = request.user  # Assigning the current user to the creator
            permit.save()
            
            #Show a success message
            messages.success(request, 'Permit created successfully')
            return redirect('home')  # Redirect to the homepage 
    else:
        form = PermitForm()
    
    return render(request, 'permit_create.html', {'form': form})

def project_form(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        print(form.errors)
        if form.is_valid():
            project = form.save(commit=False)            
            project.creator = request.user  # Assigning the current user to the creator
            project.save()
            #Show a success message            
            messages.success(request, 'Project Created successfully')
            return redirect('home')  # Redirect to the homepage 
    else:
        form = ProjectForm()
    
    return render(request, 'project_create.html', {'form': form})

def sale_form(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        print(form.errors)
        if form.is_valid():
            sale = form.save(commit=False)            
            sale.owner = request.user  # Assigning the current user to the creator    
            sale.save()
            #Show a success message
            messages.success(request, 'Sale Created successfully')
            return redirect('home')
    else:
        form = SaleForm()
    
    return render(request, 'sale_create.html', {'form': form})

def get_partner_share(request):
    if request.method == 'GET'and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        project_id = request.GET.get('project_id') # Get Project ID from AJAX request
        
        try:
            project = Project.objects.get(pk=project_id) # Get the project object            
            partner_share = project.partner_share # Get the partner share
            
            # Return the Partner Share as a JSON Response
            return JsonResponse({'partner_share': partner_share})
        except Project.DoesNotExist:
            return JsonResponse({'error': 'Project not found'}, status=404)
        
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
            