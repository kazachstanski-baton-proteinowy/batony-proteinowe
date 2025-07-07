from flask import Flask, render_template, request, redirect, flash, url_for
import re

app = Flask(__name__)
app.secret_key = 'tajny_klucz'

EMAIL_REGEX  = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

def validate_form_data(data):
    errors = {}
    if not data.get('name'):
        errors['name'] = 'Imie jest wymagane.'
    if not data.get('email') or not re.match(EMAIL_REGEX, data['email']):
        errors['email'] = 'Poprawny email jest wymagany.'
    if not data.get('message'):
        errors['message'] = 'Wiadomosc nie moze byc pusta.'

    return (len(errors) == 0), errors

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

@app.route('/kontakt', methods=['GET', 'POST'])
def kontakt():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name', '').strip(),
            'email': request.form.get('email', '').strip(),
            'message': request.form.get('message', '').strip()
        }
        is_valid, errors = validate_form_data(data)
        if is_valid:
            flash('Wiadomosc zostala wyslana!', 'success')
            return redirect(url_for('kontakt'))
        else:
            for field, msg in errors.items():
                flash(f"{field}: {msg}", 'error')
            return render_template('contact.html', data=data)

    return render_template('contact.html', data={})

if __name__ == '__main__':
    app.run(debug=True)
