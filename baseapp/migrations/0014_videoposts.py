# Generated by Django 3.2.8 on 2021-12-13 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0013_auto_20210423_0321'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('video_file', models.FileField(upload_to='videos/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('MemberSelected', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='baseapp.member')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
    ]
