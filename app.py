from flask import Flask, request, jsonify
from flask_redis import FlaskRedis 
from flask_cors import CORS 

import random
import string

app = Flask(__name__)
app.config["REDIS_URL"] ="redis://@localhost:6379/0"

redis_client = FlaskRedis(app)
CORS(app)

@app.route("/url/add", methods=["POST"])
def add_url():
    post_data = request.get_json()
    url = post_data.get("url")

    key = "".join([random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase)for _ in range(20)])
    redis_client.set(key, url)

    return jsonify(key)

@app.route("/url/get/<key>", methods=["GET"])
def get_url(key):
    url = redis_client.get(key).decode("utf-8")
    print(url)
    return jsonify(url)

@app.route("/url/get", methods=["GET"])
def get_all_urls():
    all_keys = redis_client.keys("*")
    # all_urls = []
    # for key in all_keys:
    #     keys.append(key.decode("utf-8"))
    return jsonify([key.decode("utf-8") for key in all_keys])

if__name__=="__main__":
    app.run(debug=True)





# from flask import Flask
# from flask_redis import FlaskRedis

#  local variables for Redis implementation
#     redis_srv = None

    



#     base_url = ''

# def __init__(self):
#         "Initializes self"
#         self.redis_srv = redis.StrictRedis(host='localhost', port=6379, db=0)

#         def shorten_url(self, long_url):

# @app.route("/add", methods=["POST"])
# def add_stuff():
#     print("test")
#     if request.content_type != "application/json":
#         print("test two")
#         return "Error: Data must be sent as JSON."
    
    

  
#     db.session.add()
#     db.session.commit()

#     url_str_arr = list(long_url)
#     random.shuffle(url_str_arr)

    
#     if len(url_str_arr) > 20:
#         shortened_url = url_str_arr[-10:]
#     else:
#         shortened_url = url_str_arr

#     jumbled_url_suffix = ''.join(shortened_url)
#     shortened_url = self.base_url + jumbled_url_suffix

    
#     encoded_url = encode_base64(shortened_url)

#     shortened_url_key = url_string_formatter(self.redis_shortened_url_key_fmt, encoded_url)

#     self.redis_srv.set(shortened_url_key, long_url)
#     self.redis_srv.lpush(self.redis_global_urls_list, encoded_url)

#     return shortened_url, encoded_url


# if __name__ == "__main__":
#     app.run(debug=True)