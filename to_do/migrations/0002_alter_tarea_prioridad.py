# Generated by Django 3.2.14 on 2022-11-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.IntegerField(choices=[(1, 'Urgentes e importantes'), (2, 'Urgentes'), (3, 'Importantes'), (4, 'Ni urgentes ni importantes (Delegar)')], default=1),
        ),
    ]
