# Generated by Django 4.0.2 on 2022-02-04 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_news_options_alter_news_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
