# Generated by Django 5.1 on 2024-08-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astroapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_form',
            name='email',
            field=models.EmailField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='lastname',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='message',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='subject',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
