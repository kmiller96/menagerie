import resend

with open("API_KEY") as f:
    resend.api_key = f.read().strip()

r = resend.Emails.send(
    {
        "from": "onboarding@resend.dev",
        "to": "kale.miller@prometheusai.com.au",
        "subject": "Hello World",
        "html": "<p>Congrats on sending your <strong>first email</strong>!</p>",
    }
)
