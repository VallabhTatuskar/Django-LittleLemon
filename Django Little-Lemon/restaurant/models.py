from django.db import models

# Booking model
class Booking(models.Model):
    first_name = models.CharField(max_length=200, help_text="Enter the guest's first name")
    last_name = models.CharField(max_length=200, help_text="Enter the guest's last name")
    guest_number = models.IntegerField(help_text="Number of guests")
    comment = models.CharField(max_length=1000, blank=True, help_text="Any additional comments or requests (optional)")

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# Menu model
class Menu(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the menu item name")
    price = models.IntegerField(null=False, help_text="Enter price in USD or your local currency")
    description = models.TextField(blank=True, help_text="Enter a short description of this menu item")

    def __str__(self):
        return self.name
