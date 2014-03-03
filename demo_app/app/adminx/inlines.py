
from app.models import MaintainLog

class MaintainInline(object):
    model = MaintainLog
    extra = 1
    style = 'accordion'
