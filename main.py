dict = {
    "ransomware": "Le malware de rançonnage est un type de malware qui empêche les utilisateurs d'accéder à leur système ou à leurs fichiers personnels et exige le paiement d'une rançon",
    "phishing": "L'hameçonnage (phishing en anglais) est une technique frauduleuse destinée à leurrer l'internaute pour l'inciter à communiquer des données personnelles",
    "ctf": "Capture The Flag (Capture de Drapeau). Mode de jeu dans lequel plusieurs attaquants doivent trouver un flag contenu dans un code ou cachée par des stratégies diverses.",
    "cyber": "Préfixe généralement utilisé pour signifier une dimension informatique et réseau à la notion qu'il accompagne",
    "cheval de troie": "Le cheval de Troie est un logiciel en apparence légitime, mais qui contient une fonctionnalité malveillante. Son but est de faire entrer cette fonctionnalité malveillante dans l'ordinateur",
    "tools": "Les outils de cybersécurité sont les différentes applications ou logiciels utilisés par les entreprises pour protéger leurs systèmes et leurs réseaux.",
    "virus": "Un virus informatique utilise son hôte (l'ordinateur qu'il infecte) pour se reproduire et se transmettre à d'autres ordinateurs",
    "botnet": "Un botnet est un groupe d'ordinateurs ou de dispositifs sous le contrôle d'un attaquant, utilisé pour mener des activités malveillantes contre une victime ciblée",
    "osint": "Le terme désigne tout simplement l'exploitation de sources d'information accessibles à tout un chacun",
    "reverse": "La rétro-ingénierie dans une FFC consiste généralement à prendre un programme compilé et à le reconvertir dans un format plus lisible pour l'homme.",
    "hardware": "Les éléments matériels d'un système informatique.",
    "software": "Ensemble des moyens d'utilisation, programmes, procédures, documentation d'un système informatique",
    "hack": "Il s'agit de l'obtention d'un accès non autorisé aux données d'un système ou d'un ordinateur.",
    "bypass": "Annuler les dispositifs de sécurité en cas de piratage, ou modifier ce que l'on fait en cas de dépannage",
    "vuln": "Une faille ou une faiblesse dans un système informatique, pouvant être exploitée pour violer la politique de sécurité du système.",
    "bug bounty": "Un Bug Bounty est une récompense financière offerte aux hackers éthiques pour avoir découvert et signalé une vulnérabilité ou un bug à un développeur d'application"
}

u = True

print("\033[93m      d8b      \033[0m")
print("\033[93m      88P  `8P           d8P\033[0m")
print("\033[93m     d88              d888888P\033[0m")
print("\033[93m d888888    88b d8888b  ?88'       .d888b,  88bd88b d8888b\033[0m")
print("\033[93md8P' ?88    88Pd8P' `P  88P        ?8b,     88P'  `d8P' `P\033[0m")
print("\033[93m88b  ,88b  d88 88b      88b          `?8b  d88     88b\033[0m")
print("\033[93m`?88P'`88bd88' `?888P'  `?8b      `?888P' d88'     `?888P'\033[0m")

while u is True:
    print("\033[92m--------------------------------------------------------------------------\033[0m")
    print("\033[95m[1] = Get the definition\033[0m, \033[94m[2] = Add to dictionnary\033[0m, \033[91m[3] Remove from dictionnary\033[0m, \033[93m[4] Show the entire dictionnary\033[0m")
    choice = input("Choice = ")
    if choice == "1":
        a = str(input("Enter a word : "))
        if a in dict.keys():
            print("Definition of\033[97m", a, "\033[0m:", dict.get(a))
        else:
            print("\033[91mThis word is not present in this dictionary\033[0m")
            print("\033[91mTry to add him with option 2\033[0m")

    if choice == "2":
        word = str(input("Word = ", ))
        definition = str(input("Definition = ", ))
        dict[word]=definition
        print("\033[92mSuccessfully add to the dictionary\033[0m")

    if choice == "3":
        b = str(input("Remove the word : "))
        if b in dict.keys():
            dict.pop(b)
            print("\033[92mSuccessfully removed\033[0m")
        else:
            print("\033[91mThis word is not present in this dictionary\033[0m")
            print("\033[91mTry to add him with option 2\033[0m")

    if choice == "4":
        password = str('root')
        user_data = input("Password : ")
        if password == user_data:
            for key in dict:
                y = key
                print("\033[97m", y, '\033[0m=', dict.get(y))
        else:
            print("\033[91mWrong Password !\033[0m")

    else:
        pass


