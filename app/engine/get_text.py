def get_err_msg(language:str):
    match language:
        case "Croatian":
            return "Unesite pitanje vezano uz hotel."
        case "Italian":
            return "Inserisci una domanda relativa all'azienda."
        case "German":
            return f"Geben Sie eine hotelbezogene Frage ein."
        case "French":
            return f"Saisissez une question relative à l'hôtel."
        case "Español":
            return "Introduzca una pregunta relacionada con el hotel."
        case _:
            return f"Enter a hotel-related question."
    
def get_set_language_text(language:str, sender_name:str):
    match language:
        case "Croatian":
            return f"""Pozdrav još jednom {sender_name}, slobodno pitajte što vas zanima.\n\nČesta pitanja su:\n- Koje vrsta soba postoje?\n- Ima li nekih događanja u blizini?\n- Koje vrste masaža nudite?\n- Jesu li dozvoljeni kućni ljubimci?"""
        case "Italian":
            return f"Ciao di nuovo {sender_name}, non esitare a chiedere cosa ti interessa.\n\nLe domande più frequenti sono:\n- Che tipi di camere ci sono?\n- Ci sono eventi nelle vicinanze?\n- Che tipi di massaggi offrite?\n- Sono ammessi animali domestici?"
        case "German":
            return f"Hallo nochmal {sender_name}, fragen Sie gerne, was Sie interessiert.\n\nHäufig gestellte Fragen sind:\n- Welche Zimmertypen gibt es?\n- Gibt es Veranstaltungen in der Nähe?\n- Welche Arten von Massagen Bieten Sie an?\n- Sind Haustiere erlaubt?"
        case "French":
            return f"Bonjour {sender_name}, n'hésitez pas à demander ce qui vous intéresse.\n\nLes questions fréquemment posées sont :\n- Quels types de salles y a-t-il ?\n- Y a-t-il des événements à proximité ?\n- Quels types de massages proposez-vous ?\n- Les animaux sont-ils autorisés ?"
        case "Español":
            return f"Hola de nuevo {sender_name}, no dudes en preguntar lo que te interese.\n\nLas preguntas frecuentes son:\n- ¿Qué tipos de habitaciones hay?\n- ¿Hay algún evento cerca?\n- ¿Qué tipos de masajes? ¿Ofrecen?\n- ¿Se permiten mascotas?"
        case _:
            return f"Hello again {sender_name}, feel free to ask what you are interested in.\n\nFrequently asked questions are:\n- What types of rooms are there?\n- Are there any events nearby?\n- What types of massages do you offer?\n- Are pets allowed?"

def get_contact_text(language:str, sender_name:str):
    match language:
        case "Croatian":
            return f"""Lista kontakta:\n\n- Recepcija: +385 (0)1 111 111\n- Posluga u sobu: +385 (0)1 222 222\n- Email: grandhotel@demo.email"""
        case "Italian":
            return f"Elenco contatti:\n\n- Reception: +385 (0)1 111 111\n- Servizio in camera: +385 (0)1 222 222\n- Email: grandhotel@demo.email"
        case "German":
            return f"Kontaktliste:\n\n- Rezeption: +385 (0)1 111 111\n- Zimmerservice: +385 (0)1 222 222\n- Email: grandhotel@demo.email"
        case "French":
            return f"Liste de contacts :\n\n- Réception : +385 (0)1 111 111\n- Room service : +385 (0)1 222 222\n- Email: grandhotel@demo.email"
        case "Español":
            return f"Lista de contactos:\n\n- Recepción: +385 (0)1 111 111\n- Servicio de habitaciones: +385 (0)1 222 222\n- Email: grandhotel@demo.email"
        case _:
            return f"Contact list:\n\n- Reception: +385 (0)1 111 111\n- Room service: +385 (0)1 222 222\n- Email: grandhotel@demo.email"
    