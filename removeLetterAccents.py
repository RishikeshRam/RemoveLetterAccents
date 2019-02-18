"""Program helps to change accented letters to corresponding letters without accent marks"""
import unicodedata

#Getting the text to be converted by removing the accents
text = input("Enter the text to remove the letter accents: ")

"""Using the Unicode Characters of Category Nonspacing Mark the text
removes the accents and convert it to corresponding letters"""
convertedText = ''.join((word for word in unicodedata.normalize('NFD', text) if unicodedata.category(word) != 'Mn'))

#The converted text is printed
print("Text after convertion: "+convertedText)
