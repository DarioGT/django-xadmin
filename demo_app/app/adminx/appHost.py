# -*- coding: utf-8 -*-

from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side
from xadmin.plugins.inline import Inline

from app.models import MaintainLog
from inlines import MaintainInline


data_charts = {
        "host_service_type_counts": {
            'title': "Host service type count",
            "x-field": "service_type",
            "y-field": ("service_type", ),
            "option": {
                "series": {
                    "bars": {
                        "align": "center",
                        "barWidth": 0.8,
                        'show': True
                    }
                },
                "xaxis": {
                    "aggregate": "count",
                    "mode": "categories"
                },
            },
        },
    }


class HostAdmin(object):
    pass 

class HostAdminBase(object):
    save_as = True
    
    def open_web(self, instance):
        return "<a href='http://%s' target='_blank'>Open</a>" % instance.ip
    open_web.short_description = "Acts"
    open_web.allow_tags = True
    open_web.is_column = True


    list_display = ('name', 'idc', 'guarantee_date', 'service_type', 'status', 'open_web', 'description')
    list_filter = ['idc', 'guarantee_date', 'status', 'brand', 'model', 'cpu', 'core_num', 'hard_disk', 'memory', 'service_type']

    list_display_links = ('name',)


    style_fields = {'system': "radio-inline", }

    search_fields = ['name', 'ip', 'description']

    list_bookmarks = [{
          'title': "Need Guarantee",
          'query': {
              'status__exact': 2
          },
          'order': ('-guarantee_date', ),
          'cols': ('brand', 'guarantee_date', 'service_type')
      }]


    raw_id_fields = ('idc',)
    show_detail_fields = ('idc',)

    list_editable = ('name', 'idc', 'guarantee_date', 'service_type', 'description')

    aggregate_fields = {"guarantee_date": "min"}


    form_layout = (
        Main(
            TabHolder(
                Tab('Comm Fields',
                    Fieldset('Company data',
                             'name', 'idc',
                             description="some comm fields, required"
                             ),
                    Inline(MaintainLog),
                    ),
                Tab('Extend Fields',
                    Fieldset('Contact details',
                             'service_type',
                             Row('brand', 'model'),
                             Row('cpu', 'core_num'),
                             Row( AppendedText( 'hard_disk', 'G'), 
                                  AppendedText('memory', "G")
                                  ),
                             'guarantee_date'
                             ),
                    ),
            ),
        ),
        Side(
            Fieldset('Status data',
                     'status', 'ssh_port', 'ip'
                     ),
        )
    )
    inlines = [MaintainInline]
    reversion_enable = True
    
