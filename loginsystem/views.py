from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from loginsystem.forms import LoginForm
from loginsystem.forms import UserCreateForm
from scrap.script import getlist
from scrap.script2 import getlyrics
from loginsystem.forms import ContactForm
from loginsystem.models import Contact
from userdata.form import Song_all
from userdata.models import Song_table
from django.http import HttpResponse
from django.db import IntegrityError



def signin(request):   #login name is not same as inbuild login function

    if request.user.username:
        return redirect(home)

    message = ''
    form = LoginForm()
    if request.method =='POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user==None:

                message = "Invalid login details"

            else:
                login(request,user)

                # request.session['city'] = 'Bangalore'     #creating session variable
                # request.session['address'] = 'BTM'          #creatinf session variables

                return redirect(home)

    return render(request, 'signin.html', {'form': form, 'message': message})



def signup(request):

    signup_success = ''

    if request.user.username:
        return redirect(home)

    form = UserCreateForm()
    if request.method=='POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():

            user = User()
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password1'])
            user.save()
            signup_success = 'User successfully Registered'
            return redirect(signin)


    return render(request, 'signup.html', {'form': form, 'signup_success': signup_success})



def home(request):

    search_query = request.GET.get('search', '')
    print(search_query)
    if len(search_query)>0:
        getresult = getlist(search_query)
        print(getresult)
        return render(request, 'home.html', {"results": getresult})

    # data = College.objects.get(id=id)  # fetch one , fetch one etc....

    # form = CollegeForm(instance=data)  # instance=data = gives previes data pre filled inside form
    # if request.method == 'POST':
    #     form = CollegeForm(request.POST, instance=data)
    #     if form.is_valid():
    #         clg = College()
    #         clg.id = id  # very must otherwise duplicate will be created
    #         clg.clg_name = form.cleaned_data['clg_name']
    #         clg.clg_email = form.cleaned_data['clg_email']
    #         clg.clg_address = form.cleaned_data['clg_address']
    #         clg.save()
    #         return redirect(index)
    #
    # return render(request, 'update.html', {'form': form})

    return render(request, 'home.html')



def signout(request):

    logout(request)
    return redirect(signin)


def results(request):

    result_url = request.GET.get('song_url', '')
    result_song = request.GET.get('song_name', '')
    result_artist = request.GET.get('song_artist', '')


    try:
        song = Song_table()
        song.song_name = result_song
        song.song_artist = result_artist
        song.song_url = result_url
        song.user_email = request.user.username
        song.save()

    except IntegrityError as e:
        # return HttpResponse('/contact')
        pass


    get_lyrics_data = getlyrics(result_url)
    print(get_lyrics_data)
    return render(request, 'search_result.html', {
        "lyrics": get_lyrics_data,
        "result_song": result_song,
        "result_artist": result_artist,
    })



def contact(request):

    message = ""
    form_data = ContactForm()
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():

            con = Contact()
            con.name = form_data.cleaned_data['name']
            con.email = form_data.cleaned_data['email']
            con.message = form_data.cleaned_data['message']
            con.save()
            message = "Your message has been successfully submitted"

            # return redirect(index)

    return render(request, 'contact_us.html', {'form_data': form_data, "message_conf":message})


def about(request):

    return render(request, 'about_us.html')

