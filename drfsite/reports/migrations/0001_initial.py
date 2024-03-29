# Generated by Django 4.2.7 on 2023-11-13 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Char', models.CharField(db_index=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=50, verbose_name='Номер заказа')),
                ('RD_for_method', models.CharField(max_length=255, verbose_name='НД на метод')),
                ('RD_for_sample', models.CharField(max_length=255, verbose_name='НД на образец')),
                ('Analyzed_Indicator', models.CharField(max_length=100, verbose_name='Анализируемый показатель')),
                ('Standard', models.CharField(max_length=30, verbose_name='Норма')),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Characteristic', models.CharField(max_length=50, verbose_name='Наименовение определяемых характеристик')),
                ('Name', models.CharField(max_length=100, verbose_name='Наименование СИ, тип(марка), заводской номер')),
                ('Number_of_reg', models.CharField(max_length=20, verbose_name='Регистрационный номер в ФИФ')),
                ('Manufacturer', models.CharField(max_length=100, verbose_name='Изготовитель (страна, организация, год выпуска)')),
                ('Year_of_exp', models.CharField(max_length=40, verbose_name='Год ввода в эксплуатацию, инвентарный номер')),
                ('Measuring_range', models.CharField(max_length=20, verbose_name='Диапазон измерений')),
                ('Accuracy_class', models.CharField(max_length=30, verbose_name='Класс точности, погрешности')),
                ('Calibration_Certificate', models.CharField(max_length=255, verbose_name='Сертификат о калибровке СИ (номер, дата, срок действия)')),
                ('Ownership', models.CharField(max_length=100, verbose_name='Право собственности')),
                ('Installation_location', models.CharField(max_length=100, verbose_name='Место установки или хранения')),
                ('Char', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reports.characteristic')),
            ],
        ),
    ]
