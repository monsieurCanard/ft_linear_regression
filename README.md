<!-- <img src=https://github.com/monsieurCanard/42Graphics/blob/main/Abstract2.png> -->
```
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      | <-- Salut ! Moi c'est Bob, vendeur de voitures d'occasion !
  |\     |_|     /|     Laisse-moi deviner le prix de ta caisse...
  | \           / |
   \| /  ___  \ |/
    \ | / _ \ | /
     \_________/
      _|_____|_
 ____|_________|____
/                   \
```
<div align="center">
<h1>ft_linear_regression 🤖💰 </h1>
</div>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Active-success.svg?style=for-the-badge" alt="Status">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-lightgrey.svg?style=for-the-badge" alt="Platform">
</p>

##
Rencontrez **Bob**, votre vendeur de voitures d'occasion préféré (et légèrement cynique) ! Depuis 20 ans, Bob achète des voitures et il a développé un sixième sens pour estimer leur prix. Ce projet implémente un modèle de régression linéaire qui reproduit l'expertise de Bob pour prédire le prix d'une voiture en fonction de son kilométrage. 📊

## 🚗 Description

Bob utilise une formule mathématique simple mais efficace :

```
estimatePrice(mileage) = θ₀ + (θ₁ × mileage)
```

**Où :**
- `θ₀` : Le prix de base (intercept/bias)
- `θ₁` : La dépréciation par kilomètre (coefficient)
- `mileage` : Le kilométrage de la voiture (normalisé)

Le modèle utilise la **descente de gradient** pour ajuster ces paramètres et minimiser l'erreur entre les prix estimés et réels. Les données sont **standardisées** pour améliorer la convergence de l'algorithme.

## 🚀 Installation

```bash
git clone https://github.com/monsieurCanard/ft_linear_regression.git
cd ft_linear_regression
pip install numpy matplotlib
```

## 📖 Utilisation

### Mode Interactif Complet (Bob vous guide)

```bash
python3 prog.py
```

Entrez le kilométrage de votre voiture et laissez Bob faire le reste : entraînement du modèle, prédiction, et vérification de la précision !

### Options en Ligne de Commande

**Entraîner le modèle :**
```bash
python3 prog.py --train
```

**Prédire le prix d'une voiture :**
```bash
python3 prog.py --predict 150000
```

**Visualiser la régression :**
```bash
python3 prog.py --vizualize
```

**Vérifier la précision du modèle :**
```bash
python3 prog.py --verify
```

**Combiner plusieurs options :**
```bash
python3 prog.py --vizualize --predict 80000
```

## 📁 Structure du Projet

```
ft_linear_regression/
│
├── prog.py                    # Point d'entrée principal avec CLI
├── trainer_model.py           # Entraînement par descente de gradient
├── predict_model.py           # Prédiction des prix
├── verifyer_model.py          # Calcul de la précision (MAE)
├── interface_prog.py          # Interface ASCII de Bob
│
└── dataset/
    ├── data_train.csv         # Données d'entraînement (km, prix)
    └── output_train_data.csv  # Paramètres θ₀, θ₁, mean, std
```

## 🧮 Algorithme

### 1. Standardisation des Données

Pour améliorer la convergence :

```python
km_normalized = (km - km_mean) / km_std
```

### 2. Descente de Gradient

Mise à jour itérative des paramètres :

```python
θ₀ = θ₀ - α × (1/m) × Σ(error)
θ₁ = θ₁ - α × (1/m) × Σ(error × km)
```

**Paramètres :**
- Learning rate (α) : `0.1`
- Itérations : `10,000`
- Métrique : Mean Absolute Error (MAE)

### 3. Prédiction

```python
price = θ₀ + θ₁ × ((km - km_mean) / km_std)
```

## 📊 Performance

Le modèle atteint généralement une précision de **~8-10%** d'erreur moyenne absolue sur le jeu de données d'entraînement, ce qui signifie que Bob se trompe rarement de plus de quelques centaines d'euros !

## 🎨 Fonctionnalités

✨ **Interface ASCII interactive** avec Bob le vendeur  
📈 **Visualisation graphique** de la régression linéaire  
🎲 **Répliques aléatoires** de Bob (parfois sarcastiques)  
⚡ **CLI flexible** avec argparse  
🧪 **Validation du modèle** avec métriques de précision  
🔢 **Normalisation automatique** des données  

## 🛠️ Détails Techniques

**Bibliothèques utilisées :**
- `numpy` : Calculs vectorisés et opérations mathématiques
- `matplotlib` : Visualisation de la régression
- `csv` : Lecture/écriture des données
- `argparse` : Interface en ligne de commande

**Format des données :**
- Entrée : `km, price` (CSV)
- Sortie : `θ₀, θ₁, km_mean, km_std` (CSV)

## 🎭 Rencontrez Bob

Bob n'est pas votre vendeur de voitures ordinaire. Avec 20 ans d'expérience et un sens de l'humour douteux, il vous proposera des estimations de prix accompagnées de commentaires tels que :

> *"Je pourrais accepter… si je veux faire semblant d'avoir un cœur."*

> *"C'est une voiture, pas un miracle, mais je suppose que tu fais ce que tu peux."*

## 📝 Exemple de Session

```
$ python3 prog.py

-- Welcome to FT Linear Regression Program --
       -------
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      | 
  |\     |_|     /|
  | \           / |
   \| /  ___  \ |/ <-- A combien de kilomètres est votre voiture ?
    \ | / _ \ | / 
     \_________/
      _|_____|_
 ____|_________|____
/                   \

> 120000

       -------   
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      |  
  |\     |_|     /|
  | \           / |
   \| /  ___  \ |/ 
    \ | / _ \ | /  <--- Faites moi voir votre voiture !
     \_________/        Je vais l'analyser et aller chercher mes données...
      _|_____|_
 ____|_________|____
/                   \

       -------   
     _/       \_
    / |       | \
   /  |__   __|  \
  |__/((o| |o))\__|
  |      | |      |  
  |\     |_|     /|
  | \           / |
   \| /  ___  \ |/ 
    \ | / _ \ | /  <--- D'après mes calculs, votre voiture vaut : 4250.75 €
     \_________/        Pour ce prix, je devrais presque t'envoyer un message de condoléances.
      _|_____|_
 ____|_________|____
/                   \

                                             |
                                         |
                                         |
                                         |
   _______                   ________    |
  |ooooooo|      ____       | __  __ |   |
  |[]+++[]|     [____]      |/  \/  \|   |
  |+ ___ +|     ]()()[      |\__/\__/|   |
  |:|   |:|   ___\__/___    |[][][][]|   |
  |:|___|:|  |__|    |__|   |++++++++|   |
  |[]===[]|   |_|_/\_|_|    | ______ |   |
_ ||||||||| _ | | __ | | __ ||______|| __|
  |_______|   |_|[::]|_|    |________|   \
              \_|_||_|_/               jro\
                |_||_|                     \
               _|_||_|_                     \
      ____    |___||___|                     \
     /  __\          ____                     \
     \( oo          (___ \                     \
     _\_o/           oo~)/ <-- Bob a acheté une voiture de 120000.0 km pour 4250.75 €
    / \|/ \         _\-_/_     Il a raté de 8.8% ses estimations !
   / / __\ \___    / \|/  \    C'est vraiment du super boulot ! Et c'est gratis !
   \ \|   |__/_)  / / .- \ \   
    \/_)  |       \ \ .  /_/ <-- Mais faudrait peut être faire quelque chose
     ||___|        \/___(_/      pour améliorer son caractère non ?   
     | | |          | |  |       Ça fait 20 ans qu'il est comme ça ! 
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___])
```

---

*Fait avec ❤️ (et beaucoup de sarcasme) par Bob et son créateur* 🚗💨
