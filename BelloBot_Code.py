### ********************** IMPORTS, FUNCTIONS, VARIABLES, ETC. **********************###
# import of modules and libraries
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
import re
import random
import pandas as pd
df = pd.read_excel("QA.xlsx", "Tabelle1")

#regex stemmer
def stem(word):
    regexp = r"^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ion)?$"
    stem, suffix = re.findall(regexp, word)[0]
    return stem
    
# preprocessing
def preprocessing(userString):
    userString = userString.lower()
    userString = word_tokenize(userString)
    sw = stopwords.words("english")
    userString = [w for w in userString if w not in sw]
    userString = [stem(t) for t in userString]
    return userString

gimmick = ["Meow!", "Whoof, whoof!", "Please enter your question, whoof!", "Hi there!"]


###********************************** MAIN PROGRAM **********************************###
# Bello Bot's introduction
BB_introduction = "Hello, my name is Bello Bot and I am here to inform you about our pound. You can ask questions about our pound, our current animal population, animal adoption, animal sponsorship, donation and contact options. Please enter your question below."
print(BB_introduction)

while True:
    userString = input("Your input: ")
    userString = preprocessing(userString)
    
# contact options
    if "contact" in userString or "approach" in userString:
        print(df["Answers"][0])
    elif "phone" in userString or "telephone" in userString or "call" in userString:
        print(df["Answers"][1])
    elif "email" in userString or "mail" in userString:
        print(df["Answers"][2])
    elif "address" in userString or "postcode" in userString or "street" in userString:
        print(df["Answers"][3])
    elif "web" in userString or "internet" in userString or "link" in userString:
        print(df["Answers"][4])
    elif "open" in userString or "visit" in userString or "time" in userString or "day" in userString or "long" in userString:
        print(df["Answers"][5])
        
# donation and sponsorship
    elif "donat" in userString or "money" in userString or "support" in userString or "account" in userString:
        print(df["Answers"][6])
    elif "sponsor" in userString or "sponsorship" in userString:
        print(df["Answers"][11])

# about the pound:
    elif "foundat" in userString or "found" in userString or "year" in userString:
        print(df["Answers"][7])
    elif "employe" in userString or "team" in userString or "keeper" in userString or "work" in userString:
        print(df["Answers"][8])
    elif "adopt" in userString or "get" in userString:
        print(df["Answers"][9])
    elif "animal" in userString or "populat" in userString or "pet" in userString:
        print(df["Answers"][10])
    
# animal population: dogs
    elif "female" in userString and "dog" in userString or "bitch" in userString:
        print(df["Answers"][14])
    elif "male" in userString and "dog" in userString:
        print(df["Answers"][13])
    elif "old" in userString or "senior" in userString and "dog" in userString:
        print(df["Answers"][16])
    elif "little" in userString or "small" in userString or "tiny" in userString or "short" in userString and "dog" in userString:
        print(df["Answers"][17])
    elif "big" in userString or "tall" in userString or "large" in userString and "dog" in userString:
        print(df["Answers"][18])
    elif "medium" in userString or "size" in userString and "dog" in userString:
        print(df["Answers"][19])
    elif "baby" in userString and "dog" in userString or "puppy" in userString or "pupp" in userString:
        print(df["Answers"][15])
    elif "dog" in userString or "doggie" in userString:
        print(df["Answers"][12])

# animal population: cats
    elif "female" in userString and "cat" in userString or "she-cat" in userString or "queen" in userString:
        print(df["Answers"][22])
    elif "male" in userString and "cat" in userString or "tom" in userString:
        print(df["Answers"][23])
    elif "baby" in userString or "young" in userString and "cat" in userString or "kitten" in userString:
        print(df["Answers"][24])
    elif "indoor" in userString or "inside" in userString or "flat" in userString and "cat" in userString:
        print(df["Answers"][25])
    elif "outdoor" in userString or "outside" in userString and "cat" in userString:
        print(df["Answers"][26])
    elif "cat" in userString or "feline" in userString:
        print(df["Answers"][21])
    
# animal population: rodents
    elif "rat" in userString or "mouse" in userString or "mice" in userString:
        print(df["Answers"][27])
    elif "guinea" in userString and "pig" in userString:
        print(df["Answers"][28])
    elif "rabbit" in userString or "hare" in userString or "bunny" in userString or "bunn" in userString or "doe" in userString or "buck" in userString:
        print(df["Answers"][29])

# birds
    elif "bird" in userString or "birdie" in userString or "budgie" in userString or "parrot" in userString:
        print(df["Answers"][30])

# exotic animals
    elif "exotic" in userString or "foreign" in userString or "snake" in userString or "chameleon" in userString or "reptile" in userString:
        print(df["Answers"][31])
        
# wild animals
    elif "wild" in userString:
        print(df["Answers"][32])

# lost animal
    elif "lost" in userString or "find" in userString or "disappear" in userString or "miss" in userString or "vanish" in userString or "stolen" in userString:
        print(df["Answers"][33])

# gimmick     
    elif "hello" in userString or "hi" in userString or "hey" in userString or "good" in userString and "afternoon" in userString or "morning" in userString or "evening" in userString:
        print(random.choice(gimmick))
    
# ending
    elif "bye"  in userString or "cu" in userString or "cheer" in userString or "see" in userString or "cya" in userString or "stop" in userString or "exit" in userString:
        print("Thank you for your interest. If you have another question regarding our pound at another time, you can always write to me. Bye-bye and whoof-whoof!")
        break

# unidentified user input:
    else:
        print("Unfortunately, I did not understand your input. Please reenter or reformulate your concern and check it for any spelling errors. If there is still a problem, please contact us during our opening hours on number +49 641 52251.")

       

