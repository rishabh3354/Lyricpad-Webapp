from django.shortcuts import render,redirect
from userdata.form import Song_all
from userdata.models import Song_table
from django.db.models import Q




def create(request):

    form = Song_all()
    if request.method =='POST':
        form = Song_all(request.POST)
        if form.is_valid():

            song = Song_table()
            song.song_id = form.cleaned_data['clg_name']
            song.song_name = form.cleaned_data['clg_email']
            song.song_artist = form.cleaned_data['clg_address']
            song.song_url = form.cleaned_data['clg_address']
            song.save()
            # return redirect(index)

    return render(request, 'create.html', {'form': form})



def mylyrics(request):

    user_history = {"a":"b"}

    if request.user.username:

        user_history = Song_table.objects.filter(Q(user_email=request.user.username))
    return render(request, 'my_lyrics.html', {'user_history': user_history})



def delete(request):

    id = request.GET['id']
    data = Song_table.objects.get(id=id)
    data.delete()
    return redirect(mylyrics)



'''

def update(request):

    id = request.GET['id']
    data = College.objects.get(id=id)    #fetch one , fetch one etc....

    form = CollegeForm(instance=data)  #instance=data = gives previes data pre filled inside form
    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=data)
        if form.is_valid():
            clg = College()
            clg.id = id      #very must otherwise duplicate will be created
            clg.clg_name = form.cleaned_data['clg_name']
            clg.clg_email = form.cleaned_data['clg_email']
            clg.clg_address = form.cleaned_data['clg_address']
            clg.save()
            return redirect(index)

    return render(request, 'update.html', {'form': form})





def index(request):

    #select * from  college
    resultset = College.objects.all()
    # resultset = College.objects.filter().values('id','clg_name') # if we wat to filter particular column

    return render(request, 'index.html', {'data': resultset})




def delete(request):

    id = request.GET['id']
    data = College.objects.get(id=id)
    data.delete()
    return redirect(index)




def view(request):

    id = request.GET['id']
    resultset = College.objects.get(id=id)

    return render(request, 'view.html', {'data': resultset})'''
