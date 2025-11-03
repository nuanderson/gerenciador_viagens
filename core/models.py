from django.db import models

class Destination(models.Model):
    local_name = models.CharField(max_length=100, verbose_name='Nome do Local')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=100, verbose_name='Estado')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')
    active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return f"{self.local_name}, {self.city}"

class BusCompany(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da Empresa')
    cnpj = models.CharField(max_length=18, verbose_name='CNPJ')
    contact_number = models.CharField(max_length=15, verbose_name='Número de Contato')
    email = models.EmailField(verbose_name='Email')
    active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Motorista')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    license_number = models.CharField(max_length=20, verbose_name='Número da CNH')
    cnh_expiry_date = models.DateField(verbose_name='Data de Validade da CNH')
    phone_number = models.CharField(max_length=15, verbose_name='Número de Telefone')
    bus_company = models.ForeignKey(BusCompany, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Empresa de Ônibus')
    active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return self.name

class TourGuide(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome do Guia')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    cadastur_number = models.CharField(max_length=20, null=True, blank=True, verbose_name='Número Cadastur')
    phone_number = models.CharField(max_length=15, verbose_name='Número de Telefone')
    specialization = models.TextField(null=True, blank=True, verbose_name='Especialização')
    active = models.BooleanField(default=True, verbose_name='Ativo')

    def __str__(self):
        return self.name