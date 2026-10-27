def extraire_donnees_brutes(lines):
    records = []
    for line in lines:
        # TODO: Mettre en place un bloc try / except (ValueError, IndexError)
        
            # TODO: Extraire le timestamp situé entre crochets [...] et retirer les microsecondes.
            
            # TODO: Découper la fin de la ligne avec les séparateurs ':' ou '--', puis par '/'
            # TODO: Extraire lat, lon, alt et les convertir en float().
            
            # TODO: Ajouter le tuple (timestamp, lat, lon, alt) à la liste records
            pass
            
        # TODO: Dans le except, utiliser 'continue' pour ignorer la ligne
        
    return records