import os

class LoadConfig():
    """
     Representation of an instance when loading the config file
    """
    def load(self):
        """
        Loads config data from config.txt
        :return: dict containing key:configuration option value:configuration value
        """
        config_dict = {}
        with open(os.path.join(os.getcwd(), "gel2mdt/config/config.txt"), 'r') as config_file:
            for line in config_file:
                line = line.strip().split('=', 1)
                config_dict[line[0]] = line[1]
        return config_dict