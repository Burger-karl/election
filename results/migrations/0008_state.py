# Generated by Django 3.2 on 2023-11-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_pollingunit'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.IntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'states',
            },
        ),
    ]
