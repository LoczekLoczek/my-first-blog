from django.db import models
from django.urls import reverse

class Produkty(models.Model):
    name = models.CharField(max_length=20, default="")
    image = models.ImageField(upload_to='images/', default='default.jpg')
    krotkiopis = models.CharField(max_length=50, default="", blank=True)
    dlugiopis = models.CharField(max_length=800, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/opisproduktu/{self.id}/"
        return reverse("opisproduktu", kwargs={"id": self.id})