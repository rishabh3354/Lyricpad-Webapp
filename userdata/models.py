from django.db import models


class Song_table(models.Model):

    song_name = models.CharField(max_length=150)
    song_artist = models.CharField(max_length=150)
    song_url = models.CharField(max_length=300)
    user_email = models.CharField(max_length=150)

    class Meta:

        db_table = 'user_history'
        unique_together = ["song_name", "song_artist", "user_email"]



