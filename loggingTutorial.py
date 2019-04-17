import logging

'''
There are 5 levels indicating the severity of evenets
1. debug
2. info
3. warning
4. error
5. critical
'''
# Change logging level and send the logs to a specific file rather than the console.
logging.basicConfig(level=logging.INFO, filename="micado.log", filemode='w', format='%(asctime)s - %(process)d - %(levelname)s - %(message)s')

# Various logging levels
logging.debug(' Debugging message ... ')
logging.info(' Info message ...')
logging.warning(' Warning message ... ')
logging.error(' Error message ...')
logging.critical(' Critical message ... ')
