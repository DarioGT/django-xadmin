

from xadmin.plugins.batch import BatchChangeAction


class IDCAdmin(object):
    list_display = ('name', 'description', 'create_time')
    list_display_links = ( 'name', )

    wizard_form_list = [
        ('First\'s Form', ('name', 'description')),
        ('Second Form', ('contact', 'telphone', 'address')),
        ('Thread Form', ('customer_id',))
    ]

    search_fields = ['name']
    relfield_style = 'fk-ajax'
    reversion_enable = True

    actions = [BatchChangeAction, ]
    batch_fields = ('contact', 'create_time')

