from django.db import models
from users.models import CustomUser
from django_countries.fields import CountryField
from djmoney.models.fields import MoneyField



# Create your models here.


class Project(models.Model):
    SURVEY_TYPE = (
        ('2D', '2D'),
        ('3D-S', '3D Streamer'),
        ('3D-O', '3D OBN'),
        ('4D-S', '4D Streamer'),
        ('4D-O', '4D OBN'),
        ('OBNL', 'OBN Long Offset'),
        ('HiRes', 'Hi-Res'),
        )
    
    PROJECT_TYPE = (
        ('Repro', 'Reprocessing'),
        ('New Acquisition', 'New Acquisition'),
        )
    
    STATUS = (('Ongoing', 'Ongoing'), ('Completed', 'Completed'),('Cancelled', 'Cancelled'),
              ('Development', 'Development'))
    
    PARTNERS = (('BGP', 'BGP'), ('CGG', 'CGG'), ('SWG', 'Shearwater'), ('PGS', 'PGS'),('SLB', 'SLB'),
                ('COSL','COSL'),('Searcher','Searcher'))
    
    permit = models.ForeignKey('Permit', on_delete=models.CASCADE, related_name='projects')    
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=15, choices=STATUS)
    country = CountryField()
    survey_type = models.CharField(max_length=6, choices=SURVEY_TYPE)
    project_type = models.CharField(max_length=15, choices=PROJECT_TYPE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    project_size = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    # Partners section
    # has_partners = models.BooleanField(default=False)
    partner_1 = models.CharField(max_length=10, choices=PARTNERS, blank=True, null=True, default=None)
    partner_2 = models.CharField(max_length=10, choices=PARTNERS, blank=True, null=True, default=None)
    partner_3 = models.CharField(max_length=10, choices=PARTNERS, blank=True, null=True, default=None)
    partner_share = models.DecimalField(max_digits=5, decimal_places=4, default=1)  # Field for partner share
    
        
    def calculate_partner_share(self):
        partner_count = bool(self.partner_1) + bool(self.partner_2) + bool(self.partner_3) + 1
        return 1 / partner_count if partner_count > 0 else 1

    def save(self, *args, **kwargs):
        self.partner_share = self.calculate_partner_share()  # Update partner_share before saving
        super().save(*args, **kwargs)
    
       
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Permit(models.Model):
    REGULATORS = (
        ("CNH", "CNH (Mexico)"),
        ("ANP", "ANP (Brazil)"),
        ("ANH", "ANH (Colombia)"),
        ("Staatsolie", "Staatsolie (Suriname)"),
        ("ANCAP", "ANCAP (Uruguay)"),
        ("MME", "MME (Brazil)"),
        ("SNE", "SNE (Argentina)"),
    )
    
    name = models.CharField(max_length=100)
    country = CountryField()
    regulator = models.CharField(max_length=10, choices=REGULATORS)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
 
# The Sale class represents a sale in a project, with various attributes such as company, owner,
# status, probability, license area, unit rate, estimated value, weighted value, and sale date.
class Sale(models.Model):
    COMPANIES = (
        ("XOM", "ExxonMobil"),("CVX", "Chevron"),("ECP", "Ecopetrol"),("PBR", "Petrobras"),("RDS", "Shell"),
        ("PEMEX", "Pemex"),("Petronas", "Petronas"), ("BP", "BP"), ("TTE", "TotalEnergies"),("Equinor", "Equinor"),
        ("YPF", "YPF"),("Apache", "Apache"),("Eni", "Eni"),("Repsol", "Repsol"),("OGX", "OGX"),("PetroSA", "PetroSA"),
        ("CNOOC", "CNOOC"),("ONGC", "ONGC"),("NNPC", "NNPC"), ("PetroChina", "PetroChina"),("PTTEP", "PTTEP"),
        ("Sinopec", "Sinopec"),("Inpex", "Inpex"),("JOGMEC", "JOGMEC"),("Mubadala", "Mubadala"),("Qatar Petroleum", "Qatar Petroleum"),
        ("Kuwait Petroleum", "Kuwait Petroleum"),("KrisEnergy", "KrisEnergy"),("PetroVietnam", "PetroVietnam"),
        ("Woodside", "Woodside"),("Hess", "Hess"),("OMV", "OMV"),("CEPSA", "CEPSA")
    )
    
    STATUS = (('Quoted','Quoted'),('Purchased','Purchased'),('Deferred','Deferred'),('Cancelled','Cancelled'))
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='sales')
    company = models.CharField(max_length=16, choices=COMPANIES)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS)
    probability = models.DecimalField(max_digits=6, decimal_places=4, default=0.0)
    license_area = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    unit_rate = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True, null=True)
    estimated_value = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True, null=True)
    weighted_value = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    
    sale_date = models.DateField()
    tgs_net_value = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', blank=True, null=True)
    
    
            