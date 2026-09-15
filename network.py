import subprocess


def get_ip_address():
    """Récupère l'adresse IP locale."""
    resultat = subprocess.run(
        ["hostname", "-I"], stdout=subprocess.PIPE, text=True, check=True
    )
    return resultat.stdout.strip()


def check_connectivity():
    """Vérifie la connectivité vers une passerelle externe."""
    resultat = subprocess.run(
        ["ping", "-c", "1", "8.8.8.8"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if resultat.returncode == 0:
        return "Connecté (Internet OK)"
    else:
        return "Non connecté"