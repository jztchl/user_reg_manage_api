# Generated by Django 4.0.6 on 2022-07-10 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapi', '0006_users_birth_date_alter_users_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]