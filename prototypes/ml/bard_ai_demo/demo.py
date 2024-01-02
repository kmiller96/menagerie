from bardapi import BardCookies

cookie_dict = {
    "__Secure-1PSID": "xxx",
    "__Secure-1PSIDTS": "xxx",
    "__Secure-1PSIDCC": "xxx",
}

bard = BardCookies(cookie_dict=cookie_dict)
print(bard.get_answer("What is the answer to the universe?")["content"])
