import subprocess


def get_hostname():
    resultat = subprocess.run(
        ["hostname"], stdout=subprocess.PIPE, text=True, check=True
    )
    return resultat.stdout.strip()


def get_disk_space():
    resultat = subprocess.run(
        ["df", "-h", "/"], stdout=subprocess.PIPE, text=True, check=True
    )
    return resultat.stdout.strip()