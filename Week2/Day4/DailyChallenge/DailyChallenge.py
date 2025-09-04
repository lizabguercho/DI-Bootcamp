import os
import string
import re
class Text:
    def __init__(self,text):
        self.text = text

    def word_frequency(self,word):
        words = self.text.split()
        word = word.lower()
        word_count = 0
        for w in words:
            if w == word:
                word_count += 1
            elif word_count == 0:
                print("This word is not found in the text.")
        return word_count

    def most_common_word(self):
        word_list = self.text.lower().split()
        word_frequencies = {}
        for word in word_list:
            word_frequencies[word] = word_frequencies.get(word,0) + 1
        return word_frequencies
    
    def unique_words(self):
        word_list2 = self.text.split()
        unique = set(word_list2)
        return list(unique)
    
    @classmethod
    def from_file(cls,file_path):
        dir_path = os.path.dirname(os.path.realpath(__file__)) 
        file_path = os.path.join(dir_path,"my_text.txt")
        with open(file_path,"r", encoding = "utf-8") as f:
            file_content = f.read()
            print("Text was read")
        return cls(file_content)
    
class TextModification(Text):
    def __init__(self,text):
        super().__init__(text)

    def remove_punctuation(self):
        punctuation = string.punctuation
        cleaned_text = ''.join(chr for chr in self.text if chr not in punctuation)
        return cleaned_text

    def load_stop_words(file_path):
        dir_path = os.path.dirname(os.path.realpath(__file__)) 
        file_path = os.path.join(dir_path,"stop_words.txt")
        with open(file_path,"r", encoding = "utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
            return set(words)
        
    def remove_stop_words(self,stop_words):
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return "".join(filtered_words)

    def remove_special_characters(self):
        #replace special characters with space
        cleaned_text = re.sub(r"[^A-Za-z0-9\s]+", " ", self.text)  
        cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()        
        return cleaned_text

text1 = Text.from_file("my_text.txt")
print(text1.text) 

# Create modifier

tm = TextModification(text1.text)
print(tm.remove_punctuation())

# Load stop words, then remove them
stop_words = TextModification.load_stop_words("stop_words.txt")
print(tm.remove_stop_words(stop_words))

print(tm.remove_special_characters())


