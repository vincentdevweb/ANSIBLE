import boto3

# Remplacez 'votre_region_aws' par la région AWS appropriée, par exemple 'us-east-1'.
region = 'votre_region_aws'

# Créez une session AWS.
session = boto3.Session(region_name=region)

# Créez un client EC2.
ec2_client = session.client('ec2')

# Dictionnaire pour stocker les adresses IP publiques
adresses_ip_publiques = {}

# Récupérez les adresses IP publiques de toutes les instances EC2
response = ec2_client.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_name = None
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break
        if instance_name:
            adresses_ip_publiques[instance_name] = instance['PublicIpAddress']

# Générer le contenu du fichier hosts.ini à partir du dictionnaire
with open('hosts.ini', 'w') as f:
    for instance_name, ip in adresses_ip_publiques.items():
        f.write(f"{instance_name} ansible_host={ip} ansible_ssh_private_key_file=/home/ec2-user/ansible_vincent.pem ansible_user=ec2-user\n")

print("Le fichier hosts.ini a été généré avec les nouvelles adresses IP publiques.")
