import flask
from counting_life import calculate_life_time_formats

app = flask.Flask(__file__)


@app.route('/<int:age>')
def main(age: int):
    lifetime_formats = calculate_life_time_formats(age)
    return {
        'days': lifetime_formats.days,
        'hours': lifetime_formats.hours,
        'minutes': lifetime_formats.minutes,
        'seconds': lifetime_formats.seconds
    }


if __name__ == "__main__":
    app.run(port=80, host='0.0.0.0')
