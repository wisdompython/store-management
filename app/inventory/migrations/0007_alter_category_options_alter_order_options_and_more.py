# Generated by Django 4.0.1 on 2024-07-25 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_products_date_added'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date']},
        ),
        migrations.AlterModelOptions(
            name='ordereditem',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-id']},
        ),
    ]