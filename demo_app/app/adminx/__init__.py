# -*- coding: utf-8 -*-

import xadmin

from xadmin import views
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline
from xadmin.plugins.batch import BatchChangeAction

from app.models import IDC, Host, MaintainLog, HostGroup, AccessRecord


from base import MainDashboard, BaseSetting, GlobalSetting
xadmin.site.register(views.website.IndexView, MainDashboard)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)

from appIDC import IDCAdmin
xadmin.site.register(IDC, IDCAdmin)


from appHost import HostAdmin
xadmin.site.register(Host, HostAdmin)


from appHostGroup import HostGroupAdmin
xadmin.site.register(HostGroup, HostGroupAdmin)


from appMaintainLog import MaintainLogAdmin
xadmin.site.register(MaintainLog, MaintainLogAdmin)


from appAccessRecord import AccessRecordAdmin
xadmin.site.register(AccessRecord, AccessRecordAdmin)

