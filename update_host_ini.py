import boto3

# Remplacez 'votre_region_aws' par la région AWS appropriée, par exemple 'us-east-1'.
region = 'votre_region_aws'

# Créez une session AWS.
session = boto3.Session(region_name=region)

# Créez un client EC2.
ec2_client = session.client('ec2')

# Lire le fichier hosts.ini et extraire les noms d'instances
instances_a_recuperer = []

with open('hosts.ini', 'r') as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            parts = line.split()
            if len(parts) > 0:
                instance_name = parts[0]
                instances_a_recuperer.append(instance_name)

# Dictionnaire pour stocker les adresses IP publiques
adresses_ip_publiques = {}

# Récupérez les adresses IP publiques des instances EC2 spécifiées
response = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': instances_a_recuperer}])
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_name = None
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break
        if instance_name:
            adresses_ip_publiques[instance_name] = instance['PublicIpAddress']

# Mettre à jour le fichier hosts.ini avec les nouvelles adresses IP publiques
with open('hosts.ini', 'r') as f:
    lines = f.readlines()

with open('hosts.ini', 'w') as f:
    for line in lines:
        if line[0].strip() == "[":
            f.write("\n"+line)
        if line.strip() and not line.startswith('#'):
            parts = line.split()
            if len(parts) > 0:
                instance_name = parts[0]
                if instance_name in adresses_ip_publiques:
                    new_ip = adresses_ip_publiques[instance_name]
                    f.write(f"{instance_name} ansible_host={new_ip} ansible_ssh_private_key_file=/home/ec2-user/ansible_vincent.pem ansible_user=ec2-user\n")
                else:
                    f.write(line)
        else:
            f.write(line)

print("Le fichier hosts_updated.ini a été créé avec les nouvelles adresses IP publiques.")
