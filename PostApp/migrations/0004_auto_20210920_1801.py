# Generated by Django 3.2.7 on 2021-09-20 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('PostApp', '0003_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='category_slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
