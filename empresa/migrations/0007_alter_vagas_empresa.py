# Generated by Django 4.1.3 on 2022-12-21 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_vagas_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vagas',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
