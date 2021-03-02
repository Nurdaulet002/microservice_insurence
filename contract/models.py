from django.db import models
from directory.models import Insurance, Insurer, Service, ICD


# Базовый mixin
class BaseMixin(models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


# Контракт mixin
class ContractMixin(models.Model):
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE)

    class Meta:
        abstract = True


# Контракт
class Contract(BaseMixin):
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    insurer = models.ForeignKey(Insurer, on_delete=models.CASCADE)


# Исключение услуг
class ServiceExclusion(ContractMixin):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


# Исключение МКБ-10
class ICDExclusion(ContractMixin):
    icd = models.ForeignKey(ICD, on_delete=models.CASCADE)


# Исключение услуг и МКБ-10
class ServiceICDExclusion(ContractMixin):
	services = models.ManyToManyField(Service)
	icds = models.ManyToManyField(ICD)