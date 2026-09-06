# Tuto : créer un script Python reproductible

Ce dossier explique comment structurer un petit projet Python — un fichier
`.py`, un environnement virtuel et un fichier `requirements.txt` — pour que
le code fonctionne de la même façon sur n'importe quelle machine. On termine
avec un exemple concret : un script d'analyse de fichier CSV avec une
visualisation.

## 1. Pourquoi un environnement virtuel ?

Un environnement virtuel (`venv`) isole les librairies installées pour un
projet donné, sans toucher à l'installation Python globale de la machine.
Cela évite deux problèmes courants :

- des projets différents qui ont besoin de versions différentes d'une même
  librairie (ex. pandas 1.x pour l'un, pandas 2.x pour l'autre) ;
- un script qui fonctionne "chez moi" mais plante chez quelqu'un d'autre
  parce que les versions installées ne sont pas les mêmes.

Le fichier `requirements.txt` liste ces librairies avec leur numéro de
version exact. C'est ce qui rend le projet **reproductible** : n'importe qui
(vous dans six mois, un collègue, un correcteur) peut recréer exactement le
même environnement en une seule commande.

## 2. Créer le script

Un projet minimal, c'est juste un dossier avec un fichier `.py` dedans :

```
mon_projet/
└── analyse.py
```

## 3. Créer l'environnement virtuel

Dans un terminal PowerShell, à la racine du projet :

```powershell
python -m venv venv
```

Cela crée un dossier `venv/` (à ne pas mettre dans Git — voir `.gitignore`).

Activez-le :

```powershell
.\venv\Scripts\Activate
```

Vous verrez `(venv)` apparaître au début de la ligne de commande, signe que
les commandes `python` et `pip` utilisent maintenant l'environnement du
projet et non l'installation globale.

Installez ensuite les librairies nécessaires :

```powershell
pip install pandas matplotlib
```

## 4. Figer les versions dans requirements.txt

Une fois les librairies installées, on génère le fichier qui décrit
l'environnement :

```powershell
pip freeze > requirements.txt
```

Le fichier ressemble à celui fourni dans ce dossier :

```
pandas==3.0.5
matplotlib==3.11.1
```

Le `==` fixe une version précise plutôt qu'une version minimale : c'est ce
détail qui garantit la reproductibilité (sans lui, une mise à jour future de
pandas pourrait changer le comportement du script sans qu'on s'en rende
compte).

## 5. Reproduire l'environnement ailleurs

C'est là que le travail des étapes précédentes paie. Sur une autre machine
(ou après un `git clone` du projet) :

```powershell
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

Trois commandes suffisent à retrouver un environnement identique, avec
exactement les mêmes versions de librairies.

## Script d'exemple : `analyse_csv.py`

[`analyse_csv.py`](analyse_csv.py) est un script minimaliste qui :

1. charge un fichier CSV avec `pandas` (par défaut
   [`data/notes_etudiants.csv`](data/notes_etudiants.csv)) ;
2. affiche un aperçu des données et quelques statistiques descriptives
   (moyenne, min, max, etc.) ;
3. trace un graphique en barres des notes avec `matplotlib`, l'enregistre en
   PNG (`notes_etudiants.png`) et l'affiche à l'écran.

## Lancer le script

Toujours avec l'environnement virtuel activé, depuis le dossier
`tuto_scripts/` :

```powershell
python analyse_csv.py
```

Pour analyser un autre fichier CSV, passez son chemin en argument :

```powershell
python analyse_csv.py data\mon_fichier.csv
```

## Structure du dossier

- **README.md** — ce tutoriel.
- **requirements.txt** — dépendances figées (`pandas`, `matplotlib`).
- **analyse_csv.py** — le script d'analyse et de visualisation.
- **data/notes_etudiants.csv** — jeu de données d'exemple.
