import re
import sys

def main():
    #extract text as a string from file
    file = open('test2.tex','r')
    string = file.read()
    file.close()
    #trim the string down to the main body (the part between abstract and ac knowledgements or bibliography, whichever comes first). This avoids capturing sections of text from eg. the appendix or elsewhere. Exclude the start and end tokens.
    match=re.search(r'(?:\\end\{abstract\}(.*?)\\begin\{(thebibliography|acknowledgments)\})', string, flags=re.DOTALL)    
    #exit with error if the result is empty
    if not match:
        print('Error: main body of text appears empty.')
        sys.exit(1)
    #Enclose main body between a begin{...} and end{...} that the subsequent regex will recognize.
    trim='\end{figure}'+match.group(1)+'\\begin{figure}'   
    #in the main body, capture only text in between certain pre-identified delimiters, eg. from the ending of the abstract, figures, or equations to the beginning of the next figure, equation, acknowledgements or bibliography.
    matchtuple=re.findall(r'(?:\\end\{(equation|figure)\}(.*?)\\begin\{(equation|figure)\})', trim, flags=re.DOTALL)
    if not matchtuple:
        print('no match')
        sys.exit(1)
    words=''
    for i in range(0,len(matchtuple)):
        words+=matchtuple[i][1]
    wordlist=words.split()
    ar1=115/86
    ar2=277/61
    ar3=183/110
    imgcount=(150/ar1+20)+(300/ar2+40)+(150/ar3+20)
    eqrows=13
    eqncount=eqrows*16
    count=len(wordlist)+imgcount+eqncount
    print('word count = '+str(count))

if __name__=='__main__':
    main()
