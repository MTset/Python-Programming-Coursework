"""
cnn_safety.py: Masks valid credit card card numbers in text with:
CCN REMOVED FOR YOUR SAFETY, leaves other numbers unchanged.
Input: text
Output: text with credit card number masking.  Masking string: CCN REMOVED FOR YOUR SAFETY.
Credit card checking: (digits only) credit card number length, valid credit
card number ranges, Luhn algorithm.
"""
import re

def mask_credit_card_numbers(text):
    potential_ccn = re.compile(r"""
        (?:\d[ -]*?) # a string of digits or groups of digits intersperse with space or -
        {13,16}      # total number of digits to be 13-16
        """, re.VERBOSE)
    numbers_to_check = re.finditer(potential_ccn, text)
    for match in numbers_to_check:
        text = text.replace(match.group(), is_credit_card_valid(match.group()))
    return text
    
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]

    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_credit_card_valid(card_number):
    credit_cards = [
                    ("Diners Club", range(3000, 3060)),
                    ("Diners Club", range(3600, 3700)),
                    ("Diners Club", range(3800, 3890)),
                    ("American Express", range(3400, 3500)),
                    ("American Express", range(3700, 3800)),
                    ("JCB", range(3528, 3590)),
                    ("Carte Blanche", range(3890, 3900)),
                    ("Visa", range(4000, 5000)),
                    ("MasterCard", range(5100, 5600)),
                    ("BankCard", range(5610, 5611)),
                    ("Discover", range(6011, 6012)),
                    ]

    #digits only required to check against card prefix ranges and luhn checksum
    not_digits = re.compile(r"[\D]+ # everything not a digit", re.VERBOSE)
    stripped_card_number = (re.sub(not_digits, "", str(card_number)))
    for item in credit_cards:
        if int(stripped_card_number[:4]) in item[1]:
            if luhn_checksum(int(stripped_card_number)) == 0:
                # passed all checks, so restore any punctuation that followed
                last_char = ""
                match = re.match(r"\D", card_number[-1])
                if match:
                    last_char = match.group()
                # no efficiency ains to be made in compiling card_number
                return(re.sub(card_number, "CCN REMOVED FOR YOUR SAFETY"+
                              last_char, card_number))
    return card_number

if __name__ == "__main__":
    text = """
    Have you ever noticed, in television and movies, that phone numbers and credit cards
    are obviously fake numbers like 555-123-4567 or 4012 8888 8888 1881? It is because a number
    that appears to be real, such as 3782-8224631-0005, triggers the attention of privacy and 
    security experts.
    """
    
    text = mask_credit_card_numbers(text)
#    text = luhn_checksum(5019717010103742)
    print(text)