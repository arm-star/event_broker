

class Consumer(object):
    """
    Class is dedicated to create consumers
    :param user name, list of file names
    """
    def __init__(self, name, files=None):
        self.name = name
        self.files = files

    def configure(self, files):
        """
        configure to set the consumer
        :param files:
        :return:
        """
        self.files = files

    def remove_files(self):
        """
        use to remove files
        :return:
        """
        self.files = []

    def log(self, messages):
        """
        :param messages:
        """
        print('consumer name: {}'.format(self.name))
        [print(m) for m in messages]

    def __eq__(self, other):
        """
        check if consumer exists by comparing consumer name and list of files
        :param other:
        :return:
        """
        return (self.name == other.name) & (set(self.files) == set(
            other.files))
