# Minnesota Boundary Service

A REST API for determing what boundaries (administrative, political, etc) a location is in for the state of Minnesota.

Forked from OpenNorth [boundary service](https://github.com/opennorth/blank-boundaryservice).  Deployed at [boundaries.minnpost.com](http://boundaries.minnpost.com/).

## Install

First, install the requirements. This assumes you already have Python 2.7.

1. Install pip: `sudo easy_install pip`
1. (optional) Use a virtual environement: `sudo pip install virtualenv && virtualenv .venv && source .venv/bin/activate`
1. Install python libraries: `pip install -r requirements.txt`

### Database

Next, create a PostGIS database, as the Boundary Service depends on PostGIS.

### Application settings

Lastly, configure the `DATABASES` Django setting and and create the database tables.

1. Copy example settings: `cp settings_override.py.example settings_override.py`
1. Put in the appropriate database setting: `nano settings_override.py`
1. Initial database: `python manage.py syncdb`

### Load boundary sets

The following will load all the boundary sets (and duplicate any existing ones).  See below for individual addition and deletions.

1. `python manage.py loadshapefiles`

## Adding and managing boundary sets

### Adding a boundary set

1. Find boundary dataset.  This should be a unzipped shapefile directory (specifically with a .shp file).
1. You may need to alter the dataset to ensure the best IDs or something like that, but the goal should be to alter the original dataset as little as possible.
1. This should go into a subject directory in `data/shapefiles` and then within a directory named by year and source.  For instance: `data/shapefiles/counties/2010-mn-gis-leg/data.shp`
1. Update the `data/shapefiles/definitions.py` file with the appropriate data.  Please follow the conventions that exist in the current definitions.
    * **The `namer` field is what will be used for the slug and should be the idtenfier for the data.  This should be the most universal and common identifer that can be used.**
1. Update database with new set by running: `python manage.py loadshapefiles -o "Censustracts(2011)","Blah.Blah.()"`
    * The comma-separated arguments are the keys of the `SHAPEFILES` dictionary with spaces removed.

### Listing boundary sets

To list the boundary sets:

    python data/shapefiles/list_sets.py

### Removing boundary datasets

If you need to remove all datasets and reload all of them, use the following:

    python manage.py sqlreset boundaryservice | psql -h localhost DB_NAME
    python manage.py syncdb

You can remove a specific dataset with the something like the following.  Get the boundary set ID with the boundary listing script.

    python data/shapefiles/remove_set.py

## Development

To test it locally:

    python manage.py runserver
    curl http://127.0.0.1:8000/1.0/

## Deployment

Production deployment is aimed at an Ubunutu server on EC2.

### Server libraries

    sudo apt-get update
    sudo apt-get install git-core python-setuptools python-dev build-essential nginx binutils gdal-bin libproj-dev python-psycopg2
    sudo apt-get install postgresql-9.1-postgis postgresql-server-dev-9.1
    sudo easy_install pip

### Database

Setup postgres password:

    sudo -u postgres psql postgres

Following [this documentation](https://wiki.archlinux.org/index.php/PostGIS) to set up postgis:

    sudo su - postgres
    createdb -E UTF8 template_postgis
    createlang plpgsql template_postgis
    psql -d postgres -c "UPDATE pg_database SET datistemplate='true' WHERE datname='template_postgis';"
    psql -d template_postgis -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
    psql -d template_postgis -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql

Create specific database and user for our default user.  Change as needed.

    createdb -U postgres -h localhost -T template_postgis mn_boundaryservice
    psql -U postgres -h localhost mn_boundaryservice
    psql> CREATE USER ubuntu;
    psql> GRANT ALL PRIVILEGES ON DATABASE mn_boundaryservice TO ubuntu;
    psql> GRANT ALL ON TABLE spatial_ref_sys TO ubuntu;
    psql> GRANT ALL ON TABLE geometry_columns TO ubuntu;
    psql> ALTER USER ubuntu WITH PASSWORD '<your_pass_here>';

### Install application

Follow the general install instructions above.  Some helpful configuration values in `settings_override.py`:

* configure `CACHES`
* set `COMPRESS_ENABLED = True`
* set `API_DOMAIN`

### Configure services

Copy and configure Gunicorn startup script:

    cp deployment/gunicorn_startup.sh .example gunicorn_startup.sh ;
    chmod +x gunicorn_startup.sh;
    nano gunicorn_startup.sh;

Copy and configure the Upstart script:

    sudo cp deployment/boundaryservice.conf.example /etc/init/boundaryservice.conf;
    sudo nano /etc/init/boundaryservice.conf;

To start the application, run the following:

    sudo start boundaryservice;

Set up NGINX for web serving.  Update values as needed.

    sudo cp deployment/boundaries.minnpost.com.nginx.example /etc/nginx/sites-available/boundaries.minnpost.com;
    sudo ln -s /etc/nginx/sites-available/boundaries.minnpost.com /etc/nginx/sites-enabled/boundaries.minnpost.com;
    sudo rm /etc/nginx/sites-enabled/default
    sudo /etc/init.d/nginx restart;

#### Set up Varnish (Optional)

From the [install Varnish on Ubuntu instructions](https://www.varnish-cache.org/installation/ubuntu).  Currently the varnish cache is set to never expire, so when adding new data or changing the data, make sure to clear the varnish cache.

1. `sudo curl http://repo.varnish-cache.org/debian/GPG-key.txt | sudo apt-key add -`
1. Edit `/etc/apt/sources.list` and add new line with `deb http://repo.varnish-cache.org/ubuntu/ lucid varnish-3.0`
1. `sudo apt-get update`
1. `sudo apt-get install varnish`

Update NGINX to use port 8080.

   sudo nano /etc/nginx/sites-available/boundaryservice.minnpost.com;
   sudo /etc/init.d/nginx restart;

Configure by copying provided Varnish config.  Update values as needed.

    sudo cp /etc/varnish/default.vcl /etc/varnish/default.vcl.orig;
    sudo cp deployment/default.vcl.example /etc/nginx/sites-available/boundaries.minnpost.com;

Add `DAEMON_OPTS="-a :80` to `/etc/default/varnish`.  Restart varnish with `sudo /etc/init.d/varnish restart`

## Troubleshooting

If `python manage.py runserver` quits unexpectedly without error, use an alternative server:

    pip install gunicorn
    python manage.py collectstatic
    gunicorn_django settings.py

If `python manage.py loadshapefiles` causes this error:

    ERROR 1: dlopen(/Library/Application Support/GDAL/1.8/PlugIns/ogr_GRASS.dylib, 1): Symbol not found: __ZN11OGRSFDriver14CopyDataSourceEP13OGRDataSourcePKcPPc
      Referenced from: /Library/Application Support/GDAL/1.8/PlugIns/ogr_GRASS.dylib
      Expected in: flat namespace
     in /Library/Application Support/GDAL/1.8/PlugIns/ogr_GRASS.dylib

you may resolve it on OS X by running:

    brew install gdal-grass

If `python manage.py loadshapefiles` causes this error:

    IOError: [Errno 2] No such file or directory: '/var/folders/yn/4cwyp7v55w1c127fbn8sk8gm0000gn/...'

make sure that all files referenced in `definitions.py` exist.

## Attribution

This Boundary Service instance uses the following open-source software:

* [Newsapps Boundary Service](https://github.com/newsapps/django-boundaryservice)
* [Leaflet](http://leaflet.cloudmade.com/)
* [json2.js](https://github.com/douglascrockford/JSON-js)
* [store.js](https://github.com/marcuswestin/store.js)
* [Less Framework 3](http://lessframework.com/v3/)
* [Eric Meyer Reset CSS](http://meyerweb.com/eric/tools/css/reset/)
* [Modernizr from HTML5 Boilerplate](http://html5boilerplate.com/)
