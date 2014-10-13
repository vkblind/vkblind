# coding: utf-8

from annoying.decorators import render_to
from django.contrib.auth import logout as logout_user
from django.shortcuts import redirect
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

    account = vkapi.users.get(user_ids=vkuser, fields='sex, '
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


    monthsList = [
        u'января',
        u'февраля',
        u'марта',
        u'апреля',
        u'мая',
        u'июня',
        u'июля',
        u'августа',
        u'сентября',
        u'октября',
        u'ноября',
        u'декабря'
    ]

    try:
        bdate = account[0]['bdate'].split('.')
        bday = bdate[0]
        bmonth = monthsList[int(bdate[1]) - 1]
    except:
        return {'account': account[0]}

    try:
        byear = bdate[2] + u' г.'
    except:
        byear = ''

    string_bdate = bday + ' ' + bmonth + ' ' + byear

    account[0]['bdate'] = string_bdate
    return {'account': account[0]}


def logout(request):
    logout_user(request)
    return redirect('/')


@render_to('help_page.html')
def help_page(request):
    return {}
