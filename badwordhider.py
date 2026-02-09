sentence = input("Enter the sentence : ")
word = input("Enter the bad word to replace : ")
repword = sentence.replace(word,"*"*len(word))
print(repword)