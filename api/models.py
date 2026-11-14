import uuid

from django.db import models


class FundoImobiliario(models.Model):
    SETOR_CHOICES = [
        ('hibrido', 'Híbrido'),
        ('shoppings', 'Shoppings'),
        ('lajes_corporativas', 'Lajes Corporativas'),
        ('logistica', 'Logística'),
        ('hoteis', 'Hotéis'),
        ('residencial', 'Residencial'),
        ('outros', 'Outros'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.CharField(max_length=6, unique=True)
    setor = models.CharField(max_length=30, choices=SETOR_CHOICES)
    dividend_yield_medio_12m = models.DecimalField(max_digits=5, decimal_places=2)
    vacancia_financeira = models.DecimalField(max_digits=5, decimal_places=2)
    vacancia_fisica = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_ativos = models.IntegerField()

    def __str__(self):
        return self.codigo
