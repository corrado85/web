from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Vai su /esegui per lanciare il codice.'

@app.route('/esegui')
def esegui():
    # Il tuo codice da eseguire
    risultato = "Codice eseguito!"
    print("Ho eseguito il codice!")  # visibile nei log Render
    return risultato

if __name__ == '__main__':
    app.run()
