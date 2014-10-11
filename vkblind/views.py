# coding: utf-8

from annoying.decorators import render_to
from django.core.cache import cache
from django.contrib.auth import logout as logout_user
from django.shortcuts import resolve_url, redirect
from vkblind.models import Settings
from vkblind.decorators import vk_api
import pprintpp
import vk

@vk_api
@render_to('index.html')
def index(request):
    try:
        vkapi = vk.API(access_token=request.user.social_auth.get().tokens)

        groups = vkapi.groups.get()
        pprintpp.pprint(groups)

        wall = vkapi.wall.get(owner_id=-groups['items'][3])
        pprintpp.pprint(wall)
    except:
        return {}
    return {}


@render_to('accounts/login.html')
def login(request):
    return {}

@render_to('profile.html')
def profile(request, vkuser):
    uid = request.user.social_auth.get().uid
    vkapi = vk.API(access_token=request.user.social_auth.get().tokens)

    # использую  users.get, а не account.getProfileInfo
    # потому что второй отчего-то только для стэндэлона
    # alexger

    account = vkapi.users.get(user_ids=uid, fields='sex, '
                                                   'bdate, '
                                                   'city, '
                                                   'country, '
                                                   'online, '
                                                   'online_mobile, '
                                                   'domain, '
                                                   'home_town, '
                                                   'has_mobile, '
                                                   'contacts, '
                                                   'connections, '
                                                   'site, '
                                                   'education, '
                                                   'universities, '
                                                   'personal, '
                                                   'schools, '
                                                   'can_post, '
                                                   'can_see_all_posts, '
                                                   'can_see_audio, '
                                                   'can_write_private_message, '
                                                   'status, '
                                                   'last_seen, '
                                                   'common_count, '
                                                   'relation, '
                                                   'relatives, '
                                                   'counters, '
                                                   'screen_name,'
                                                   'maiden_name, '
                                                   'timezone, '
                                                   'occupation,'
                                                   'activities, '
                                                   'interests, '
                                                   'music, '
                                                   'movies, '
                                                   'tv, '
                                                   'books, '
                                                   'games, '
                                                   'about, '
                                                   'quotes')

    return {'account': account[0]}

@render_to('settings.html')
def settings(request):
    return {}

def save_settings(request):
    user = request.user
    try:
       settings = Settings.objects.get(user=user)
    except:
       settings = Settings()
    settings.user = user
    settings.font_size = request.POST['font_size']
    settings.color_scheme = request.POST['color_scheme']
    settings.save()
    return redirect('../')

def logout(request):
    logout_user(request)
    return redirect('/')


@vk_api
@render_to('search.html')
def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        groups = request.vk.groups.search(q=query, count=10)['items']
        return {'groups': groups}
    else:
        return {'groups': []}
