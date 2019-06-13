from app import app

@app.route("/")
def index():
	return "Flask uWSGI under docker container"