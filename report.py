def generate_report(hostname, ip, connectivity, disk):
    """Génère le rapport final sous forme de fichier texte."""
    filename = "rapport_systeme.txt"

    content = f"""========================================
       RAPPORT DE VERIFICATION SYSTEME
========================================
1. Nom de la machine : {hostname}
2. Adresse IP        : {ip}
3. Connectivité      : {connectivity}

4. Espace Disque     :
{disk}
========================================
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[+] Rapport généré avec succès : {filename}")

    print(content)