# Generated by Django 3.0.4 on 2021-05-01 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_category_des'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='des',
            new_name='desc',
        ),
    ]