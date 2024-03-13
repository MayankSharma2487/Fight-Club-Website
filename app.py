from flask import Flask, render_template, jsonify

app = Flask(__name__)

CLUB = [
    {
        'id': 1,
        'name': 'Aligarh Club',
        'country': 'India',
        'founded': 1999,
        'place': 'Khair',
        'manager': 'Nikhil Sharma'
    },
    {
        'id': 2,
        'name': 'Mathura Club',
        'country': 'India',
        'founded': 2021,
        'place': 'GLA',
        'manager': 'Kapil Sharma'
    },
    {
        'id': 3,
        'name': 'Delhi Club',
        'country': 'India',
        'founded': 2022,
        'place': 'Mukharji Nagar',
        'manager': 'Sachin Sharma'
    },
    {
        'id': 4,
        'name': 'Bhopal Club',
        'country': 'India',
        'founded': 2020,
        'place': 'Indrapuri',
        'manager': 'Ankit Goutam'
    },
    {
        'id': 5,
        'name': 'Khair sub Club',
        'country': 'India',
        'founded': 2000,
        'place': 'Nagla Virua , khair aligarh',
        'manager': "Royal Pandit's"
    },
]


@app.route("/")
def hello_world():
    return render_template('home.html', clubs=CLUB)


@app.route("/myclub")  # No club ID in the route definition
def show_club():
    return render_template('club_details.html', clubs=CLUB)


@app.route("/api/clubs")
def list_clubs():
    return jsonify(CLUB)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
