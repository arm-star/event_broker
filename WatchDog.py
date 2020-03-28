from Observer import Observer
from Consumer import Consumer
from definitions import *

if __name__ == "__main__":
    obs = Observer(PATH_TO_WATCH)
    s1 = Consumer('Arman')
    s1.configure(FILES_LIST)
    s2 = Consumer('Eduard')
    s2.configure(FILES_LIST)
    obs.add_consumer(s1)
    obs.add_consumer(s2)
    obs.run()