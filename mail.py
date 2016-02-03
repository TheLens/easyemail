
"""Methods for sending emails."""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail(object):
    """Methods for sending emails via Gmail."""

    def __init__(self, subject="", frm='', to=[''], cc=None, body="",):
        """Initialize class variables."""
        self.subject = subject
        self.body = body
        self.frm = frm
        self.to = to
        self.cc = cc

        self.host = 'smtp.gmail.com'
        self.port = 587

    def send_email(self, msg):
        """Send email."""
        s = smtplib.SMTP(self.host, self.port)

        s.ehlo()
        s.starttls()
        s.ehlo()

        s.login(os.getenv('EASYEMAIL_GMAIL_USERNAME'),
                os.getenv('EASYEMAIL_GMAIL_PASSWORD'))

        s.sendmail(self.frm, self.to, msg.as_string())

        s.quit()

    def add_headers(self, msg):
        """Add headers."""
        msg['Subject'] = self.subject
        msg['From'] = self.frm
        msg['To'] = ','.join(self.to)

        if self.cc:
            msg['cc'] = self.cc

        return msg

    def send_as_html(self):
        """Form message."""
        msg = MIMEMultipart('alternative')
        msg = self.add_headers(msg)
        html = (
            '<!DOCTYPE html>' +
            '<html>' +
            '<head><meta charset="utf-8"></head>' +
            '<body>' +
            self.body +
            '</body>' +
            '</html>')

        msg_text = MIMEText(html, 'plain')
        msg_html = MIMEText(html, 'html')

        msg.attach(msg_text)
        msg.attach(msg_html)

        self.send_email(msg)
