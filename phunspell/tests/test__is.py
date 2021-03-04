import phunspell
import inspect
import unittest


class TestIS(unittest.TestCase):
    pspell = phunspell.Phunspell('is')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("vonbiðilsins"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = (
            "freðfiski vonbiðilsins ráðherraráðs jafnsnart skólafélagi borken"
        )
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
