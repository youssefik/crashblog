# Generated by Django 5.0.3 on 2024-03-31 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options_post_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post',
            new_name='category',
        ),
    ]
