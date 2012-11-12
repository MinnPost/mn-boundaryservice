#!/usr/bin/env python
import os
from django.core.management import setup_environ
import settings

setup_environ(settings)

from django.conf import settings
from django.contrib.gis.gdal import CoordTransform, DataSource, OGRGeometry, OGRGeomType
from django.core.management.base import BaseCommand
from django.db import connections, DEFAULT_DB_ALIAS, transaction
from boundaryservice.models import BoundarySet, Boundary

# A simple way to list the sets

for bs in BoundarySet.objects.all():
  print '%s: %s' % (bs.id, bs.name)
  