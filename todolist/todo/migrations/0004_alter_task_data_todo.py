# Generated by Django 4.0.2 on 2022-03-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_task_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='data_todo',
            field=models.DateField(blank=True, verbose_name='Дата выполнения'),
        ),
    ]