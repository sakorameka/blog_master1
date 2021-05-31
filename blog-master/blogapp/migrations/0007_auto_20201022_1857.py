# Generated by Django 3.0.7 on 2020-10-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='next_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next', to='blogapp.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='prev_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previous', to='blogapp.Post'),
        ),
    ]
