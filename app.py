from flask import Flask, render_template,request
import random
app = Flask(__name__)

OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESSIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Keto Diet', 'Robot', 'Peach', 'Banana', 'Serial Killer']
PLACES = ['House', 'School', 'Mall', 'Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']

def pick(lst): return random.choice(lst)
def num(a,b): return random.randint(a, b)

GENERATORS = [
    lambda: f"Are Millenials Killing the {pick(NOUNS)} Industry?",
    lambda: f"Without this {pick(NOUNS)}! {pick(NOUNS)} Could Kill You {pick(WHEN)}",
    lambda: f"Big Companies Hate {pick(OBJECT_PRONOUNS)}! See how this {pick(STATES)} {pick(NOUNS)} Invented a Cheaper {pick(NOUNS)}",
    lambda: f"What {pick(NOUNS)} Dont Want You to Know About {pick(NOUNS)}s",
    lambda: f"{num(7,15)} Gift Ideas To Give Your {pick(NOUNS)} from {pick(STATES)}",
    lambda: (n := num(3,19),f"{n} Reasons Why {pick(NOUNS)} are More Interesting Than You Think (Number {num(1,n)} Will Suprise You!)")[1],
    lambda: (i := num(0, 2), f"This {pick(STATES)} {pick(NOUNS)} Didn't Think Robots Would Take {POSSESSIVE_PRONOUNS[i]} Job. {PERSONAL_PRONOUNS[i]} Were Wrong.")[1]
    
]

@app.route("/", methods = ["GET","POST"])
def index():
    headlines = []
    if request.method == "POST":
        amount = min(int(request.form.get("amount", 5)), 20)
        headlines = [random.choice(GENERATORS)() for _ in range(amount)]
    return render_template("index.html",headlines=headlines)

if __name__ == "__main__":
    import os 
    port = int(os.environ.get("PORT", 8080))
    app.run(host = "0.0.0.0", port = port,debug = False)
    