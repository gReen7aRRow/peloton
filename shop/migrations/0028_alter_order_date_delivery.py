# Generated by Django 4.1.7 on 2023-04-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_review_options_alter_order_date_delivery_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_delivery',
            field=models.CharField(default=1, max_length=40, verbose_name='Время доставки'),
            preserve_default=False,
        ),
    ]
