# Generated by Django 4.2.6 on 2023-10-26 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fkylo-the-shiba-inu-on-instagram-eh-whats-up-doc-in-2021--659918151684833434%2F&psig=AOvVaw2P_MyJIUXo0T4QriU4o0-P&ust=1698397083917000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCPiT5qisk4IDFQAAAAAdAAAAABAZ', max_length=500),
        ),
    ]
