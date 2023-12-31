# Generated by Django 3.2 on 2023-11-09 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncedLGAResult',
            fields=[
                ('result_id', models.AutoField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=50)),
                ('party_abbreviation', models.CharField(max_length=4)),
                ('party_score', models.IntegerField()),
                ('entered_by_user', models.CharField(max_length=50)),
                ('date_entered', models.DateTimeField()),
                ('user_ip_address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'announced_lga_results',
            },
        ),
    ]
