#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import date
import os
def generate_report(filename, title, paragraph):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(paragraph, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])

if __name__ == '__main__':
  filename = '/tmp/processed.pdf'
  title = 'Processed Update on ' + date.today().strftime('%B %Y')
  paragraph = ''
  for file in os.listdir('supplier-data/descriptions'):
    with open('supplier-data/descriptions/'+file) as desc:
      lines = desc.readlines()

      for i in range(2):
        if i == 0:

          lin = lines[i].strip()
          paragraph += 'name: ' + lin + '<br/>'
        else:
          lin = lines[i].strip()
          lin = lines[i].split('.')[0]
          paragraph += 'weight: ' + lin + '<br/>'
      paragraph += '<br/>'
  generate_report(filename,title,paragraph)
