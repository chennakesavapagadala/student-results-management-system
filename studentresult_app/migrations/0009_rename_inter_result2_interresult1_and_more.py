# Generated by Django 4.2.3 on 2023-09-29 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentresult_app', '0008_delete_btech_result4'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='inter_result2',
            new_name='InterResult1',
        ),
        migrations.RenameModel(
            old_name='inter_result1',
            new_name='InterResult2',
        ),
    ]
