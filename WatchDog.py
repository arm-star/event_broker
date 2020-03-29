from Observer import Observer
from Consumer import Consumer
from definitions import *

if __name__ == "__main__":
    obs = Observer(PATH_TO_WATCH)
    s1 = Consumer('User_1')
    s1.configure(FILES_LIST_USER_1)
    s2 = Consumer('User_2')
    s2.configure(FILES_LIST_USER_2)
    obs.add_consumer(s1)
    obs.add_consumer(s2)
    obs.run()