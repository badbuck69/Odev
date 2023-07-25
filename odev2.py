from flask import Flask, render_template,request
import requests

#uygulama oluşturma
app = Flask(__name__)
#Ana Sayfa
@app.route("/")
def index():
    return render_template("index.html")
# /pokemon adresine gönderilen get ve post işlemleri
@app.route("/pokemon", methods=['GET',"POST"])
def pokemon():
    if request.method == 'POST':
        pokename = request.form.get('pokename')
        result = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokename.lower()}")

        if pokename == '':
            return "Bad request", 400
        #Pokeapi den başarılı yanıt alınırsa
        elif result.status_code == 200:
            json_data = result.json()
            #pokemon.html şablonunu renderlayarak yanıt döndürülür
            return render_template('pokemon.html', result = json_data)
        elif result.status_code == 404:
            return "Not Found", 404

        else:
            return render_template('pokemon.html', result="Pokemon not found")
    #Eğer Get isteği gelirse
    else:        
        return render_template('pokemon.html') 
#Flask çalıştırılması
if __name__ == "__main__":
    app.run(port=3000, debug=True)