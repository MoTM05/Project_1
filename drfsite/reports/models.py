from django.contrib.auth.models import User
from django.db import models



class Orders(models.Model):
    Number = models.CharField(max_length=50, verbose_name='Номер заказа')
    RD_for_method = models.CharField(max_length=255, verbose_name='НД на метод')
    RD_for_sample = models.CharField(max_length=255, verbose_name='НД на образец')
    Analyzed_Indicator = models.CharField(max_length=100, verbose_name='Анализируемый показатель')
    Standard = models.CharField(max_length=30, verbose_name='Норма')
    user = models.ForeignKey(User, verbose_name='Сотрудник', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Number


class Equipment(models.Model):
    Characteristic = models.CharField(max_length=50, verbose_name='Наименовение определяемых характеристик')
    Name = models.CharField(max_length=100, verbose_name='Наименование СИ, тип(марка), заводской номер')
    Number_of_reg = models.CharField(max_length=20, verbose_name='Регистрационный номер в ФИФ')
    Manufacturer = models.CharField(max_length=100, verbose_name='Изготовитель (страна, организация, год выпуска)')
    Year_of_exp = models.CharField(max_length=40, verbose_name='Год ввода в эксплуатацию, инвентарный номер')
    Measuring_range = models.CharField(max_length=20, verbose_name='Диапазон измерений')
    Accuracy_class = models.CharField(max_length=30, verbose_name='Класс точности, погрешности')
    Calibration_Certificate = models.CharField(max_length=255, verbose_name='Сертификат о калибровке СИ (номер, дата, срок действия)')
    Ownership = models.CharField(max_length=100, verbose_name='Право собственности')
    Installation_location = models.CharField(max_length=100, verbose_name='Место установки или хранения')
    Char = models.ForeignKey('Characteristic', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Сотрудник', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Characteristic


class Characteristic(models.Model):
    Char = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.Char


class Reports(models.Model):
    Medicinal_product = models.CharField(max_length=255, verbose_name='Наименование ЛС')
    RD_for_method = models.CharField(max_length=255, verbose_name='НД на метод')
    RD_for_sample = models.CharField(max_length=255, verbose_name='НД на образец')
    Analyzed_Indicator = models.CharField(max_length=100, verbose_name='Анализируемый показатель')
    Standard = models.CharField(max_length=30, verbose_name='Норма по спецификации в НД')
    Test_procedure = models.CharField(max_length=255,verbose_name='Методика испытаний')
    Reagents_used = models.CharField(max_length=255, verbose_name='Используемые реагенты')
    Equipment_used = models.CharField(max_length=255, verbose_name='Используемое оборудование')
    Measurements = models.ImageField(max_length=255, verbose_name='Измерения')
    Formula = models.CharField(max_length=255, verbose_name='Формула')
    Arguments = models.CharField(max_length=30, verbose_name='Аргументы')
    Calculations = models.CharField(max_length=100, verbose_name='Расчеты')
    Analysis_number = models.CharField(max_length=30, verbose_name='Номер аналлиза')
    Analysis_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время анализа')
    user = models.ForeignKey(User, verbose_name='Сотрудник', on_delete=models.DO_NOTHING)


