# Generated by Django 4.0.4 on 2022-07-03 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='blog_title',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comments',
        ),
    ]