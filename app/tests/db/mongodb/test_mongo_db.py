from unittest.mock import MagicMock, patch
from db.mongodb.get_db import get_db_mongo
import mongomock

def test_get_db_mongo():

    with patch("db.mongodb.get_db.MongoClient") as mock_mongo_client:

        mock_users_collection = MagicMock()

        mock_mongo_client.return_value.__getitem__.return_value.__getitem__.return_value = mock_users_collection

        connect = get_db_mongo()

        assert connect == mock_users_collection

        mock_mongo_client.assert_called_once()
        mock_mongo_client.return_value.__getitem__.assert_called_once_with("practice")
        mock_mongo_client.return_value.__getitem__.return_value.__getitem__.assert_called_once_with("users")




""" 
Estamos simulando la siguiente cadena de llamadas:

MongoClient(): Simulado por mock_mongo_client.return_value

client["practice"]: Simulado por mock_mongo_client.return_value.__getitem__.return_value

db["users"]: Simulado por mock_mongo_client.return_value.__getitem__.return_value.__getitem__.return_value, que finalmente devuelve mock_users_collection.

"""