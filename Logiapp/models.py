from django.db import models

# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.amount} - {self.status}"



class ServiceRequest1(models.Model):
    SERVICE_CHOICES = [
        ('store', 'Storage'),
        ('logistics', 'Logistics'),
        ('cargo', 'Cargo'),
        ('trucking', 'Trucking'),
        ('packaging', 'Packaging'),
        ('warehousing', 'Warehousing'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    service = models.CharField(
        max_length=20,
        choices=SERVICE_CHOICES,
        default='web_dev'
    )
    request_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='bookings/')  # New field

    def __str__(self):
        return f"{self.full_name} - {self.get_service_display()}"
