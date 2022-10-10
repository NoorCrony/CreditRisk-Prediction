from datetime import datetime


class Logger:

    """
    Purpose: Custom logging class
    Version: 1
    Date of modification: 10/10/2022
    Input:  * log message
            * file object
    Output: add a row to file object with all details related to logging

    """

    def __init__(self):
        pass

    def log_method(self, file_object, log_message):
        """
        :param file_object: log file path
        :param log_message: custom log message
        :return: add new row to log file

        """

        # self.file_object = file_object
        # self.log_message = log_message
        self.datetime = datetime.now()
        self.date = self.datetime.date()
        self.current_time = self.datetime.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message + "\n")



