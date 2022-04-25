# Generated by Django 4.0.3 on 2022-04-25 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hikers_haven', '0004_post_comments_post_pinned_post_user_id_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='topic',
            name='f_name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hikers_haven.forum'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comm_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comm_on',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='hikers_haven.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='New Post', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='topic',
            name='label',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='topic',
            name='posts',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='hikers_haven.post'),
        ),
    ]
