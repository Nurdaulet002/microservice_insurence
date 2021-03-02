from django.db import models
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


# Базовый mixin
class BaseMixin(models.Model):
    title = models.CharField(max_length=180)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


# Mixin древовидной структуры
class TreeMixin(BaseMixin):
    code = models.CharField(max_length=180)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, 
        blank=True, null=True
    )

    class Meta:
        abstract = True
        ordering = ["tree_id", "lft"]

    class MPTTMeta:
        order_insertion_by = ["title"]


# Страховая компания
class Insurance(BaseMixin):
    pass


# Страховщик
class Insurer(BaseMixin):
    pass


# Услуги
class Service(MPTTModel, TreeMixin):
    pass


# МКБ-10
class ICD(MPTTModel, TreeMixin):
    pass