# Generated by Django 3.2 on 2022-10-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eithers', '0005_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='either',
            name='issue_a',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='either',
            name='issue_b',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='either',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
