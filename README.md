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
cf push <YOUR_APP_NAME> -m 128M
cf bind-service <YOUR_APP_NAME> RedisCloud
cf restage <YOUR_APP_NAME>
```
UPDATE: Add NEWRELIC Instrumentation
```script
cf push <YOUR_APP_NAME> -m 128M
cf set-env <YOUR_APP_NAME> NEW_RELIC_APP_NAME <YOUR_APP_NAME>
cf set-env <YOUR_APP_NAME> NEW_RELIC_LICENSE_KEY <YOUR_NEWRELIC_LIC_KEY> 
```
