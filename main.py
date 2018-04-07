import logging
from logging.handlers import RotatingFileHandler
from logging import Formatter
from tm import app

if __name__ == "__main__":
    logHandler = logging.StreamHandler()

    logHandler.setLevel(logging.INFO)

    logHandler.setFormatter(Formatter('''%(asctime)s %(levelname)s %(module)s - %(message)s'''))

    app.logger.setLevel(logging.INFO)

    app.logger.addHandler(logHandler)
    app.run()
