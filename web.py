import webbrowser

def ouvrir_site(url):
    """Ouvre le site web spécifié dans le navigateur par défaut."""
    webbrowser.open_new_tab(url)
print("\n✨OUVRIR UN SITE WEB AVEC LE MODULE WEBBROWSER✨\n")
url = input("Entrez l'URL du site à ouvrir (ex: https://www.python.org) : ")
print(f"Ouverture du site : {url}")
ouvrir_site(url)

