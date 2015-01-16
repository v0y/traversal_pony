from pyramid.view import view_config

from models import Group, Kind, Pony


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pony'}
