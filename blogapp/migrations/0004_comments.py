# Generated by Django 2.2 on 2019-04-15 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_encryptedpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('randomText', models.TextField()),
                ('frequencyOfAnalysis', models.TextField()),
                ('standardDeviation', models.CharField(max_length=300)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
