# Generated by Django 3.1.5 on 2021-05-09 09:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0011_auto_20210508_1235'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contactus1',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='upload',
            name='city',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='email',
            field=models.EmailField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='state',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='street',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='whatsappphone',
            field=phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, region=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='zip',
            field=models.CharField(default=None, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload',
            name='filepath',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
