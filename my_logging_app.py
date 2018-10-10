import logging
import logstash
import sys
import time
import random
#import logging.handlers

#from logstashHandler import logstashHandler

# Setup logger
test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(logstash.LogstashHandler('52.15.38.138', 5959, version=1))


test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')

for i in range(100):
    # add extra field to logstash message
    extra = {
        'test_string': 'python version: ' + repr(sys.version_info),
        'test_boolean': random.choice([True, False]),
        'test_dict': {'a': 1, 'b': 'c'},
        'test_float': 1.23,
        'test_integer': random.randint(10, 150),
        'test_list': [1, 2, '3'],
        
    }
    test_logger.info('python-logstash: test extra fields', extra=extra)



person_firstname = ['Suka','Shami','Gilbal']
person_lastname = ['Sinah','Gimn', 'Trump']


for i in range(100):
    firstname = random.choice(person_firstname)
    lastname = random.choice(person_lastname)
    
   
    add_extra_data={
    'First Name':firstname,
    'Last Name': lastname,
    'Address':'8811 215 st Quueens New York 11427',
    'Contact Number':'915.456.8900',
    'Vist Number': i,
    }

    # I have added extra fake data for test in Kibana.
    # Call the info method on the test_logger object and give it two parameters.
    test_logger.info('python-logstash: fake test data', extra=add_extra_data)
