import speech_recognition as sr
from gtts import gTTS 
from PyDictionary import PyDictionary
import nltk 

nltk.download('wordnet')

from nltk.corpus import wordnet

#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

r = sr.Recognizer()

global text

print('If you want to stop this service, please say stop.')

print('Please start talking...')

dictionary=PyDictionary()


for i in range(100000000000000):
           
       with sr.Microphone() as source:
                
        r.adjust_for_ambient_noise(source)
    
        audio = r.listen(source)
                
        try:
            
            global text
                        
            text = r.recognize_google(audio)
            # set language = "ta" for tamil
                 
            if(text == 'stop'):
                
                break

            else:
                
                words = []
                
                synonyms = []
                
                antonyms = []
                
                words = text.split(" ")
                
                #print(words)
                
                if('meaning' in words or 'synonym' in words):
                    
                    word = words[2]
                    
                    print('Meaning:')
                    
                    print(dictionary.meaning(word))
                    
                    print("\n")
                                        
                    print('Synonyms are:')
                    
                    for syn in wordnet.synsets(word): 
                        for l in syn.lemmas(): 
                            synonyms.append(l.name()) 
                    
                    print(set(synonyms))
                    
                    print("\n");

                
                elif('opposite' in words or 'antonym' in words or 'antonyms' in words):
                    
                    word = words[2]
                    
                    print('Meaning:')
                    
                    print(dictionary.meaning(word))
                    
                    print("\n")
                                        
                    print('Antonyms are:')
                    
                    for syn in wordnet.synsets(word): 
                        for l in syn.lemmas(): 
                            if l.antonyms(): 
                                antonyms.append(l.antonyms()[0].name())
                    
                    print(set(antonyms))
                    
                    print("\n")    
            
                else:
                    
                    print("Could not hear you, please try again")                                    

        except sr.UnknownValueError:
            
            print("Could not hear you, please try again")
            

'''
mytext = "Hello world."

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=mytext, lang=language, slow=False) 

# Saving the converted audio in a wav file named sample
tts.save('sample.wav')

import winsound

filename = 'sample.wav'

winsound.PlaySound(filename, winsound.SND_FILENAME)


import pyttsx
engine = pyttsx.init()
engine.say('Good morning.')
engine.runAndWait()


import pyttsx3
engine = pyttsx3.init()
engine.say("hello world.")
engine.runAndWait()
'''        