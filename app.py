from flask import Flask
from redis import Redis
import logging

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    counter = str(redis.get('hits'),'utf-8')
    return "Welcome to Thetips4you!, This webpage has been viewed "+counter+" time(s)"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True)
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)