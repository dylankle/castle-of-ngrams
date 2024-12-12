# Kingdom of N-Grams

## Description
Text adventure game in Python using a language model to generate a small sentence for the user to guess what the next word in the final room to win!

## UML
- main.py : main python file {run this} 
- room_data.json : json file with all the room information: description, possible key words, and connected vertices 
- word_generator.py : python file that has the n-gram tokenizer program from the extra credit assignment. takes puzzle_text.txt, tokenizes it, and turns it into a dictionary, word_data.json. - returns information back to main.py 
- puzzle_text.txt : text file with 100 word fantasty text to make the dictionary with 
- word_data.json : dictionary based on a word and the word that may come after. word_generator.py uses to generate 9 word sequence with random keys and values 

## Cheat Sheet
![Kingdom of NGrams (Graph)](https://github.com/user-attachments/assets/96d4d579-5dad-4b75-8f23-1898a3790cd4) <br/>
*Heads Up, the movement of the user in the game is fixed on North. This map is based on a cardinal directions*
