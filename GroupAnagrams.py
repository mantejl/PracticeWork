from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # main trick with groupAnagrams here is map the character counts/sorted words to actual words
        # not the other way around

        anagram_groups = {}

        # getting each word and sorting it using sorted() method, which returns a list of strings
        for word in strs:
            new_str = "".join(sorted(word))
            # after joining, adding it to our map along with the word we are currently checking
            if new_str in anagram_groups:
                anagram_groups[new_str].append(word)
            else:
                anagram_groups[new_str] = [word]

        return anagram_groups.values()

        anagram_groups = {}

        # using the count of each character as a key vs the words
        for word in strs:
            count = [0] * 26

            # getting the count of each character and mapping using ascii values with ord() function
            for c in word:
                count[ord(c) - ord("a")] += 1

            # creating tuple of count bc lists cannot be keys in python
            key = tuple(count)

            # adding the word to the list key
            if key not in anagram_groups.keys():
                anagram_groups[key] = [word]
            else:
                anagram_groups[key].append(word)

        # outputting the words grouped by character count
        return anagram_groups.values()



