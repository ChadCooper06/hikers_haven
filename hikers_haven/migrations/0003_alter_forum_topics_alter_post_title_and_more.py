# Generated by Django 4.0.3 on 2022-04-22 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hikers_haven', '0002_post_alter_forum_id_topic_alter_forum_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='topics',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hikers_haven.topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='label',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hikers_haven.forum'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='posts',
            field=models.CharField(max_length=250),
        ),
    ]
