# Generated by Django 5.1.4 on 2024-12-25 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['id'], 'verbose_name': 'پست', 'verbose_name_plural': 'پست ها'},
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]