#!/usr/bin/env python
import os
import sys
from django.core.management import setup_environ
import settings

setup_environ(settings)

from django.conf import settings
from django.contrib.gis.gdal import CoordTransform, DataSource, OGRGeometry, OGRGeomType
from django.core.management.base import BaseCommand
from django.db import connections, DEFAULT_DB_ALIAS, transaction
from boundaryservice.models import BoundarySet, Boundary

# A simple way to remove a boundary set and associated data

if sys.argv[1]:
  bs = BoundarySet.objects.get(id = sys.argv[1])
  confirm = raw_input('Found set (' + bs.name + ').  Delete [Y/n]: ')
  if confirm == 'Y':
    print 'Deleting...'
    bs.delete()  