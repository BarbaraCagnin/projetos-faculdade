from flask import Flask, render_template
import folium
from folium.plugins import MarkerCluster
import mimetypes
mimetypes.add_type('text/css', '.css')
mimetypes.add_type('application/javascript', '.js')

app = Flask(__name__)

@app.route('/')
def mapa():
    m = folium.Map(
        location=[-23.575, -46.585],
        zoom_start=13,
        tiles='OpenStreetMap',
        control_scale=True
    )

    marker_cluster = MarkerCluster().add_to(m)

    locais = [
        {"nome": "EcoPonto Vila Prudente", "coordenadas": [-23.5847, -46.5835], "tipo": "Diversos", "endereço": "R. Dr. João Ribeiro, 142"},
        {"nome": "Supermercado EcoVila", "coordenadas": [-23.5823, -46.5801], "tipo": "Recicláveis", "endereço": "Av. do Oratório, 2001"},
        {"nome": "Cooperativa Recicla Vila Alpina", "coordenadas": [-23.5672, -46.5718], "tipo": "Recicláveis", "endereço": "R. Serra da Mantiqueira, 45"},
        {"nome": "Posto de Coleta VL Alpina", "coordenadas": [-23.5705, -46.5753], "tipo": "Eletrônicos", "endereço": "R. Itapira, 88"},        
        {"nome": "EcoPonto Mooca", "coordenadas": [-23.5624, -46.5998], "tipo": "Diversos", "endereço": "R. Taquari, 549"},
        {"nome": "Loja Verde Mooca", "coordenadas": [-23.5589, -46.5932], "tipo": "Óleo/Pilhas", "endereço": "Av. Paes de Barros, 1567"},
        {"nome": "EcoPonto São Lucas", "coordenadas": [-23.5989, -46.5345], "tipo": "Diversos", "endereço": "R. São Lucas, 200"},
        {"nome": "Centro de Reciclagem SL", "coordenadas": [-23.6012, -46.5388], "tipo": "Recicláveis", "endereço": "Av. Sapopemba, 3000"},
        {"nome": "Ponto de Coleta Camillo Haddad", "coordenadas": [-23.5912, -46.5567], "tipo": "Eletrônicos", "endereço": "R. Camillo Haddad, 150"},
        {"nome": "Escola Recicla CH", "coordenadas": [-23.5889, -46.5523], "tipo": "Papel/Pet", "endereço": "R. dos Bandeirantes, 500"},
        {"nome": "Associação Jd. Independência", "coordenadas": [-23.6067, -46.5432], "tipo": "Recicláveis", "endereço": "R. Independência, 350"},
        {"nome": "EcoPonto Jd. Independência", "coordenadas": [-23.6034, -46.5401], "tipo": "Diversos", "endereço": "Av. Sapopemba, 3200"}
    ]

    # Cores por tipo de material
    cores = {
        "Diversos": "green",
        "Recicláveis": "blue",
        "Eletrônicos": "red",
        "Óleo/Pilhas": "orange",
        "Papel/Pet": "lightblue"
    }

    for local in locais:
        folium.Marker(
            location=local["coordenadas"],
            popup=f"""
                <b>{local['nome']}</b><br>
                <b>Tipo:</b> {local['tipo']}<br>
                <b>Endereço:</b> {local['endereço']}
            """,
            tooltip=local["nome"],
            icon=folium.Icon(
                color=cores.get(local["tipo"], "gray"),
                icon="recycle",
                prefix="fa"
            )
        ).add_to(marker_cluster)

    folium.LayerControl().add_to(m)

    # Mapa para HTML
    mapa_html = m._repr_html_()

    return render_template(
        'mapa.html',
        mapa_html=mapa_html,
        titulo="Pontos de Coleta - Zona Leste SP",
        bairros="Vila Prudente, Vila Alpina, Mooca, São Lucas, Camillo Haddad e Jardim Independência"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)