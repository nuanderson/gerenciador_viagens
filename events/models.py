from django.db import models
from . core import Destination

class Event(models.Model):
    class EventStatus(models.TextChoices):
        SCHEDULED = 'scheduled', _('Agendado')
        CONFIRMED = 'confirmed', _('Confirmado')
        COMPLETED = 'completed', _('Realizado')
        CANCELED = 'canceled', _('Cancelado')

    title = models.CharField(max_length=200, verbose_name='Título do Evento')
    destination = models.ForeignKey('core.Destination', on_delete=models.CASCADE, verbose_name='Destino')
    departure_date = models.DateTimeField(verbose_name='Data de Partida')
    return_date = models.DateTimeField(verbose_name='Data de Retorno')
    total_vacancies = models.PositiveIntegerField(verbose_name='Total de Vagas')
    event_status = models.CharField(
        max_length=10,
        choices=EventStatus.choices,
        default=EventStatus.SCHEDULED,
        verbose_name='Status do Evento'
    )
    # Financial Details
    standard_package_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do Pacote Padrão')
    bus_company_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Custo da Empresa de Ônibus')
    driver_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Custo do Motorista')
    tour_guide_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Custo do Guia de Turismo')
    other_costs = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Outros Custos')

    description = models.TextField(null=True, blank=True, verbose_name='Descrição do Evento')
    internal_observations = models.TextField(null=True, blank=True, verbose_name='Observações Internas')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Criado por')

    def __str__(self):
        return self.title
