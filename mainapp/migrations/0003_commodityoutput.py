# Generated by Django 3.0.3 on 2020-02-16 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20191012_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommodityOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Commodity')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodity_output_parent', to='mainapp.Commodity')),
            ],
        ),
    ]