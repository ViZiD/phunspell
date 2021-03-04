import phunspell
import inspect
import unittest


class TestSwTZ(unittest.TestCase):
    pspell = phunspell.Phunspell('sw_TZ')

    def test_word_found(self):
        self.assertTrue(self.pspell.lookup("niliwahimiza"))

    def test_word_not_found(self):
        self.assertFalse(self.pspell.lookup("phunspell"))

    def test_lookup_list_return_not_found(self):
        words = "chasasa niliwahimiza chunusha ahera mwanandoa borken"
        self.assertListEqual(
            self.pspell.lookup_list(words.split(" ")), ["borken"]
        )


if __name__ == "__main__":
    unittest.main()
