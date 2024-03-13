# Generated by Django 4.2.11 on 2024-03-12 02:56

from django.db import migrations, models
import posts.validators


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_user_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='student_id',
        ),
        migrations.AddField(
            model_name='user',
            name='student_number',
            field=models.CharField(error_messages={'unique': '이미 등록된 학번입니다'}, max_length=10, null=True, unique=True, validators=[posts.validators.validate_no_special_characters]),
        ),
    ]
