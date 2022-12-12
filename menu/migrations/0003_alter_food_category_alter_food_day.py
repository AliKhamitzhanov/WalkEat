# Generated by Django 4.1.3 on 2022-12-12 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_food_day_food_fit_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='food', to='menu.category'),
        ),
        migrations.AlterField(
            model_name='food',
            name='day',
            field=models.IntegerField(choices=[(0, 'monday'), (1, 'tuesday'), (2, 'wednesday'), (3, 'thursday'), (4, 'friday'), (5, 'saturday'), (6, 'sunday')], null=True),
        ),
    ]
