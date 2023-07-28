import logging
from datetime import datetime

logging.basicConfig(filename='name_log.log', filemode='a', encoding='utf=8', level=logging.INFO)


def log_all():
    logging.info(f'Добавлен экземпляр класса DIR_LIST {datetime.now()}')
