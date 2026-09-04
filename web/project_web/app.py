from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Liste des notes
notes = []

@app.route("/")
def index():
    """Afficher toutes les notes."""
    return render_template("index.html", notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    """Ajouter une nouvelle note."""
    title = request.form.get("title")  # Récupérer le titre
    content = request.form.get("content")  # Récupérer le contenu
    if title and content:  # Vérifier que le titre et le contenu sont non vides
        notes.append({"title": title, "content": content})  # Ajouter la note
    return redirect(url_for("index"))  # Revenir à la page principale

@app.route("/delete/<int:index>")
def delete_note(index):
    """Supprimer une note."""
    if 0 <= index < len(notes):  # Vérifier que l'index est valide
        notes.pop(index)  # Supprimer la note
    return redirect(url_for("index"))  # Revenir à la page principale

if __name__ == "__main__":
    app.run(debug=True)
