These files are used for deployment.

## Deploying

Copy and configure Gunicorn startup script:

``
cp deployment/gunicorn.startup_sh.example gunicorn.startup_sh;
nano gunicorn.startup_sh;
```

Copy and configure the Upstart script:

``
sudo cp deployment/boundaryservice.conf /etc/init/boundaryservice.conf;
sudo nano /etc/init/boundaryservice.conf;
```

To start the application, run the following:

```
sudo start boundaryservice;
```


For more details on install and deployment, see:
https://github.com/MinnPost/mn-boundaryservice/wiki/Deployment-and-Install