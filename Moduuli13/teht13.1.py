# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina
# saatu luku alkuluku vai ei. Hyödynnä toteutuksessa aiempaa tehtävää,
# jossa alkuluvun testaus tehtiin. Esimerkiksi lukua 31 vastaava GET-pyyntö
# annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, Response
import json

app = Flask(__name__)


@app.route('/alkuluku/<number>')
def alkuluku(number):
    try:
        number = float(number)
        if number > 1 and number % 1 == 0 and number % number == 0:
            isPrime = True
            tilakoodi = 200
            vastaus = {
                "Number": number,
                "isPrime": isPrime
            }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
