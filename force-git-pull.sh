#!/bin/bash

# Se rendre dans le répertoire du dépôt Git
#cd /chemin/vers/votre/depot

# Récupérer toutes les modifications des branches distantes
git fetch --all

# Réinitialiser votre branche actuelle pour correspondre à la branche distante spécifiée (changez branch-name)
git reset --hard origin

# Afficher un message de confirmation
echo "Git pull forcé effectué avec succès."
