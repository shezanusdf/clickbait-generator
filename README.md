# Clickbait Headline Generator

A Flask web application that generates randomized clickbait headlines using multiple templates and word pools.

## Tech stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)


## Installation

Install Flask:
```bash
pip install flask
```

## Usage

Run the application:
```bash
python app.py
```

Access the web interface at:
```
http://localhost:5000
```

Enter the desired number of headlines and click generate.

## How It Works

The application uses randomization to combine words from predefined lists:

- OBJECT_PRONOUNS: Her, Him, Them
- POSSESSIVE_PRONOUNS: Her, His, Their
- PERSONAL_PRONOUNS: She, He, They
- STATES: California, Texas, Florida, New York, Pennsylvania, Illinois, Ohio, Georgia, North Carolina, Michigan
- NOUNS: Athlete, Clown, Shovel, Keto Diet, Robot, Peach, Banana, Serial Killer
- PLACES: House, School, Mall, Bunker
- WHEN: Soon, This Year, Later Today, RIGHT NOW, Next Week

Each headline template function randomly selects items from these lists to create absurd but structurally valid clickbait headlines.
