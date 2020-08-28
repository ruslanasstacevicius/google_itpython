#!/usr/bin/env python3

import os
import emails
import datetime
from run import get_fruit_data
from reports import generate_report

fruits = get_fruit_data()

pdf_content = ''

for fruit in fruits:
    print(fruit)
    pdf_content += 'name: ' + fruit['name'] + '<br />' \
            + 'weight: ' + fruit['weight'] + ' lbs' + '<br />' + '<br />'


current_date = datetime.date.today().strftime('%B %d, %Y')
title = 'Processed update on ' + str(current_date)
generate_report('/tmp/processed.pdf', title, pdf_content)

email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

user = os.getenv('USER')
email = emails.generate('automation@example.com', user + '@example.com', 'Upload Completed - Online Fruit Store', email_body, '/tmp/processed.pdf')
emails.send(email)

