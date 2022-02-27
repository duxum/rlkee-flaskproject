from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

def handle_translation(request, func):
    text = request.args.get('textToTranslate')

    return func(text)
 
@app.route("/englishToFrench")
def english_to_spanish():
    return handle_translation(request, translator.english_to_french)

@app.route("/frenchToEnglish")
def french_to_english():
    return handle_translation(request, translator.french_to_english)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
