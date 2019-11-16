# Generated by Django 3.0b1 on 2019-11-14 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tof', '0002_auto_20191113_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='translations',
            name='lang',
            field=models.ForeignKey(limit_choices_to=models.Q(is_active=True), on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='tof.Language'),
        ),
    ]