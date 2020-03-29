import time
from definitions import *

hDir = HDIR


class Observer(object):
    """"
    Class dedicated to initialize obs object
    :param path_to_watch
    """
    def __init__(self, path_to_watch):
        self.path_to_watch = path_to_watch
        self.backup_path = PATH_TO_BACKUP
        self.consumers = []

    def add_consumer(self, consumer):
        """
        add new consumer
        :param consumer:
        :return:
        """
        self.consumers.append(consumer)

    def remove_consumer(self, consumer):
        """
        this function can be used to remove the consumer
        :param consumer:
        :return:
        """
        self.consumers = [i for i in self.consumers if i != consumer]

    def backup(self):
        """
        backup the files to watch
        :return:
        """
        os.makedirs(self.backup_path, exist_ok=True)
        files = []
        for c in self.consumers:
            for f in c.files:
                if f not in files:
                    copyfile(os.path.join(self.path_to_watch, f),
                             os.path.join(self.backup_path, f))
                    files.append(f)

    def run(self):
        """
        run the core
        :return:
        """
        self.backup()
        while True:
            #
            # ReadDirectoryChangesW takes a previously-created
            # handle to a directory, a buffer size for results,
            # a flag to indicate whether to watch subtrees and
            # a filter of what changes to notify.
            #
            # NB Tim Juchcinski reports that he needed to up
            # the buffer size to be sure of picking up all
            # events when a large number of files were
            # deleted at once.
            #
            results = win32file.ReadDirectoryChangesW(
                hDir, 1024, True, win32con.FILE_NOTIFY_CHANGE_FILE_NAME
                | win32con.FILE_NOTIFY_CHANGE_DIR_NAME
                | win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES
                | win32con.FILE_NOTIFY_CHANGE_SIZE
                | win32con.FILE_NOTIFY_CHANGE_LAST_WRITE
                | win32con.FILE_NOTIFY_CHANGE_SECURITY, None, None)
            if results:
                self.on_modified(results)
                self.backup()

    def on_modified(self, results):
        """
        checks if modified and gets difference
        :param results:
        :return: message of modification time and difference list
        """
        for action, file in results:
            consumers = [c for c in self.consumers if file in c.files]
            if consumers:
                full_filename = os.path.join(self.path_to_watch, file)
                backup_filename = os.path.join(self.backup_path, file)
                if ACTIONS.get(action, "Unknown") == "Updated":
                    with open(backup_filename, 'r') as f:
                        text_before = f.readlines()
                    with open(full_filename, 'r') as f:
                        text_after = f.readlines()
                    message = []
                    message.append("Modification time: {}".format(time.ctime(os.stat(full_filename).st_mtime)))
                    for line in difflib.unified_diff(text_before,
                                                     text_after):
                        message.append(line)
                    if len(message) != 1:
                        for c in consumers:
                            c.log(message)
