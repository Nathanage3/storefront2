# Generated by Django 4.2.13 on 2024-07-10 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='store.order'),
        ),
    ]
