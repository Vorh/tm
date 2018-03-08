import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from src import app

if __name__ == "__main__":
    # initialize the log handler
    logHandler = logging.StreamHandler()

    # set the log handler level
    logHandler.setLevel(logging.INFO)

    logHandler.setFormatter(Formatter('''%(asctime)s %(levelname)s %(module)s - %(message)s'''))

    # set the app logger level
    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)
    app.run()
