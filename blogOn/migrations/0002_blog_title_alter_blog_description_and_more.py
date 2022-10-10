# Generated by Django 4.0.2 on 2022-10-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogOn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
    ]
