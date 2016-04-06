import unittest
from ccn_safety import mask_credit_card_numbers

class TestCCNSafety(unittest.TestCase):
    def test_ccn_masking_embedded(self):
        """
        Tests masking of true test credit numbers embedded in text, specifically
        Visa and American Express, with dashes and or spaces in them.
        Test that numbers that do not pass all the test are unchanged.
        """
        text = """
        Have you ever noticed, in television and movies, that phone numbers and credit cards
        are obviously fake numbers like 555-123-4567 or 4012 8888 8888 1881? It is because a number
        that appears to be real, such as 3782-8224631-0005, triggers the attention of privacy and 
        security experts.
        """
        expected =  """
        Have you ever noticed, in television and movies, that phone numbers and credit cards
        are obviously fake numbers like 555-123-4567 or XXXX XXXX XXXX 1881? It is because a number
        that appears to be real, such as XXXX-XXXXXXX-0005, triggers the attention of privacy and 
        security experts.
        """
        observed = mask_credit_card_numbers(text)
        self.assertEqual(expected, observed)
    
    def test_ccn_masking_at_start(self):
        """
        Tests masking of true test credit numbers at start of text, specifically
        Discover
        """
        text = """
        6011000990139424 is a good number to start with.
        """
        expected = """
        XXXXXXXXXXXX9424 is a good number to start with.
        """
        observed = mask_credit_card_numbers(text)
        self.assertEqual(expected, observed)
        
    
    def test_ccn_masking_at_end(self):
        """
        Tests masking of true test credit numbers at end of text, specifically
        Diners
        """
        text = """
        A good number to end with is 30569309025904
        """
        expected = """
        A good number to end with is XXXXXXXXXX5904
        """
        observed = mask_credit_card_numbers(text)
        self.assertEqual(expected, observed)
        
    def test_ccn_masking_number_only(self):
        """
        Tests masking of true test credit numbers  as only entry, specifically
        JCB and MasterCard 
        """
        text = """
        3530111333300000 5105105105105100
        """
        expected = """
        XXXXXXXXXXXX0000 XXXXXXXXXXXX5100
        """
        observed = mask_credit_card_numbers(text)
        self.assertEqual(expected, observed)
        
    def test_ccn_no_masking_fails_luhn(self):
        """
        Tests no masking of numbers that pass all the checks except luhn checksum
        Diners one (last) digit out (proper number masked in test above)
        """
        text = """
        30569309025905
        """
        expected = """
        30569309025905
        """
        observed = mask_credit_card_numbers(text)
        self.assertEqual(expected, observed)
        
    def test_ccn_no_masking_not_in_list(self):
        """
        Tests no masking of numbers that pass all the checks except except
        they are processor specific and are not o the list, specifically
        Dankort (PBS)s
        """
        text = """
        5019717010103742
        """
        expected = """
        5019717010103742
        """
        observed = mask_credit_card_numbers(text)
        self.assertEqual(expected, observed)
        
if __name__ == "__main__":
    unittest.main()