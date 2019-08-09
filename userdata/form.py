from django import forms
from userdata.models import Song_table


class Song_all(forms.ModelForm):

    class Meta:

        model = Song_table  # class name in the models.py of database
        fields = '__all__'

        # fields = ('clg_name', 'clg_email')
