#WordCount.py
#Name: Emily Billings
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lineCount = 0
  wordCount = 0
  letterCount = 0 
  charactersCount = 0
  
  for line in textFile:
    lineCount = lineCount + 1
    words = line.split()
    for w in words:
      wordCount = wordCount + 1 
    
    for ch in line.strip("\n"): 
      charactersCount +=1
    
    #print(line)

    print("Lines:", lineCount)
    print("Words:", wordCount)
    print("characters:", charactersCount)
    charactersCount +=1
    
    print("characters:", charactersCount)
  
if __name__ == '__main__':
  main()
