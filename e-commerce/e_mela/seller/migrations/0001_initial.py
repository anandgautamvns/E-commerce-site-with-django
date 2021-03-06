# Generated by Django 2.0.7 on 2018-07-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('name', models.CharField(default='', max_length=60)),
                ('product_category', models.CharField(choices=[('Electronics', 'electronics'), ('Men', 'men'), ('Women', 'women'), ('Kids', 'kids'), ('Furniture', 'furniture'), ('Sports', 'sports'), ('Other', 'other')], max_length=256)),
            ],
            options={
                'verbose_name_plural': 'category_images',
            },
        ),
        migrations.CreateModel(
            name='uploadItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_small', models.FileField(upload_to='')),
                ('image_big', models.FileField(default='', upload_to='')),
                ('price', models.IntegerField()),
                ('product_name', models.CharField(default='', max_length=50)),
                ('discount', models.IntegerField()),
                ('description', models.CharField(default='', max_length=200)),
                ('product_category', models.CharField(choices=[('Electronics', 'electronics'), ('Men', 'men'), ('Women', 'women'), ('Kids', 'kids'), ('Furniture', 'furniture'), ('Sports', 'sports'), ('Other', 'other')], max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
