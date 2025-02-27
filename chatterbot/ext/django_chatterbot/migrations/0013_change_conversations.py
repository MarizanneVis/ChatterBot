# Generated by Django 1.11 on 2018-09-13 01:01
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_chatterbot', '0012_statement_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversation',
            name='responses',
        ),
        migrations.RemoveField(
            model_name='response',
            name='response',
        ),
        migrations.RemoveField(
            model_name='response',
            name='statement',
        ),
        migrations.AddField(
            model_name='statement',
            name='conversation',
            field=models.CharField(default='default', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statement',
            name='in_response_to',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='text',
            field=models.CharField(max_length=2000),
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
