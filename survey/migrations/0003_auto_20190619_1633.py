# Generated by Django 2.2.2 on 2019-06-19 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190617_0137'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_test',
            new_name='question_text',
        ),
    ]
