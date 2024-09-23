class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        bigString = ""
        for i in strs:
            lenght = str(len(i))
            bigString = bigString + lenght + "@" + i
        return bigString
    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
            listOfStrings = []
        numLetters = ""
        index = 0
        while index < len(str):
            if str[index] == "@":
                length = int(numLetters)
                word = str[index+1 : index+1+length]
                listOfStrings.append(word)
                numLetters = ""
                index = index+1+length
            else:
                numLetters = numLetters + str[index]
                index += 1

        return listOfStrings



## carefull for when numbers are double or more digits long
