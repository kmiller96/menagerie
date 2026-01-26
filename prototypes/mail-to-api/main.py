import time
import os
import imaplib
import logging
from email import policy
from email.parser import BytesParser
from email.utils import getaddresses

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


def check_and_process_unseen_emails():
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
        else:
            logging.info(f"Found {len(email_ids)} new emails.")

        for email_id in email_ids:
            details = process_email(mail, email_id)
            logging.debug(f"Email details: {details}")

    logging.debug("Done checking emails.")


def process_email(mail, email_id):
    """Placeholder for email processing."""
    status, data = mail.fetch(email_id, "(RFC822)")

    if status != "OK" or not data or not data[0]:
        logging.warning(f"Failed to fetch email {email_id}.")
        return

    logging.debug("Processing email.")
    raw_email = data[0][1]
    details = extract_email_details(raw_email)

    logging.info(f"Processed email {email_id}.")
    mail.store(email_id, "+FLAGS", "\\Seen")
    logging.debug(f"Marked email {email_id} as seen.")

    return details


def extract_email_details(raw_email):
    """Extracts details from a raw email byte string.

    NOTE: This is an AI-generated function. I am not really sure how it works.
    Worth reviewing at some point to see if I can make it cleaner.
    """
    msg = BytesParser(policy=policy.default).parsebytes(raw_email)

    from_addrs = getaddresses(msg.get_all("From", []))
    sender_addr = ""
    if from_addrs:
        sender_addr = from_addrs[0][1] or from_addrs[0][0]

    cc = [addr for _, addr in getaddresses(msg.get_all("Cc", [])) if addr]
    subject = msg.get("Subject", "")

    body_bytes = b""
    attachments = []

    if msg.is_multipart():
        text_part = None
        html_part = None
        for part in msg.walk():
            if part.is_multipart():
                continue
            disposition = part.get_content_disposition()
            if disposition == "attachment":
                payload = part.get_payload(decode=True)
                if payload is not None:
                    attachments.append(payload)
                continue
            content_type = part.get_content_type()
            if content_type == "text/plain" and text_part is None:
                text_part = part
            elif content_type == "text/html" and html_part is None:
                html_part = part
        chosen = text_part or html_part
        if chosen:
            body_bytes = chosen.get_payload(decode=True) or b""
    else:
        body_bytes = msg.get_payload(decode=True) or b""

    return {
        "sender": sender_addr,
        "cc": cc,
        "subject": subject,
        "body": body_bytes,
        "attachments": attachments,
    }


## ---------------------- ##
## -- Define Scheduler -- ##
## ---------------------- ##

if __name__ == "__main__":
    logging.info("Starting email processor.")

    while True:
        logging.debug("Starting new email check cycle.")

        check_and_process_unseen_emails()

        logging.debug("Loop complete, waiting for next cycle.")
        time.sleep(5)  # HACK: Wait at least 5 second between checking for new emails.
