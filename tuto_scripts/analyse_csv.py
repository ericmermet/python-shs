"""Analyse minimaliste d'un fichier CSV : statistiques descriptives + graphique."""

import sys

import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else "data/notes_etudiants.csv"

df = pd.read_csv(CSV_PATH)

print("Aperçu des données :")
print(df.head(), "\n")

print("Statistiques descriptives (colonne 'Note') :")
print(df["Note"].describe())

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(df["Prénom"], df["Note"], color="#2a78d6")

ax.set_title("Notes des étudiants")
ax.set_xlabel("Étudiant")
ax.set_ylabel("Note")
ax.set_ylim(0, 20)
ax.spines[["top", "right"]].set_visible(False)
ax.set_axisbelow(True)
ax.grid(axis="y", color="#e1e0d9", linewidth=0.8)

plt.tight_layout()
plt.savefig("notes_etudiants.png", dpi=150)
print("\nGraphique enregistré dans notes_etudiants.png")

plt.show()
