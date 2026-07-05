#traducteur de code morse
#test code français : B,O,n,j,O,u,R
#test code morse : -...,---,-.,.---,---,..-,.-.
from flask import Flask, render_template, request

app = Flask(__name__)



alphabet_morse = {
"'" : "'",
"," : ",",
" " : " ",
".-" : "a",
"-..." : "b",
"-.-." : "c",
"-.." : "d",
"." : "e",
"..-." : "f",
"--." : "g",
"...." : "h",
".." : "i",
".---" : "j",
"-.-" : "k",
".-.." : "l",
"--" : "m",
"-." : "n",
"---" : "o",
".--." : "p",
"--.-" : "q",
".-." : "r",
"..." : "s",
"-" : "t",
"..-" : "u",
"...-" : "v",
".--" : "w",
"-..-" : "x",
"-.--" : "y",
"--.." : "z"
}

alphabet_normal = {
    "'" : "'",
    "," : ",",
    " " : " ",
    "a" : ".-",
    "b" : "-...",
    "c" : "-.-.",
    "d" : "-..",
    "e" : ".",
    "f" : "..-.",
    "g" : "--.",
    "h" : "....",
    "i" : "..",
    "j" : ".---",
    "k" : "-.-",
    "l" : ".-..",
    "m" : "--",
    "n" : "-.",
    "o" : "---",
    "p" : ".--.",
    "q" : "--.-",
    "r" : ".-.",
    "s" : "...",
    "t" : "-",
    "u" : "..-",
    "v" : "...-",
    "w" : ".--",
    "x" : "-..-",
    "y" : "-.--",
    "z" : "--..",
}

@app.route("/", methods=["GET", "POST"])
def accueil():
    resultat = None
    if request.method == "POST":
        saisie = request.form["saisie"].lower()
        phrase = saisie.split(",")
        resultat = traduction(phrase, alphabet_morse, alphabet_normal)
    return render_template("index.html", resultat=resultat)


def traduction(phrase, alphabet_morse, alphabet_normal):

    phrase_traduction = ""

    if "-" in "".join(phrase) or "." in "".join(phrase):
        dico = alphabet_morse
    else:
        dico = alphabet_normal

    for lettre in phrase:
        phrase_traduction += dico[lettre]
    return phrase_traduction

if __name__ == "__main__":
    app.run(debug=True)