import subprocess


def get_ip_address():
    #PASSONS PAR LA VERIFICATION DE L'IP
    resultat = subprocess.run(
        ["hostname", "-I"], stdout=subprocess.PIPE, text=True, check=True
    )
    return resultat.stdout.strip()


def check_connectivity():
    resultat = subprocess.run(
        ["ping", "-c", "1", "8.8.8.8"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if resultat.returncode == 0:
        return "Connecté (Internet OK)"
    else:
        return "Non connecté"