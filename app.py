from flask import Flask, request, jsonify
from flask_redis import FlaskRedis 

import random
import string

app = Flask(__name__)
app.config["REDIS_URL"] ="redis://@localhost:6379/0"

redis_client = FlaskRedis(app)

@app.route("/url/add", methods=["POST"])
def add_url():
    post_data = request.get_json()
    url = post_data.get("url")

    key = "".join([random.SystemRandom().choice([string.ascii_uppercase + string.ascii_lowercase])])
    redis_client.set("Key", url)

    return jsonify("Data added")

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