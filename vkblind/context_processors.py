from vkblind.models import Settings

def get_settings(request):
    try:
        settings = Settings.objects.get(user=request.user)
        font_size = settings.font_size
        color_scheme = settings.color_scheme
    except:
        font_size = 'L'
        color_scheme = 'black'
    return {
        'font_size': font_size,
        'color_scheme': color_scheme
    }


def settings(request):
    return {
        'settings': get_settings(request)
    }
