from django.db import models

# Create your models here.
from django.db import models


class Gateau(models.Model):
    name = models.CharField('Nom du gateau', max_length=200, unique = False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "gateau"



class Album(models.Model):
    reference = models.IntegerField("référence", null=True)
    created_at = models.DateTimeField("date de création", auto_now_add=True)
    available = models.BooleanField("disponible", default=True)
    title = models.CharField('titre du disque ', max_length=200)
    photo = models.FileField("URL dl image", upload_to="photo/")
    gateaux = models.ManyToManyField(Gateau, related_name='albums', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "album"


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "contact"

class Booking(models.Model):
    created_at = models.DateTimeField("date d'envoie",auto_now_add=True)
    contacted = models.BooleanField("demande traitée ?", default = False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    #album = models.OneToOneField(Album, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.contact)

    class Meta:
        verbose_name = "réservation"