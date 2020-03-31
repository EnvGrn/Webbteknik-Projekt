import flask
from flask import request
app = flask.Flask(__name__)

users = {
	"Envy" : [
		"Envy",
		hash("cfad44646")
	]
}

@app.route("/")
def main():
	# visa FILVÄG för användaren
	return flask.render_template("index.html") #filväg för index.html

@app.route("/teks")
def teks():
	return flask.render_template("17teks.html")

@app.route("/tekcs")
def tekcs():
	return flask.render_template("17tekcs.html")

@app.route("/tekdm")
def tekdm():
	return flask.render_template("17tekdm.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        form = request.form

        if len(form.psw) > 16 or len(form.psw) < 4:
            return flask.render_template("register.html", error="Lösenordet måste vara mellan 4 och 16 tecken")
        elif form.psw != form.psw2:
            return flask.render_template("register.html", error="Lösenorden ska matcha!")
        elif form.email in users:
            return flask.render_template("register.html", error="Det finns redan ett konto med nedskriven email")
        else:
            users[form.email] = [form.email, hash(form.psw)]
            return flask.render_template("login.html")
    else:
        return flask.render_template("register.html")
		
# hanterar vad som händer när route är "/login"
# accepterar requests med metoderna get och post
# get för att hämta login sida, post för att ladda upp saker till den
@app.route("/login", methods=["GET", "POST"])
def login():

	# om metoden är post
	if request.method == "POST":
		form = request.form

		# ha en form på hemsidan som har två fält för inlogning
		# password för lösenord och username för användarnamn

		# kolla om lösenordet finns
		if form.email in users:
			#kolla om lösenorden stämmer
			if hash(form.psw) == users[form.email][1]:
				# filväg för den in loggade hesidan som man ska se om man är inloggad
				return flask.redirect("index.html")
		return flask.render_template("login.html",  error="Någonting är fel, försök igen")
	# visa FILVÄG för användaren (eftersom get metoder kommer igenom)
	return flask.render_template("login.html") #filväg för login.html

app.run()
