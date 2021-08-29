from time import sleep
from src.endpoint_listener import Listener
from src.watcher import EndpointWatcher
from src.db_store import SqliteDataStore
import logging

logging.basicConfig(filename="log.log")

def main():
    data_storage = SqliteDataStore()
    #data_storage.createTableIfNotExists()
    endpoint_list = [
        Listener(url="https://viacep.com.br/ws/01001000/json/"),
        Listener(url="https://pokeapi.co/api/v2/pokemon/ditto")
    ]
    watch_list = [EndpointWatcher(endpoint) for endpoint in endpoint_list]        

    for _ in range(1,10):
        for watcher in watch_list:
            response = watcher.watch()
            if response['status_code'] not in (200,201):
                print("Alert!")
            data_storage.storeData(tuple(response.values()))
        sleep(5)


    for col in data_storage.con.execute("select * from analytics"):
        print(col)

    data_storage.con.close()

if __name__ == '__main__':
    main()