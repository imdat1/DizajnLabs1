from django.db import models

# Create your models here.

class Kategorija(models.Model):
    ime_kategorija = models.CharField(max_length=50)
    opis = models.CharField(max_length=50)
class Gotvac(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=60)
    bio = models.EmailField()
    profile_picture= models.ImageField()
    date_of_birth = models.DateField()
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE, blank= True, null= True)
class Recept(models.Model):
    naslov = models.CharField(max_length=50)
    TYPE_CHOICES = [
        ("IT", "italjanska"),
        ("CH", "kineska"),
        ("JP", "japonska"),
        ("MX", "meksikanska"),
    ]

    kategorija = models.CharField(max_length=3, choices=TYPE_CHOICES)
    gotvac = models.ForeignKey(Gotvac, on_delete=models.CASCADE)
    opis=models.CharField(max_length=60)
    sostojki = models.CharField(max_length=90)
    instrukcii = models.CharField(max_length=90)
    dali_veganski = models.BooleanField()
    dali_bez_gluten = models.BooleanField()

class SlikaRecept(models.Model):
    slika = models.ImageField()

class ReceptSliki(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    slika = models.ForeignKey(SlikaRecept, on_delete=models.CASCADE)

class Pregled(models.Model):
    RATING = [
        ("ED", "1"),
        ("DV", "2"),
        ("TR", "3"),
        ("CT", "4"),
        ("PT", "5")
    ]
    rating_cook = models.CharField(max_length=3, choices=RATING)
    komentar = models.CharField(max_length=90)
    datum_dodavanje = models.DateField()

class ReceptPregled(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    pregled = models.ForeignKey(Pregled, on_delete=models.CASCADE)

class KnigaZaGotvenje(models.Model):
    TYPE_KUJNA = [
        ("IT", "italjanska"),
        ("CH", "kineska"),
        ("JP", "japonska"),
        ("MX", "meksikanska")
    ]
    naslov = models.CharField(max_length=90)
    gotvac = models.ForeignKey(Gotvac, on_delete=models.CASCADE)
    tip_kujna = models.CharField(max_length=3, choices=TYPE_KUJNA)

class KnigaRecepti(models.Model):
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    kniga = models.ForeignKey(KnigaZaGotvenje, on_delete=models.CASCADE)

class NagradaRecept(models.Model):
    naslov_nagrada = models.CharField(max_length=90)
    recept = models.ForeignKey(Recept, on_delete=models.CASCADE)
    datum_dobiena_nagrada=models.DateField()

