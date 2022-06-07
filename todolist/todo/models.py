from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'catid': self.pk})

    class Meta:
        verbose_name = ("Категория")
        verbose_name_plural = ("Категории")


class Task(models.Model):
    task = models.CharField(max_length=100, verbose_name="Задача")
    content = models.TextField(blank=True, max_length=300, verbose_name='Информация о задаче')
    data_todo = models.DateField(blank=True, verbose_name='Дата выполнения')
    is_done = models.BooleanField(default=False, verbose_name="Сделано")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, verbose_name="Категория")

    def __str__(self):
        return self.task

    def get_absolute_url(self):
        return reverse('task', kwargs={'taskid': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


