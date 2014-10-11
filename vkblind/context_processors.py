from vkblind.user_settings.models import UserSettings


def get_user_settings(request):
    try:
        settings = UserSettings.objects.get(user=request.user)
        font_size = settings.font_size
        color_scheme = settings.color_scheme
    except UserSettings.DoesNotExist:
        font_size = 'L'
        color_scheme = 'black'
    return {
        'font_size': font_size,
        'color_scheme': color_scheme
    }


def user_settings(request):
    return {
        'user_settings': get_user_settings(request)
    }
