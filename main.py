from network import check_connectivity, get_ip_address
from report import generate_report
from system import get_disk_space, get_hostname


def main():
    print("Lancement de la vérification système...")

    # Collecte des données
    hostname = get_hostname()
    ip = get_ip_address()
    connectivity = check_connectivity()
    disk = get_disk_space()

    # Génération du rapport
    generate_report(hostname, ip, connectivity, disk)


if __name__ == "__main__":
    main()