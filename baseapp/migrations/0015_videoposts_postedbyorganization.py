# Generated by Django 3.2.8 on 2021-12-15 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0014_videoposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='videoposts',
            name='postedByOrganization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.organization'),
        ),
    ]
