

class HostGroupAdmin(object):
    list_display = ('name', 'description')
    list_display_links = ('name',)

    search_fields = ['name']
    style_fields = {'hosts': 'm2m_transfer'}

