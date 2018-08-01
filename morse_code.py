import string

class Solution(object):
    
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        mapping = {}
        encountered_morse_code = []
        ascii_lowercase = list(string.ascii_lowercase)
        morse_code_list = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",
            ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."
        ]
        
        zipped = zip(ascii_lowercase,morse_code_list)
        for item in zipped:
            mapping[item[0]] = item[1]
            
        morse_code = ""
        for word in words:
            for letter in word:
                if letter in mapping:
                    morse_code = morse_code + mapping[letter]
                
            if morse_code not in encountered_morse_code:
                encountered_morse_code.append(morse_code)
            morse_code = ""
        return len(encountered_morse_code)


if __name__ == "__main__":
    words = ["gin", "zen", "gig", "msg"]
    s = Solution()
    print (s.uniqueMorseRepresentations(words))