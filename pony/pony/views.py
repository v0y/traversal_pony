from pyramid.view import view_config

from models import Group, Kind, Pony
from pony.db import DBSession


@view_config(name='mv1', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pony'}


@view_config(context=Group, renderer='templates/mytemplate.pt')
def my_view2(request):
    return {'project': [p.name for p in request.context.ponies]}


@view_config(context=Kind, renderer='templates/mytemplate.pt')
def my_view3(request):
    return {'project': [p.name for p in request.context.ponies]}


@view_config(context=Pony, renderer='templates/mytemplate.pt')
def widok_konika(request):
    return {'project': 'widok konika: {}, {}, {}'.format(
        request.context.name,
        request.context.colour,
        request.context.kind.name
    )}


def get_groups():
    # return {
    #     'a': {},
    #     'b': {},
    # }
    groups_dict = {}
    for g in DBSession.query(Group).all():
        groups_dict[g.name] = g
    return groups_dict


def get_kinds():
    kinds_dict = {}
    for k in DBSession.query(Kind).all():
        kinds_dict[k.name] = k
    return kinds_dict

def get_root(request):
    return {
        'group': get_groups(),
        'kind': get_kinds(),
    }
