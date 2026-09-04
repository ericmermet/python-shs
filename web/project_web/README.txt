
# Projet Web Flask : Application de Prise de Notes

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
1. **Python 3.x** : Téléchargez et installez Python depuis [python.org](https://www.python.org/downloads/). Assurez-vous que `pip` est inclus.
2. **Git** : Téléchargez et installez Git depuis [git-scm.com](https://git-scm.com/).
3. **Visual Studio Code** : Téléchargez et installez VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/).

---

## Étapes d'installation

### 1. Récupérer le code depuis un dépôt Git
1. Ouvrez une fenêtre **PowerShell** ou **Invite de commandes**.
2. Clonez le dépôt Git contenant le projet :

   git clone <URL_DU_DEPOT_GIT>

   Remplacez `<URL_DU_DEPOT_GIT>` par l'URL du dépôt contenant le projet.

3. Déplacez-vous dans le répertoire du projet :

   cd <NOM_DU_DEPOT>


4. Accédez au sous-dossier contenant le projet Flask :

   cd project_web


---

### 2. Créer un environnement virtuel Python
1. Créez un environnement virtuel avec Python 3 :

   python -m venv venv


2. Activez l'environnement virtuel :
   - Si vous utilisez PowerShell :

     .\venv\Scripts\Activate

   - Si vous utilisez l'Invite de commandes :

     venv\Scripts\Activate.bat


   Une fois activé, vous verrez `(venv)` apparaître au début de la ligne de commande.

3. Installez les dépendances du projet :

   pip install -r requirements.txt


---

### 3. Configurer Visual Studio Code
1. Ouvrez le répertoire **project_web** dans Visual Studio Code :

   code .


2. Configurez l'environnement Python :
   - Cliquez sur **Ctrl + Maj + P** pour ouvrir la palette de commandes.
   - Tapez `Python: Select Interpreter` et appuyez sur Entrée.
   - Sélectionnez l'interpréteur Python associé à votre environnement virtuel (`venv`).

3. Assurez-vous que les extensions suivantes sont installées dans VS Code :
   - **Python** : Extension officielle pour Python.
   - **Code Runner** (optionnel) : Pour exécuter facilement des scripts.

---

### 4. Lancer l'application
1. Assurez-vous que l'environnement virtuel est activé :

   .\venv\Scripts\Activate


2. Lancez l'application Flask :

   python app.py


3. Une fois le serveur lancé, vous verrez un message indiquant :

   Running on http://127.0.0.1:5000


4. Ouvrez votre navigateur et accédez à l'URL suivante :

   http://127.0.0.1:5000


---

## Notes supplémentaires

- Si vous rencontrez des problèmes, vérifiez les points suivants :
  - Python est bien installé et accessible via la commande `python`.
  - L'environnement virtuel est correctement activé.
  - Toutes les dépendances sont installées (via `pip install -r requirements.txt`).
- Si vous souhaitez arrêter l'application Flask, appuyez sur **Ctrl + C** dans le terminal.

---

## Structure du projet

- **app.py** : Fichier principal contenant l'application Flask.
- **templates/** : Dossier contenant les fichiers HTML.
- **static/** : Dossier contenant les fichiers CSS et JavaScript.
- **requirements.txt** : Liste des dépendances Python nécessaires au projet.

---

## Crédits
Développé par Eric Mermet (CNRS) dans le cadre d'une formation Python avec Flask.