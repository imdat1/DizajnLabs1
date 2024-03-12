from django.contrib import admin

from .models import Gotvac, Recept, SlikaRecept, ReceptSliki, Pregled, ReceptPregled, KnigaZaGotvenje, KnigaRecepti, NagradaRecept, Kategorija

admin.site.register(Gotvac)
admin.site.register(Recept)
admin.site.register(SlikaRecept)
admin.site.register(ReceptSliki)
admin.site.register(Pregled)
admin.site.register(ReceptPregled)
admin.site.register(KnigaZaGotvenje)
admin.site.register(KnigaRecepti)
admin.site.register(NagradaRecept)
admin.site.register(Kategorija)
