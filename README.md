Sample Python Web application
=============================

The`` sample is using [Flask microframework](http://flask.pocoo.org/) and is intented to test the Python support on [Pivotal's Cloud Foundry](https://run.pivotal.io/).
`````
Deploy to Cloud Foundry
-----------------------
```script
cf push <YOUR_APP_NAME> -m 128M
```
or
```script
cf push <YOUR_APP_NAME> -m 128M
```
or
```script
cf push <YOUR_APP_NAME> -m 128M
````
UPDATE: Deploy with REDIS
```script
cf push hello-world-rafa-counter -m 128M
cf bind-service hello-world-rafa-counterRedisCloud
cf restage hello-world-rafa-counter
```
