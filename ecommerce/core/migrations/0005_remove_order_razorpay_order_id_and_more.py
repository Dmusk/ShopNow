# Generated by Django 5.0.7 on 2024-07-25 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_order_razorpay_order_id_order_razorpay_payment_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='razorpay_order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='razorpay_signature',
        ),
    ]
