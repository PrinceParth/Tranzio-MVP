from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text", "")
    target_lang = data.get("target_lang", "fr")

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    print("👑 Tranzio MVP: Language Queen is now LIVE on http://localhost:9347 👑")
    app.run(debug=True, port=9347)
