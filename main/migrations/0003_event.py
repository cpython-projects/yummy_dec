# Generated by Django 5.1.4 on 2024-12-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gallery_alter_category_options_alter_dish_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('short_desc', models.TextField(blank=True, max_length=500)),
                ('desc', models.TextField(blank=True, max_length=2000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('photo', models.ImageField(blank=True, upload_to='images/events/')),
                ('date_time', models.DateTimeField(blank=True, null=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'ordering': ('date_time',),
                'unique_together': {('id', 'slug')},
            },
        ),
    ]