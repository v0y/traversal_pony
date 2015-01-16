import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars
from pony.db import (
    Base,
    DBSession,
)
from pony.models import Group, Kind


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        DBSession.add(Kind(name='earth_ponies'))
        DBSession.add(Kind(name='pegasis'))
        DBSession.add(Kind(name='unicorns'))
        DBSession.add(Group(name='stallion'))
        DBSession.add(Group(name='filly'))
        DBSession.add(Group(name='mare'))
        DBSession.add(Group(name='colt'))

