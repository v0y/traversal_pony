from pyramid.view import view_config
from sqlalchemy.orm.exc import NoResultFound

from models import Group, Kind, Pony
from pony.db import DBSession


class GetGroups(object):
    def __init__(self, request):
        self.request = request
        self.all = DBSession.query(Group)

    def __getitem__(self, item):
        try:
            return self.all.filter(Group.name == item).one()
        except NoResultFound:
            raise KeyError


class GetKinds(object):
    def __init__(self, request):
        self.request = request
        self.all = DBSession.query(Kind)

    def __getitem__(self, item):
        try:
            return self.all.filter(Kind.name == item).one()
        except NoResultFound:
            raise KeyError

    @property
    def objects(self):
        return self.all.all()


class GetRoot(object):
    def __init__(self, request):
        self.request = request

    def __getitem__(self, item):
        return {
            'group': GetGroups,
            'kind': GetKinds,
        }[item](self.request)


# def get_kinds():
# kinds_dict = {}
#     for k in DBSession.query(Kind).all():
#         kinds_dict[k.name] = k
#     return kinds_dict

# def get_root(request):
#     return {
#         'group': GetGroups(),
#         'kind': GetKinds(),
#     }

@view_config(context=GetKinds, renderer='templates/mytemplate.pt')
def my_view3(request):
    return {'project': [p.name for p in request.context.ponies]}



@view_config(name='mv1', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pony'}


@view_config(name='all', context=GetKinds, renderer='templates/mytemplate.pt')
def my_view_k(request):
    return {'project': 'szystkie kindy: {}'.format(
        [k.name for k in request.context.objects])}


@view_config(name='all', context=Pony, renderer='templates/mytemplate.pt')
def my_view_p(request):
    return {'project': 'szystkie koniki'}


@view_config(name='all', context=Group, renderer='templates/mytemplate.pt')
def my_view_g(request):
    return {'project': 'szystkie koniki grupy {}'.format(request.context.name)}


@view_config(context=Group, renderer='templates/mytemplate.pt')
def my_view2(request):
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
