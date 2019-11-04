from django.db import models
from django.urls import reverse

class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.imie) + str(self.nazwisko))

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.pk})

class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE, editable=False)
    telefon = models.CharField(max_length=50)

    def __str__(self):
        return (str(self.telefon) + ": " + str(self.osoba))

    def get_absolute_url(self):
        return reverse('phone', kwargs={'pk': self.pk})


class Email(models.Model):
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE, editable=False)
    email = models.EmailField()

    def __str__(self):
        return (str(self.email) + ": " + str(self.osoba))

    def get_absolute_url(self):
        return reverse('email', kwargs={'pk': self.pk})

