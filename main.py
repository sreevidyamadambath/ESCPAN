from flask import*
from public import public
from staff import staff
from cbi import cbi
from branch import branch
from api import api

app=Flask(__name__)
app.secret_key="abc"
app.register_blueprint(public)
app.register_blueprint(branch)
app.register_blueprint(staff)
app.register_blueprint(cbi)
app.register_blueprint(api)
app.run(debug=True)