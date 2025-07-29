
from django.db import models

# ✅ Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(
        max_length=100,
        choices=(
            ('IT', 'IT'),
            ('NON IT', 'Non IT'),
            ('Mobile Phones', 'Mobile Phones')
        )
    )
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} -- {self.location}"


# ✅ Employee Model (linked with Company using "employer")
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    address = models.CharField(max_length=200)
    employer = models.ForeignKey(Company, on_delete=models.CASCADE)  # ✅ FK to Company
    phone = models.CharField(max_length=50)
    about = models.TextField()
    position = models.CharField(
        max_length=50,
        choices=(
            ('manager', 'Manager'),
            ('software Developer', 'Software Developer'),
            ('project leader', 'Project Leader')
        )
    )

    def __str__(self):
        return self.name
