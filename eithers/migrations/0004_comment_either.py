# Generated by Django 3.2 on 2022-10-06 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eithers', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='either',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eithers.either'),
            preserve_default=False,
        ),
    ]