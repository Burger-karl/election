# Generated by Django 3.2 on 2023-11-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_announcedlgaresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncedPUResult',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('polling_unit_uniqueid', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_pu_results',
            },
        ),
    ]
