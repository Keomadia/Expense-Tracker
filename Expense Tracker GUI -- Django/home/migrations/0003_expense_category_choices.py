# Generated by Django 5.1.3 on 2024-12-26 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_expense_id_expense_srno'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='category_choices',
            field=models.JSONField(default=list),
        ),
    ]
