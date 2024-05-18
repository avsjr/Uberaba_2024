from flask import Flask, render_template, request
import geopandas as gpd
import folium

app = Flask(__name__)

# Seu arquivo .geojson
file_path = 'c:/Users/avsj/iCloudDrive/01.Antonio/01.Projetos/01.github/Uberaba_2024/files/UPG_REGIOES.geojson'

# Lê o arquivo .geojson como um GeoDataFrame
gdf = gpd.read_file(file_path)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        
        # Cria o mapa uma vez fora do loop
        m = folium.Map(location=[gdf.geometry.centroid.y.mean(), gdf.geometry.centroid.x.mean()], zoom_start=12)

        legend2_html = '''
            <div style="position: fixed; 
                        bottom: 30px; left: 250px; width: 200px; height: 600px; 
                        border:2px solid grey; z-index:9999; font-size:12px;
                        background-color: white;
                        opacity: 0.8;
                        overflow-y: scroll;
                        ">
                <h4 style="text-align:center; margin: 5px; font-size: 13px;">Elisa X Tony</h4>
        '''

        for idx, row in gdf.iterrows():
            region_number = idx + 1
            elisa_percentage = float(request.form[f'region{region_number}_elisa_percentage'])
            tony_percentage = float(request.form[f'region{region_number}_tony_percentage'])
            
            # Calcula o líder da região
            if elisa_percentage > tony_percentage:
                region_leader = 'Elisa'
            elif tony_percentage > elisa_percentage:
                region_leader = 'Tony'
            else:
                region_leader = 'Empate'
            
            color = get_color(region_leader)

            # Adiciona a geometria da região ao mapa com a cor definida
            folium.GeoJson(row['geometry'],
                           name=row['name'],
                           style_function=lambda feature, color=color: {'fillColor': color, 'color': 'black', 'weight': 1.5}).add_to(m)

            # Adiciona marcador com o nome da região (mesma cor para todos)
            folium.Marker(location=[row['geometry'].centroid.y, row['geometry'].centroid.x],
                          popup=folium.Popup(row['name'], max_width=300),
                          icon=folium.Icon(color='white', icon_color='black')).add_to(m)

            # Adiciona a legenda flutuante
            legend2_html += f'''
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região {region_number}:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Elisa Araújo: {elisa_percentage}%</li>
                    <li>Tony Carlos: {tony_percentage}%</li>
                    <li>Liderança: {region_leader}</li>
                </ul>
            </p>
                '''
        # Fecha a div da legenda 2
        legend2_html += '</div>'

        legend1_html = '''
            <div style="position: fixed; 
                        bottom: 30px; left: 30px; width: 200px; height: 600px; 
                        border:2px solid grey; z-index:9999; font-size:12px;
                        background-color: white;
                        opacity: 0.8;
                        overflow-y: scroll;
                        ">
            <h4 style="text-align:center; margin: 5px; font-size: 13px;">Regiões</h4>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 1:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Amoroso Costa</li>
                    <li>Paraíso</li>
                    <li>Lageado</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 2:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Lourdes</li>
                    <li>Residencial 2000</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 3:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Costa Teles</li>
                    <li>Leblon</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 4:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Vallim</li>
                    <li>Santa Clara</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 5:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Maracanã</li>
                    <li>Recreio dos Bandeirantes</li>
                    <li>São Geraldo</li>
                    <li>Lemes</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 6:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>São Cristóvão</li>
                    <li>Parque das Américas</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 7:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Abadia</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 8:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Estados Unidos</li>
                    <li>Boa Esperança</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 9:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Boa Vista</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 10:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Fabrício</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 11:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Centro</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 12:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>São Benedito</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 13:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Mercês</li>
                    <li>Grande Horizonte</li>
                    <li>Distrito Industrial I</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 14:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Aeroporto</li>
                    <li>Santa Maria</li>
                </ul>
            </p>
            <p style="margin: 10px; font-size: 12px; font-weight: bold;">Região 15:</span>
                <ul style="list-style-type: none; padding: 10;">
                    <li>Jockey Park</li>
                    <li>Morumbi</li>
                    <li>Alfredo Freire</li>
                    <li>Vila Real</li>
                    <li>Buriti</li>
                    <li>Marajó</li>
                </ul>
            </div>
            <div style="position: fixed; 
                 bottom: 30px; right: 30px; width: 280px; height: 100px; 
                 border:2px solid grey; z-index:9999; font-size:12px;
                 background-color: white;
                 opacity: 0.8;
                 ">
            <h4 style="text-align: center; margin: 5px; font-size: 13px;">Legenda</h4>
            <div style="margin: 10px;">
            <div style="display: flex; align-items: center;">
            <div style="width: 15px; height: 15px; margin: 3px; border: 1px solid black; background-color: darkgreen; opacity: 0.8;"></div>
            <span style="margin-right: 5px;">Elisa com maior porcentagem</span>
            </div>
            <div style="display: flex; align-items: center;">
            <div style="width: 15px; height: 15px; margin: 3px; border: 1px solid black; background-color: darkred; opacity: 0.8;"></div>
            <span style="margin-right: 5px;">Tony com maior porecentagem</span>
            </div>
            <div style="display: flex; align-items: center;">
            <div style="width: 15px; height: 15px; margin: 3px; border: 1px solid black; background-color: orange; opacity: 0.8;"></div>
            <span style="margin-right: 5px;">Empate entre Elisa e Tony</span>
            </div>
            </div>
            </div>
            '''

        # Adiciona as legendas ao mapa
        m.get_root().html.add_child(folium.Element(legend1_html))
        m.get_root().html.add_child(folium.Element(legend2_html))

        # Salva o mapa interativo como um arquivo HTML
        m.save('templates/mapa.html')

        # Redireciona para a página com o mapa
        return render_template('mapa.html')
    else:
        return render_template('form.html')

def get_color(region_leader):
    if region_leader == 'Elisa':
        return 'darkgreen'  # Elisa como líder
    elif region_leader == 'Tony':
        return 'darkred'  # Tony como líder
    #elif region_leader == 'Nenhum':
        #return 'yellow'  # Nenhum como líder
    else:
        return 'orange'  # Empate ou outro caso

if __name__ == '__main__':
    app.run(debug=True)
