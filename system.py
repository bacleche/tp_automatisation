import subprocess


def get_hostname():
    """Récupère le nom de la machine."""
    resultat = subprocess.run(
        ["hostname"], stdout=subprocess.PIPE, text=True, check=True
    )
    return resultat.stdout.strip()


def get_disk_space():
    """Récupère l'espace disque de la racine."""
    resultat = subprocess.run(
        ["df", "-h", "/"], stdout=subprocess.PIPE, text=True, check=True
    )
    return resultat.stdout.strip()