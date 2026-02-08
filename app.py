from flask import Flask, render_template, request
import random

app = Flask(__name__)

# ---------- Constants ----------
OBJECT_PRONOUNS = ['Her','Him','Them']
POSSESSIVE_PRONOUNS = ['Her','His','Their']
PERSONAL_PRONOUNS = ['She','He','They']

STATES = ['California','Texas','Florida','New York','Penssylvania',
          'Illinois','Ohio','Georgia','North Carolina','Michigan']

NOUNS = ['Athlete','Clown','Shovel','Keto Diet','Robot',
         'Peach','Banana','Serial Killer']

PLACES = ['House','School','Mall','Bunker']

WHEN = ['Soon','This Year','Later Today','RIGHT NOW','Next Week']


# ---------- Headline Functions ----------

def generateAreMillennialsKillingHeadline():
    noun = random.choice(NOUNS)
    return f"Are Millennials Killing the {noun} Industry?"


def generateWhatYouDontKnowHeadline():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + 's'
    when = random.choice(WHEN)
    return f"Without This {noun}, {pluralNoun} could kill you {when}"


def generateBigCompaniesHateHerHeadline():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See how this {state} {noun1} Invented a Cheaper {noun2}"


def generateYouWontBelieveHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESSIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won't Believe What This {state} {noun} Found in {pronoun} {place}"


def generateDontWantYouToKnowHeadline():
    pluralNoun1 = random.choice(NOUNS) + 's'
    pluralNoun2 = random.choice(NOUNS) + 's'
    return f"What {pluralNoun1} Don't Want You To Know About {pluralNoun2}"


def generateGiftIdeaHeadline():
    number = random.randint(7, 15)
    noun = random.choice(NOUNS)
    state = random.choice(STATES)
    return f"{number} Gift Ideas to Give Your {noun} From {state}"


def generateReasonsWhyHeadline():
    number1 = random.randint(3, 19)
    pluralNoun = random.choice(NOUNS) + 's'
    number2 = random.randint(1, number1)
    return f"{number1} Reasons Why {pluralNoun} Are More Interesting Than You Think (Number {number2} Will Surprise You!)"


def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)

    i = random.randint(0, 2)
    pronoun1 = POSSESSIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]

    return f"This {state} {noun} Didn't Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong."


def generate_random_headline():
    clickbaitType = random.randint(1, 8)

    if clickbaitType == 1:
        return generateAreMillennialsKillingHeadline()
    elif clickbaitType == 2:
        return generateWhatYouDontKnowHeadline()
    elif clickbaitType == 3:
        return generateBigCompaniesHateHerHeadline()
    elif clickbaitType == 4:
        return generateYouWontBelieveHeadline()
    elif clickbaitType == 5:
        return generateDontWantYouToKnowHeadline()
    elif clickbaitType == 6:
        return generateGiftIdeaHeadline()
    elif clickbaitType == 7:
        return generateReasonsWhyHeadline()
    else:
        return generateJobAutomatedHeadline()


# ---------- Flask Routes ----------

@app.route("/", methods=["GET", "POST"])
def index():
    headlines = []

    if request.method == "POST":
        amount = int(request.form.get("amount", 5))

        for _ in range(amount):
            headlines.append(generate_random_headline())

    return render_template("index.html", headlines=headlines)


if __name__ == "__main__":
    app.run(debug=True)
