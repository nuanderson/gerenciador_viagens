from django.db import models

class Passenger(models.Model):
    # Informações Pessoais
    name = models.CharField(max_length=100, verbose_name='Nome do Passageiro')
    cpf = models.CharField(max_length=14, verbose_name='CPF')
    number_rg = models.CharField(max_length=20, verbose_name='Número do RG')
    issuing_body = models.CharField(max_length=50, verbose_name='Órgão Emissor')
    date_of_birth = models.DateField(verbose_name='Data de Nascimento')
    phone_number = models.CharField(max_length=15, verbose_name='Número de Telefone')
    phone_secondary = models.CharField(max_length=15, null=True, blank=True, verbose_name='Número de Telefone Secundário')
    # Endereço
    street_address = models.CharField(max_length=150, verbose_name='Endereço')
    number_address = models.CharField(max_length=10, verbose_name='Número')
    complement = models.CharField(max_length=100, null=True, blank=True, verbose_name='Complemento')
    neighborhood = models.CharField(max_length=100, verbose_name='Bairro')
    city = models.CharField(max_length=100, verbose_name='Cidade')
    state = models.CharField(max_length=100, verbose_name='Estado')
    zip_code = models.CharField(max_length=10, verbose_name='CEP')
    # Informações Adicionais
    emergency_contact_name = models.CharField(max_length=100, verbose_name='Nome do Contato de Emergência')
    emergency_contact_phone = models.CharField(max_length=15, verbose_name='Telefone do Contato de Emergência')
    observations = models.TextField(null=True, blank=True, verbose_name='Observações')
    active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.name
