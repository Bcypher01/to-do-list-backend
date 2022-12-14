# Generated by Django 3.2.7 on 2022-10-02 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['created']},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated',
        ),
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='progress',
            field=models.PositiveSmallIntegerField(blank=True, default=1, null=True),
        ),
    ]
