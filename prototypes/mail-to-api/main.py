import time
import os
import imaplib
import logging

import dotenv

# TODO: Throttle the processing to avoid hitting email provider limits.

## ------------- ##
## -- Globals -- ##
## ------------- ##

dotenv.load_dotenv()
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s:%(lineno)d | %(message)s",
)

sender = os.getenv("EMAIL_USER", "")
password = os.getenv("EMAIL_PASS", "")

if sender == "":
    raise ValueError("EMAIL_USER environment variable not set")
if password == "":
    raise ValueError("EMAIL_PASS environment variable not set")

## -------------------- ##
## -- Define Handler -- ##
## -------------------- ##


def process_emails():
    """Checks for new emails and processes them."""
    logging.debug("Processing emails.")

    with imaplib.IMAP4_SSL("imap.gmail.com") as mail:
        mail.login(sender, password)
        mail.select("inbox")

        status, messages = mail.search(None, "UNSEEN")
        email_ids = messages[0].split()

        if len(email_ids) == 0:
            logging.debug("No new emails found.")
            return

        logging.info(f"Found {len(email_ids)} new emails.")
        # TODO: Add email processing logic here.

    logging.debug("Done checking emails.")


## ---------------------- ##
## -- Define Scheduler -- ##
## ---------------------- ##

if __name__ == "__main__":
    logging.info("Starting email processor.")

    while True:
        logging.debug("Starting new email check cycle.")

        process_emails()

        logging.debug("Loop complete, waiting for next cycle.")
        time.sleep(5)  # HACK: Wait at least 5 second between checking for new emails.
