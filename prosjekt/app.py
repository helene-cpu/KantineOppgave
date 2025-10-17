from flask import Flask, render_template

app= Flask(__name__)

varer_kantine=["Litago - 26,-", "Iskaffe - 28,-", "Coca Cola - 32,-   + pant", "Iste - 30,-   + pant", "Påsmurte Rundstykker - 25,-", "Baguetter - 29,-", "Knekkebrød -18,-", "Sjokolade - 29,-"]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/meny')
def meny():
    return render_template("meny.html")

@app.route('/varer')
def varer():
    return render_template("varer.html", mat=varer_kantine)

@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html")

    
if __name__ == "__main__":
    app.run()