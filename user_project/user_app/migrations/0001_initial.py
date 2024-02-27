# Generated by Django 3.2.13 on 2024-02-13 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=50)),
                ('mobile_no', models.CharField(max_length=100)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'user_register',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='user_app.userregister')),
            ],
            options={
                'db_table': 'user_role',
            },
        ),
    ]