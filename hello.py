import os
import uuid
import redis
import json
from flask import Flask, session


app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN


rediscloud_service = json.loads(os.environ['VCAP_SERVICES'])['rediscloud'][0]
credentials = rediscloud_service['credentials']
r = redis.Redis(host=credentials['hostname'], port=credentials['port'], password=credentials['password'])

r.set("rafa_hit_counter", 1)

def sumhitcounter():
    r.incr("rafa_hit_counter")
    pcounter = r.get("rafa_hit_counter")
    return pcounter


@app.route('/')
def hello():
#    sumhitcounter()
    return """
    <html>
    <body bgcolor="{}">

    <center><h1><font color="white">Hi, I'm GUID:<br/>
    {}</br>
    <hr>
    <h2>Page Counter: {}

    </center>

    </body>
    </html>
    """.format(COLOR,my_uuid,sumhitcounter(),)
    

if __name__ == "__main__":
	app.run(debug=True,host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', '5000')))
