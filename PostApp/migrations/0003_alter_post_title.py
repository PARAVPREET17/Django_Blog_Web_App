# Generated by Django 3.2.7 on 2021-09-19 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostApp', '0002_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
