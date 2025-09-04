import os
import os, ctypes
# Point PyEnchant to the Homebrew lib explicitly (Apple Silicon path shown):
os.environ["PYENCHANT_LIBRARY_PATH"] = "/opt/homebrew/opt/enchant/lib/libenchant-2.2.dylib"
os.environ["PYENCHANT_VERBOSE_FIND"] = "1"
ctypes.CDLL("/opt/homebrew/opt/enchant/lib/libenchant-2.2.dylib")
import enchant

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path =os.path.join(dir_path,'sowpods.txt')


class AnagramChecker:
    """Checker for different anagrams. Checks if it's in English"""
    def __init__(self,file_path:str):
        with open(file_path, "r", encoding="utf-8") as f:
            self.words = [line.strip() for line in f if line.strip()]
        self._english_dictionary = enchant.Dict("en_US")

    def is_valid_word(self,word) -> bool:
        return self._english_dictionary.check(word)
    
    def get_anagrams(self, word):
        anagrams = []
        for candidate in self.words:
            if self.is_anagram(word1=word, word2=candidate):
                anagrams.append(candidate)
        return anagrams
    
    def is_anagram(self, word1 : str, word2 : str) -> bool:
        if len(word1) != len(word2):
            return False
        word1_list = list(word1.lower())
        word1_list.sort()
        word2_list = list(word2.lower())
        word2_list.sort()
        return word1_list == word2_list and word1 != word2

if __name__ == "__main__":
    checker = AnagramChecker(file_path)
    print(checker.is_valid_word("meat"))
    print(checker.get_anagrams('meat'))
    print()