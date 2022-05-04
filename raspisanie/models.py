from datetime import date

from django.db import models


class Prepod(models.Model):
    full_name = models.CharField("ФИО", max_length=50)

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Group(models.Model):
    group_name = models.CharField("Группа", max_length=20)

    def __str__(self):
        return f"{self.group_name}"

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class Cabinet(models.Model):
    cabinet_name = models.CharField("Кабинет", max_length=20)

    def __str__(self):
        return f"{self.cabinet_name}"

    class Meta:
        verbose_name = "Кабинет"
        verbose_name_plural = "Кабинеты"


class TimeTable(models.Model):
    number = models.PositiveSmallIntegerField("Номер пары", default=1)
    date = models.DateField("День недели", default=date.today)
    prepod = models.ForeignKey(Prepod, verbose_name="Преподаватель", on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.SET_NULL, blank=list, null=True)
    cabinet = models.ForeignKey(Cabinet, verbose_name="Кабинет", on_delete=models.SET_NULL, blank=list, null=True)
    reduction = models.BooleanField("Сокращенка", default=False)

    def __str__(self):
        return f"{self.date} - {self.prepod} - {self.group} - {self.cabinet}"

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
