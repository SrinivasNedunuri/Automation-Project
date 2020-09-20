#!/usr/bin/env python3
# automatic email attached with the pdf expalaining the supplier about import data
import emails

if __name__ == "__main__":
  sender = 'automation@example.com'
  recipient = 'student-00-ceea497b272a@example.com'
  subject = 'Upload Completed - Online Fruit Store'
  body =  'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

  attachment_path = '/tmp/processed.pdf'
  message = emails.generate(sender, recipient, subject, body, attachment_path)
  emails.send(message)

