# Generated by Django 2.2.6 on 2019-10-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('minor_unit_plural', models.CharField(max_length=50, verbose_name='minor unit (plural)')),
            ],
        ),
    ]