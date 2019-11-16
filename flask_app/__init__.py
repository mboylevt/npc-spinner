from flask import Flask
from flask_app.route_npc import npc
app = Flask(__name__)
app.register_blueprint(npc, url_prefix='/')

# Start app if in development mode
try:
    app.run('0.0.0.0', port=3030, debug=True)
except:
    pass