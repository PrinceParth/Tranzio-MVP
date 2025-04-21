from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)
CORS(app)

# 🌟 Fake user data for dashboard (can be upgraded to real DB)
user_data = {
    "name": "Parth",
    "xp": 1420,
    "streak": 9,
    "words_learned": 320,
    "translations": [
        {"input": "Bonjour", "output": "Hello"},
        {"input": "Merci", "output": "Thank you"},
        {"input": "Chat", "output": "Cat"}
    ]
}

# 🌍 Home Page
@app.route("/")
def index():
    return render_template("index.html")

# 🔁 Translate Route (AJAX)
@app.route("/translate", methods=["POST"])
def translate_text():
    data = request.get_json()
    text = data.get("text", "")
    target_lang = data.get("target_lang", "fr")

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        
        # Log to user_data
        user_data["xp"] += 10  # simulate XP reward
        user_data["words_learned"] += 1
        user_data["translations"].insert(0, {"input": text, "output": translated})
        if len(user_data["translations"]) > 10:
            user_data["translations"].pop()
        
        return jsonify({"translated_text": translated})
    except Exception as e:
        return jsonify({"error": str(e)})

# 👑 Admin Panel Route
@app.route("/admin")
def admin_panel():
    return render_template("admin.html", user=user_data)

@app.route("/save", methods=["POST"])
def save_user_data():
    data = request.get_json()
    print("⭐ XP:", data.get("xp"), "🔥 Streak:", data.get("streak"))
    return jsonify({"status": "saved"})

# 🚀 Launch Server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 9347))
    print(f"👑 Tranzio MVP: Language Queen is now LIVE on http://localhost:{port} 👑")
    app.run(host="0.0.0.0", port=port, debug=True)
