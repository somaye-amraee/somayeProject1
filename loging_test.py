import logging
logging.basicConfig(level=logging.DEBUG,
                   filename='actual_test.log',
                   filemod='a',
                   format='%(Levelname)s -%(asctime)s - %(message)s',
                   datefmt='%d-%b-%y %H:%M:%S')

logging.debug('this is a debug message')
logging.info('this is an info message')
logging.warning('this is a warning message')
logging.error('this is a debug message')
logging.critical('this is a critical message')


my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.INFO)
event_handler = logging.FileHandler('Event.log')
ticket_handler = logging.FileHandler('Ticket.log')
error_handler.setLevel(logging.WARNING)
log_format = logging.Formatter('%(Levelname)s -%(asctime)s - %(message)s',
                               datefmt='%d-%b-%y %H:%M:%S')
event_handler.setFormatter(log_format)
ticket_handler.setFormatter(log_format)
error_handler.setFormatter(log_format)
my_logger.addHandler(ticket_handler)
my_logger.addHandler(error_handler)


