# Generated by Django 4.2.4 on 2023-09-06 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='ATL.jpeg', upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default='ATL.jpeg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to=''),
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='music_player.album'),
        ),
    ]
