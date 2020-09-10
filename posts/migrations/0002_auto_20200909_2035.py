# Generated by Django 3.1.1 on 2020-09-09 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['postDateCreate']},
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postDateCreate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='dateOfCreate'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postDateLastRefresh',
            field=models.DateTimeField(auto_now=True, verbose_name='dateOfRefresh'),
        ),
        migrations.AlterField(
            model_name='post',
            name='postDatePublication',
            field=models.DateTimeField(blank=True, null=True, verbose_name='dateOfPub'),
        ),
    ]
