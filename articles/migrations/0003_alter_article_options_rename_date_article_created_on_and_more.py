# Generated by Django 5.0.6 on 2024-05-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date',
            new_name='created_on',
        ),
        migrations.AddField(
            model_name='article',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
