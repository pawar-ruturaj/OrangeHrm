import inspect
import logging


class logGenerate:

    @staticmethod
    def log_gen():
        name = inspect.stack()[1][3]   # in log report replace roo with class name
        logger = logging.getLogger()
        file = logging.FileHandler("D:\\Ruturaj\\OrangeHRM\\Logs\\OrangeHRM.log")  # give a path of Logs folder.
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        # search logging format on Google, on python web side it will show format.
        file.setFormatter(format)
        logger.addHandler(file)
        logger.setLevel(logging.INFO)
        return  logger

# get log --> logging.getLogger()
# log file --> path and name
# format --> define logs format
# setformatter --> link file and format
# add handler --> maintain log file

# create this log file is one time activity, you can use this log in multiple projects
# when we create html reports that log also shown in that html reports
