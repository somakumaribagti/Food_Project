# Generated by Django 5.0.6 on 2024-08-04 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home_App', '0005_alter_items_price_alter_items_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AboutUs',
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.RemoveField(
            model_name='items',
            name='Category',
        ),
        migrations.DeleteModel(
            name='ItemList',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
    ]
