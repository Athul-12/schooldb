import logging
logging.basicConfig(filename="log_msg.log", format='%(asctime)s  %(message)s', filemode='w')
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

a = 10
b = 0
try:
    c = a/b
except Exception as e:
    logging.error("exeption occured",exc_info = True)

# logging.debug('the debug messege is displaying')
# logging.info('the info messege is displaying')
# logging.warning('the warning messege is displaying')
# logging.error('the error messege is displaying')
# logging.critical('the critical messege is displaying')
