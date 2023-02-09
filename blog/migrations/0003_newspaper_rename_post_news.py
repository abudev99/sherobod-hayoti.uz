# Generated by Django 4.1.6 on 2023-02-06 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newspaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('photo', models.FileField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Post',
            new_name='News',
        ),
    ]