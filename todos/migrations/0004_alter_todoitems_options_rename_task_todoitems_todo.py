# Generated by Django 5.1.4 on 2025-01-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_remove_todoitems_todo_delete_todo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todoitems',
            options={'ordering': ['-date_created']},
        ),
        migrations.RenameField(
            model_name='todoitems',
            old_name='task',
            new_name='todo',
        ),
    ]
