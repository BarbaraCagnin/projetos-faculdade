from flask import Flask, render_template
import folium

app = Flask(__name__)

@app.route('/')
def mapa():
    mapa = folium.Map(location=[-23.55052, -46.633308], zoom_start=13)

    pontos = [
        {"nome": "Supermercado Verde", "local": [-23.5489, -46.6388]},
        {"nome": "Escola Municipal São João", "local": [-23.5532, -46.6291]},
        {"nome": "EcoPonto Bairro Novo", "local": [-23.5525, -46.635]},
    ]

    for ponto in pontos:
        folium.Marker(ponto["local"], tooltip=ponto["nome"]).add_to(mapa)

    mapa.save("templates/mapa.html")
    return render_template("mapa.html")

if __name__ == '__main__':
    app.run(debug=True)

