class Solution:
    def romanToInt(self, s: str) -> int:
        # Create the dictionary
        roman_map = {
            # 1. Letter Lookups
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
    
            # 2. Index Lookups (0 to 6)
            0: ("I", 1),
            1: ("V", 5),
            2: ("X", 10),
            3: ("L", 50),
            4: ("C", 100),
            5: ("D", 500),
            6: ("M", 1000)
        }

        #Create List of letters
        roman_list = list(s)
        #roman_list.reverse()
        #Check word length
        length = len(roman_list)

        ##########

        def roman_calc(word, long):

            down = 1
            num = 0
            prev = 0
            size = long 

            while size != 0:
                if prev <= (roman_map[word[size - 1]]):
                    num += (roman_map[word[size - 1]])
                    prev = (roman_map[word[size - 1]])
                    size -= 1
                else: #prev > (roman_map[word[size - 1]]):
                    num -= (roman_map[word[size - 1]])
                    prev = (roman_map[word[size - 1]])
                    size -= 1
            else:
                return num

        ##########

        return roman_calc(roman_list, length)