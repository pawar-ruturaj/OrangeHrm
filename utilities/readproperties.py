import configparser


configuration = configparser.RawConfigParser()
configuration.read("D:\\Ruturaj\\OrangeHRM\\Configurations\\config.ini")
# RawConfigParser is used to read files from config.ini file.


class Readconfig:

    @staticmethod  # when we use this decorator self in method need not use, we can use method when we call class.
    def geturl():
        url = configuration.get("common info","Url")
        return url

    @staticmethod  # when we use this decorator self in method need not use, we can use method when we call class.
    def getusername():
        Username = configuration.get("common info", "Username")
        return Username

    @staticmethod  # when we use this decorator self in method need not use, we can use method when we call class.
    def getpassword():
        password = configuration.get("common info", "Password")
        return password
