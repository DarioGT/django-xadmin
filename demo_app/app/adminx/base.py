import xadmin

from app.models import IDC, Host

class MainDashboard(object):
    widgets = []


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    global_search_models = [Host, IDC]
    global_models_icon = {
        Host: 'laptop', IDC: 'cloud'
    }
