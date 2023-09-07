DEPUIS LA MACHINE: 

ssh -i <nom_de_votre_clé> ec2-user@<addresse_ip>:<chemin_sur_l'instance>

scp -i <nom_de_votre_clé> <nom_de_votre_clé> ec2-user@<addresse_ip>:<chemin_sur_l'instance>

DEPUIS CONTROLLEUR: 

sudo yum install pip
pip install ansible
sudo yum install git

chmod +x force-git-pull.sh