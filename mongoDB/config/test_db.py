from config.connection_db import get_database

def test_database():
    db = get_database()
    if db:
        try:
            # Vérifiez les données dans la collection "Ballots"
            ballots = list(db.Ballots.find())
            print(f"Nombre de documents dans 'Ballots' : {len(ballots)}")

            # Vérifiez les données dans la collection "Users"
            users = list(db.Users.find())
            print(f"Nombre de documents dans 'Users' : {len(users)}")
        except Exception as e:
            print(f"Erreur lors du test de la base de données : {e}")

if __name__ == "__main__":
    test_database()