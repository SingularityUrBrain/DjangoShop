# Generated by Django 2.1.7 on 2019-04-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20190406_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcharacteristics',
            name='total_money',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='shopcharacteristics',
            name='total_usage_of_coupons',
            field=models.PositiveIntegerField(default=0),
        ),
    ]