"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return """<!doctype html><html>Hi! This is the home page. <a href="/hello">Hello page</a></html>"""


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("player")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", player=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """Ask player if they want to play a game."""
    
    response = request.args.get("game")

    if response == "game-yes":
        return render_template("game.html") 
    elif response == "game-no":
        return render_template("goodbye.html") 
    

@app.route("/madlib")
def show_madlib():
    """Take in inputs from the player, and output the madlib sentence."""

    player = request.args.get("player")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    
    return render_template("madlib.html", player=player, color=color, noun=noun, adjective=adjective)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
