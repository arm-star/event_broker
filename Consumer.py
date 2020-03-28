

class Consumer(object):
    """

    """
    def __init__(self, name, files=None):
        self.name = name
        self.files = files

    def configure(self, files):
        """

        :param files:
        :return:
        """
        self.files = files

    def remove_files(self):
        """

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

        :param other:
        :return:
        """
        return (self.name == other.name) & (set(self.files) == set(
            other.files))
