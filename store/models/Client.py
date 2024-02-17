from django.db import models


class Customer(models.Model):
    fname = models.CharField(blank=True,max_length=50)
    phone = models.CharField(blank=True,max_length=10)
    adresse = models.CharField(blank=True, max_length=500)
    email = models.EmailField()
    username = models.CharField(blank=True,max_length=50)
    password = models.CharField(max_length=100)

    def register(self):
        self.save()

    def update(self, **kwargs):
        for field, value in kwargs.items():
            setattr(self, field, value)
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False

    def __str__(self):
        return f"{self.fname} {self.phone} {self.adresse} {self.email} {self.username}"