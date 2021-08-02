from time import sleep
from endpoint_listener import Listener
from watcher import EndpointWatcher
from db_store import SqliteDataStore

def main():
    data_storage = SqliteDataStore()
    #data_storage.createTableIfNotExists()
    s = Listener(url="https://viacep.com.br/ws/01001000/json/")
    #s = Listener(url="https://pokeapi.co/api/v2/pokemon/ditto")
    watcher = EndpointWatcher(s)

    for _ in range(1,10):
        response = watcher.watch()
        if response.status_code not in (200,201):
            print("Alert!")

        data_storage.storeData(tuple(response.values()))

        sleep(5)


    for col in data_storage.con.execute("select * from analytics"):
        print(col)

    data_storage.con.close()

if __name__ == '__main__':
    main()