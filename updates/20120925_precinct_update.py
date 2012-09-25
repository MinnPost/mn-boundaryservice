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

# This switches around a couple precincts in Minnetonka that were
# mixed up in a previous version of 2012-mn_sos/vtd2012_primary_rev20120720

# 270532120, 270532125
A = Boundary.objects.get(external_id='270532120')
B = Boundary.objects.get(external_id='270532125')

# do the ol' switcheroo
A.shape, B.shape = B.shape, A.shape
A.simple_shape, B.simple_shape = B.simple_shape, A.simple_shape
A.centroid, B.centroid = B.centroid, A.centroid

if (A.shape != B.shape):
  print "Saving ..."
  A.save()
  B.save()
else:
  print "Not saving ..."