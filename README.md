## easyemail

This makes it easy to loop through a CSV file and send template emails to many people. We use it to quickly send the same public records request to more than 40 school boards in New Orleans.

__Usage__

```
Usage: easyemail [options]

Options:
  -h, --help    Show this help message and exit.
  -l, --live    Send emails to their actual recipients.
  -d, --dry-run Test output by sending one email to test email address (default: tthoren@thelensnola.org).
```

__Setup__

```bash
git clone https://github.com/TheLens/easy-email.git
cd easy-email
chmod +x easyemail
```

Make sure `easyemail` is in your `PATH`. If currently in same directory:

```bash
export PATH=$(pwd):$PATH
```

You will need to temporarily turn off two-step verification, if you have it set up. You might also need to [allow your Gmail account to be accessed by insecure apps](Insecure Gmail). Make sure you change these back after you are finished.

__Steps__

1. Download CSV from Google Sheets and name `recipients.csv`. Make sure to use columns "name" and "email."
2. Update the request template with any new language. Make sure CSV headers match the variables in the template.
3. Update email subject, from and CC variables in `easyemail`.
4. Update environment variables `EASYEMAIL_GMAIL_USERNAME` and `EASYEMAIL_GMAIL_PASSWORD` for the account that will be sending the emails.
5. Run `easyemail --dry-run` to test that everything looks okay.
6. If everything looks good, run `easyemail --live` to send the emails for real.

__Known limitations__

- Currently only supports a single recipient per email.
- Only uses Gmail.

[Insecure Gmail]: https://www.google.com/settings/security/lesssecureapps