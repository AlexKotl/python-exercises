from flask import Flask, render_template, request
from pprint import pprint

app = Flask(__name__, static_folder=".", static_url_path='', template_folder='.')

@app.route("/")
def index():
    #return app.send_static_file('template.html')
    return render_template('template.html', content = request.args.get("content"), color = request.args.get("color"))

app.run(port=5001, debug=True)
