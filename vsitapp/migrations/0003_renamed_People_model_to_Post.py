# Generated by Django 2.0.2 on 2018-03-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vsitapp', '0002_test_migration'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='people',
            new_name='Post',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('name',)},
        ),
    ]
