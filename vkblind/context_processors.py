from vkblind.user_settings.models import UserSettings


def get_user_settings(request):
    user_params = {
        'font_size': 'L',
        'color_scheme': 'black'
    }
    if request.user.is_authenticated():
        try:
            settings = UserSettings.objects.get(user=request.user)
            user_params['font_size'] = settings.font_size
            user_params['color_scheme'] = settings.color_scheme
        except UserSettings.DoesNotExist:
            pass
    return user_params


def user_settings(request):
    return {
        'user_settings': get_user_settings(request)
    }
