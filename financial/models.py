from django.db import models
from . events import Event
from . passenger import Passenger

class Sale(models.Model):
    class SaleStatus(models.TextChoices):
        PENDING = 'pending', _('Pendente')
        PARTIALLY_PAID = 'partially_paid', _('Parcialmente Pago')
        PAID = 'paid', _('Pago')
        CANCELED = 'canceled', _('Cancelado')

    class PaymentMethod(models.TextChoices):
        CREDIT_CARD = 'credit_card', _('Cartão de Crédito')
        DEBIT_CARD = 'debit_card', _('Cartão de Débito')
        BANK_TRANSFER = 'bank_transfer', _('Transferência Bancária')
        CASH = 'cash', _('Dinheiro')
        PIX = 'pix', _('PIX')

    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name='Evento')
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, verbose_name='Passageiro')
    total_sale_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Total da Venda')
    base_payment_method = models.CharField(
        max_length=50, 
        choices=PaymentMethod.choices, 
        verbose_name='Método de Pagamento Base'
    )
    status_payment = models.CharField(
        max_length=15,
        choices=SaleStatus.choices,
        default=SaleStatus.PENDING,
        verbose_name='Status do Pagamento'
    )
    sale_date = models.DateTimeField(auto_now_add=True, verbose_name='Data da Venda')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor Pago')
    receipt_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Número do Recibo')
    observations = models.TextField(null=True, blank=True, verbose_name='Observações')
    sale_created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Venda Criada por')

    def __str__(self):
        return f"Venda: {self.passenger.name} - Evento: {self.event.title}"

class Installment(models.Model):
    """ Representa uma parcela do 'carnê' """
    class InstallmentStatus(models.TextChoices):
        PENDING = 'pending', _('Pendente')
        PAID = 'paid', _('Pago')
        LATE = 'late', _('Em Atraso')
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Venda')
    installment_number = models.PositiveIntegerField(verbose_name='Número da Parcela')
    due_date = models.DateField(verbose_name='Data de Vencimento')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor da Parcela')
    status_installment = models.CharField(
        max_length=10,
        choices=InstallmentStatus.choices,
        default=InstallmentStatus.PENDING,
        verbose_name='Status da Parcela'
    )
    payment_date = models.DateField(null=True, blank=True, verbose_name='Data de Pagamento')
    payment_method = models.CharField(
        max_length=50,
        choices=Sale.PaymentMethod.choices,
        null=True,
        blank=True,
        verbose_name='Método de Pagamento'
    )
    receipt_number = models.CharField(max_length=100, null=True, blank=True, verbose_name='Número do Recibo')

    class Meta:
        # Garante que não haja duas parcelas com o mesmo número para a mesma venda
        unique_together = ('sale', 'installment_number')
        ordering = ['due_date']

    def __str__(self):
        return f"Parcela {self.installment_number} - Venda: {self.sale.passenger.name}"

class Payment(models.Model):
    """ Registra um pagamento individual, que pode ser de uma parcela ou avulso """
    class PaymentMethod(models.TextChoices):
        CASH = 'cash', _('Dinheiro')
        CREDIT_CARD = 'credit_card', _('Cartão de Crédito')
        DEBIT_CARD = 'debit_card', _('Cartão de Débito')
        PIX = 'pix', _('Pix')
        BANK_TRANSFER = 'bank_transfer', _('Transferência Bancária')
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Venda')
    installment = models.ForeignKey(Installment, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Parcela')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Data do Pagamento')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Valor do Pagamento')
    payment_method = models.CharField(
        max_length=50,
        choices=PaymentMethod.choices,
        null=True,
        blank=True,
        verbose_name='Método de Pagamento'
    )
    observations = models.TextField(null=True, blank=True, verbose_name='Observações')
    sale_created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Pagamento Criado por')
