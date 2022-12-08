# Generated by Django 4.1.3 on 2022-12-08 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0006_user_payment_alter_user_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('home', models.PositiveIntegerField(default=1)),
                ('flat', models.PositiveIntegerField(default=0)),
                ('floor', models.PositiveIntegerField(default=1)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='reg.addresses'),
        ),
    ]
