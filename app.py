from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    produkty = [
        {
            'nazwa': 'Baton Proteinowy XYZ',
            'opis': 'Baton XYZ zawiera 20g białka i idealnie nadaje się po treningu.',
            'obraz': 'images/baton2.jpg'
        },
        {
            'nazwa': 'Baton Proteinowy ABC',
            'opis': 'Baton ABC to zdrowa przekąska z dodatkiem orzechów i kakao.',
            'obraz': 'images/baton3.jpg'
        }
    ]
    return render_template('index.html', produkty=produkty)

@app.route('/kontakt')
def kontakt():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
