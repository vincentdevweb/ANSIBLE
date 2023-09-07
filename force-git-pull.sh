#!/bin/bash

# Se rendre dans le répertoire du dépôt Git
#cd /chemin/vers/votre/depot

# Récupérer toutes les modifications des branches distantes
git fetch --all

# Nettoyer le répertoire (supprimer les fichiers non suivis et les fichiers ignorés)
git clean -fd

# Réinitialiser votre branche actuelle pour correspondre à la branche distante spécifiée (changez branch-name)
git reset --hard origin

# Afficher un message de confirmation
echo "Git pull forcé effectué avec succès."
