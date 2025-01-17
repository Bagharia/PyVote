import json
import os
from mongoDB.config.connection_db import get_database


def initialize_collections():
    db = get_database()
    if db is not None:
        try:
            # Liste des collections à créer
            collections_to_create = ["Users", "Ballots"]

            # Récupérer les collections existantes dans la base de données
            existing_collections = db.list_collection_names()

            # Parcourir les collections
            for collection in collections_to_create:
                if collection not in existing_collections:
                    # Créer la collection si elle n'existe pas
                    db.create_collection(collection)
                    print(f"Collection '{collection}' créée.")
                else:
                    print(f"Collection '{collection}' existe déjà.")
        except Exception as e:
            print(f"Erreur lors de l'initialisation des collections : {e}")


if __name__ == "__main__":
    initialize_collections()