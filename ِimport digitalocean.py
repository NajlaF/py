ِimport digitalocean

token = 'YOUR_API_TOKEN'

manager = digitalocean.Manager(token=token)
droplets = manager.get_all_droplets()

for droplet in droplets:
    print(f"Name: {droplet.name}")
    print(f"IP Address: {droplet.ip_address}")
    print(f"Status: {droplet.status}")
    print("-----------------------------")
    pip install python-digitalocean