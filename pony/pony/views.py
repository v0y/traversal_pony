from pyramid.view import view_config

from models import Group, Kind, Pony
from pony.db import DBSession


@view_config(name='mv1', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pony'}


@view_config(name='all', context=Kind, renderer='templates/mytemplate.pt')
def my_view_k(request):
    return {'project': 'szystkie kindy'}


@view_config(name='all', context=Pony, renderer='templates/mytemplate.pt')
def my_view_p(request):
    return {'project': 'szystkie koniki'}


@view_config(name='all', context=Group, renderer='templates/mytemplate.pt')
def my_view_g(request):
    return {'project': 'szystkie koniki grupy {}'.format(request.context.name)}


@view_config(context=Group, renderer='templates/mytemplate.pt')
def my_view2(request):
    return {'project': [p.name for p in request.context.ponies]}


@view_config(context=Kind, renderer='templates/mytemplate.pt')
def my_view3(request):
    return {'project': [p.name for p in request.context.ponies]}


@view_config(name='all', renderer='templates/mytemplate.pt')
def my_view666(request):
    return {'project': 'szystkie blble {}'.format(request.context)}


@view_config(context=Pony, renderer='templates/mytemplate.pt')
def widok_konika(request):
    return {'project': 'widok konika: {}, {}, {}'.format(
        request.context.name,
        request.context.colour,
        request.context.kind.name
    )}


class GetGroups(object):
    def __init__(self):
        self.all = DBSession.query(Group)

    def __getitem__(self, item):
        return self.all.filter(Group.name==item).one()


class GetKinds(object):
    def __init__(self):
        self.all = DBSession.query(Kind)

    def __getitem__(self, item):
        return self.all.filter(Kind.name==item).one()


# def get_kinds():
#     kinds_dict = {}
#     for k in DBSession.query(Kind).all():
#         kinds_dict[k.name] = k
#     return kinds_dict


def get_root(request):
    return {
        'group': GetGroups(),
        'kind': GetKinds(),
    }
