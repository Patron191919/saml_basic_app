from flask import Flask, redirect, url_for, session, request
import config
from onelogin.saml2.auth import OneLogin_Saml2_Auth
import base64
from xml.dom.minidom import parseString

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

def prepare_flask_request(request):
    # Flask'tan gelen isteği OneLogin için düzenler
    url_data = request.host_url
    return {
        'https': 'on' if request.scheme == 'https' else 'off',
        'http_host': request.host,
        'server_port': request.host.split(':')[1] if ':' in request.host else ('443' if request.scheme == 'https' else '80'),
        'script_name': request.path,
        'get_data': request.args.copy(),
        'post_data': request.form.copy()
    }

@app.route('/')
def home():
    if 'firstname' in session and 'lastname' in session:
        return f'İyi günler, {session["firstname"]} {session["lastname"]}! site3\'de oturum açtınız.'
    return redirect(url_for('login'))

@app.route('/login')
def login():
    req = prepare_flask_request(request)
    auth = OneLogin_Saml2_Auth(req, config.SAML_SETTINGS)
    return redirect(auth.login())

@app.route('/callback', methods=['GET', 'POST'])
def saml_callback():
    req = prepare_flask_request(request)
    auth = OneLogin_Saml2_Auth(req, config.SAML_SETTINGS)
    
    auth.process_response()
    errors = auth.get_errors()
    saml_response = request.form['SAMLResponse']
    decoded_saml_response = base64.b64decode(saml_response)
    print(parseString(decoded_saml_response).toprettyxml())

    if not errors:
        # Kullanıcı bilgilerini SAML yanıtından Attribute olarak çek
        attributes = auth.get_attributes()

        # İsim ve soyadı SAML yanıtından çekip session'a kaydet
        session['firstname'] = attributes.get('http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname', [''])[0]
        session['lastname'] = attributes.get('http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname', [''])[0]

        return redirect(url_for('home'))
    else:
        return f'Hata: {errors}', 500

if __name__ == '__main__':
    app.run(port=5003)
