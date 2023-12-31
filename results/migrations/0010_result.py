# Generated by Django 3.2 on 2023-11-10 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0009_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_number', models.CharField(max_length=50)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='results.party')),
            ],
        ),
    ]
