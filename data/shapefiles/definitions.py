from datetime import date

from boundaryservice import utils

SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    'Minnesota State House districts (2002)': {
        # Path to a shapefile, relative to /data/shapefiles
        'file': 'state-house-districts/2010/tl_2010_27_sldl10/tl_2010_27_sldl10.shp',
        # Generic singular name for an boundary of from this set
        'singular': 'Minnesota State House district (2002)',
        # Should the singular name come first when creating canonical identifiers for this set?
        'kind_first': False,
        # Function which each feature wall be passed to in order to extract its "external_id" property
        # The utils module contains several generic functions for doing this
        'ider': utils.simple_namer(['geoid10']),
        # Function which each feature will be passed to in order to extract its "name" property
        'namer': utils.simple_namer(['sldlst10'], normalizer=lambda x: x.lstrip('0')),
        # Authority that is responsible for the accuracy of this data
        'authority': 'U.S. Census Bureau Tiger lines',
        # Geographic extents which the boundary set encompasses
        'domain': 'Minnesota',
        # Last time the source was checked for new data
        'last_updated': date(2012, 5, 3),
        # A url to the source of the data
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
        'notes': 'These districts were defined in 2002.',
        # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
        'encoding': '',
        # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
        # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
        'srid': ''
    },
    'Minnesota State Senate districts (2002)': {
        'file': 'state-senate-districts/2010/tl_2010_27_sldu10/tl_2010_27_sldu10.shp',
        'singular': 'Minnesota State Senate district (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['sldust10'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'These districts were defined in 2002.',
        'encoding': '',
        'srid': ''
    },
    'Minnesota State House districts': {
        'file': 'state-house-districts/2012/L2012/L2012.shp',
        'singular': 'Minnesota State House district',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota GIS',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': 'These districts were defined in 2012.',
        'encoding': '',
        'srid': ''
    },
    'Minnesota State Senate districts': {
        'file': 'state-senate-districts/2012/S2012/S2012.shp',
        'singular': 'Minnesota State Senate district',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'Minnesota GIS',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': 'These districts were defined in 2012.',
        'encoding': '',
        'srid': ''
    },
    'Congressional districts': {
        'file': 'congressional-districts/2012/C2012/C2012.shp',
        'singular': 'Congressional district',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['district']),
        'authority': 'Minnesota GIS',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.gis.leg.mn/redist2010/plans.html',
        'notes': 'These districts were defined in 2012.',
        'encoding': '',
        'srid': ''
    },
    'Congressional districts (2002)': {
        'file': 'congressional-districts/2010/tl_2010_27_cd111/tl_2010_27_cd111.shp',
        'singular': 'Congressional district (2002)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['cd111fp'], normalizer=lambda x: x.lstrip('0')),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': 'These districts were defined in 2002.',
        'encoding': '',
        'srid': ''
    },
    'School districts': {
        'file': 'school-districts/tl_2010_27_unsd10/tl_2010_27_unsd10.shp',
        'singular': 'School district',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['name10']),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 5, 3),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2010/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Census tracts (2011)': {
        'file': 'census-tracts/tiger_2011/tl_2011_27_tract.shp',
        'singular': 'Census tract (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid']),
        'namer': utils.simple_namer(['name']),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2011/main',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Counties (2010)': {
        'file': 'counties/2010-ire-census/mn-counties-tl_2010_27_county10.shp',
        'singular': 'County (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid10']),
        'namer': utils.simple_namer(['name10']),
        'authority': 'U.S. Census Bureau (via IRE)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://census.ire.org/data/bulkdata.html',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'State forests': {
        'file': 'dnr/2009-state-forests/bdry_stforpy3.shp',
        'singular': 'State forest',
        'kind_first': False,
        'ider': utils.index_namer('sft-'),
        'namer': utils.simple_namer(['name']),
        'authority': 'Minnesota Department of Natural Resources (DNR)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://deli.dnr.state.mn.us/metadata.html?id=L220000170201',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'State parks': {
        'file': 'dnr/2002-state-parks/bdry_stprkpy3.shp',
        'singular': 'State park',
        'kind_first': False,
        'ider': utils.index_namer('sp-'),
        'namer': utils.simple_namer(['long_name']),
        'authority': 'Minnesota Department of Natural Resources (DNR)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://deli.dnr.state.mn.us/metadata.html?id=L220000190201',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'National forests': {
        'file': 'dnr/2008-national-forests/bdry_ntforpy3.shp',
        'singular': 'National forest',
        'kind_first': False,
        'ider': utils.index_namer('nf-'),
        'namer': utils.simple_namer(['name']),
        'authority': 'Minnesota Department of Natural Resources (DNR)',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://deli.dnr.state.mn.us/metadata.html?id=L220000110201',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Census places (2011)': {
        'file': 'census-places/2011-places/tl_2011_27_place.shp',
        'singular': 'Census place (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['geoid']),
        'namer': utils.simple_namer(['name']),
        'authority': 'U.S. Census Bureau Tiger lines',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.census.gov/cgi-bin/geo/shapefiles2011/main',
        'notes': 'From Wikipedia: "A census-designated place (CDP) is a concentration of population identified by the United States Census Bureau for statistical purposes. CDPs are delineated for each decennial census as the statistical counterparts of incorporated places such as cities, towns and villages. CDPs are populated areas that lack separate municipal government, but which otherwise physically resemble incorporated places."',
        'encoding': '',
        'srid': ''
    },
    'Neighborhoods (2012)': {
        'file': 'zillow/2012-neighborhoods/ZillowNeighborhoods-MN.shp',
        'singular': 'Neighborhood (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['regionid']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Zillow',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.zillow.com/howto/api/neighborhood-boundaries.htm',
        'notes': 'Data provided by Zillow.',
        'encoding': '',
        'srid': ''
    },
    'Reservation lands (2010)': {
        'file': 'reservations/2010-air/amerind2010.shp',
        'singular': 'Reservation land (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Minnesota GIS and US Census',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.gis.leg.mn/metadata/amerind2010.htm',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    # Will take awhile
    'Voting precincts (2010)': {
        'file': 'precincts/2010-precincts/vtd_20101029.shp',
        'singular': 'Voting precinct (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['district', 'precinct_n']),
        'namer': utils.simple_namer(['precinct']),
        'authority': 'Minnesota GIS and Minnesota Secretary of State',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.gis.leg.mn/metadata/vtd2010.htm',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    # Will take awhile
    'Minor civil divisions (2010)': {
        'file': 'minor-civil-divisions/2010-mcd/mcd2010.shp',
        'singular': 'Minor civil division (2010)',
        'kind_first': False,
        'ider': utils.simple_namer(['id']),
        'namer': utils.simple_namer(['name']),
        'authority': 'Minnesota Legislative Coordinating Commission - GIS Office',
        'domain': 'Minnesota',
        'last_updated': date(2012, 6, 22),
        'href': 'http://www.gis.leg.mn/metadata/mcd2010.htm',
        'notes': 'Minor civil divisions are also considered cities and townships.',
        'encoding': '',
        'srid': ''
    },
    'States (2011)': {
        'file': 'states/2011-census/tl_2011_us_state.shp',
        'singular': 'State (2011)',
        'kind_first': False,
        'ider': utils.simple_namer(['stusps']),
        'namer': utils.simple_namer(['name']),
        'authority': 'US Census Bureau',
        'domain': 'United States of America',
        'last_updated': date(2012, 7, 13),
        'href': 'ftp://ftp2.census.gov/geo/tiger/TIGER2011/STATE/',
        'notes': '',
        'encoding': '',
        'srid': ''
    },
    'Countries (2012)': {
        'file': 'countries/2012-natural_earth_1.4.0/10m-admin-0-countries-edited.shp',
        'singular': 'Country (2012)',
        'kind_first': False,
        'ider': utils.simple_namer(['ne_10m_adm']),
        'namer': utils.simple_namer(['admin']),
        'authority': 'Natural Earth',
        'domain': 'World',
        'last_updated': date(2012, 7, 13),
        'href': 'http://www.naturalearthdata.com/downloads/10m-cultural-vectors/',
        'notes': 'Edited to remove columns to reduce file size, and to remove any non-ASCII characters.',
        'encoding': '',
        'srid': ''
    }
}