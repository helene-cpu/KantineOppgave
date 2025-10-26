from flask import Flask, render_template

app= Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/meny')
def meny():
    meny_kantine=[
        {"dag": "mandag", "rett": "Grønnsakssuppe", "bilde": "/static/images/suppe.jpg", "beskrivelse": "Grønnsaks suppe med gulrøtter, pølser og kjøttboller", "allergier": "Inneholder: Svin"},
        {"dag": "tirsdag", "rett": "Pastasalat", "bilde": "/static/images/pastasalat.jpg", "beskrivelse": "varm salat med pasta og masse næringsrike grønnsaker","allergier": "Inneholder: Gluten"},
        {"dag": "Onsdag", "rett": "Laks og potet", "bilde": "/static/images/laks.jpg", "beskrivelse": "En laksefilet per person, med potet og revet gulrot"},
        {"dag": "Torsdag", "rett": "Vegetarlasagne", "bilde": "/static/images/lasagne.jpg","beskrivelse": "Vegetar lasagne med ostesaus på toppen", "allergier": "Inneholder: Gluten, Laktose"},
        {"dag": "Fredag", "rett": "Wok", "bilde": "/static/images/wok.jpg", "beskrivelse": "nudler med grønnsaker og saus"}
        ]
    return render_template("meny.html", kantine=meny_kantine)

@app.route('/varer')
def varer():
    varer_kantine=[
        {"vare": "Litago", "pris": "26", "bilde": "/static/images/litago.png"},
        {"vare": "Iskaffe", "pris": "28", "bilde": "/static/images/iskaffe.png"},
        {"vare": "Coca Cola", "pris": "32", "bilde": "/static/images/coca-cola.png"},
        {"vare": "Iste", "pris": "30", "bilde": "/static/images/iste.png"},
        {"vare": "Påsmurte rundstykker", "pris": "29", "bilde": "/static/images/rundstykke.png"},
        {"vare": "Baguetter", "pris": "29", "bilde": "/static/images/baguette.png"},
        {"vare": "Knekkebrød", "pris": "18", "bilde": "/static/images/knekkebrod.png"},
        {"vare": "Sjokolade", "pris": "29", "bilde": "/static/images/sjokolade.png"}
    ]
    return render_template("varer.html", mat=varer_kantine)

@app.route('/kontakt')
def kontakt():
    ansatte_kantine=[
        {"navn": "Thea", "stilling": "Sint kokk", "bilde": "/static/images/thea.jpg", "kommentar": "Alltid 2 sekunder fra å kaste sleiva, men maten er fantastisk", "epost": "matmedaggresjon@akademiet.no", "tlf": "+47 12345678"},
        {"navn": "Markus", "stilling": "Dessertdirektør", "bilde": "/static/images/markus.jpg", "kommentar": "Den virkelige maktpersonen i kantina", "epost": "sjefssukker@akademiet.no", "tlf": "+47 21436587"},
        {"navn": "Ebbe", "stilling": "Vaskedame", "bilde": "/static/images/ebbe.jpg", "kommentar": "Tar kampen mot støv- taper hver gang", "epost": "vaskedronning@akademiet.no", "tlf": "+47 87654321"},
        {"navn": "Ludvig", "stilling": "Matfilosof", "bilde": "/static/images/ludvig.jpg", "kommentar": "spør- hva er egentlig til lunsj?", "epost": "eksistensiellkokk@akademiet.no", "tlf": "+47 67676767"},
        {"navn": "Nikolai", "stilling": "Uhygenisk oppvaskmester", "bilde": "/static/images/nikolai.jpg", "kommentar": "Skyller tallerkner med optimisme og luft", "epost": "rentnok@akademiet.no", "tlf": "+47 76767676"},
        {"navn": "Audun", "stilling": "Usunn ernæringsfysiolog", "bilde": "/static/images/audun.jpg", "kommentar": "Anbefaler pommes frites som grønnsak", "epost": "usunnveileder@akademiet.no", "tlf": "+47 34561278"}
    ]
    return render_template("kontakt.html",ansatte=ansatte_kantine )

    
if __name__ == "__main__":
    app.run(debug=True)