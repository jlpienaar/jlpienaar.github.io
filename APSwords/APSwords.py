import re
import sys

def main():
    #extract text as a string from file
    filename=input('Enter the name of the .tex file you want to count: ')
    file = open(filename,'r')
    string = file.read()
    file.close()
    arlist=[]
    fig1cols=int(input('Enter number of 1-column figures: '))
    for i in range(0,fig1cols):
        newar=input('Enter aspect ratio (width / height) of one-column image number '+str(i+1)+': ')
        arlist.append(newar)
    fig2cols=int(input('Enter number of 2-column figures: '))
    for i in range(0,fig2cols):
        newar=input('Enter aspect ratio (width / height) of two-column image number'+str(i+1)+': ')
        arlist.append(newar)
    eqn1cols=int(input('Enter number of rows of 1-column equations: '))
    eqn2cols=int(input('Enter number of rows of 2-column equations: '))
    numfigs=fig1cols+fig2cols
    #trim the string to the main body (the part between abstract and ac knowledgements or bibliography, whichever comes first). This avoids capturing sections of text from eg. the appendix or elsewhere. Exclude the start and end tokens.
    endtoken=r'\\begin\{(thebibliography|acknowledgments)\}'
    custom=input('Use custom end token? (y/n) : ')
    if custom=='y':
        endtoken=r'\\appendix'
    match=re.search(r'(?:\\end\{abstract\}(.*?)'+endtoken+r')', string, flags=re.DOTALL)    
    #exit with error if the result is empty
    if not match:
        print('Error: main body of text appears empty.')
        sys.exit(1)
    #Enclose main body between a begin{...} and end{...} that the subsequent regex will recognize.
    trim='\end{figure}'+match.group(1)+'\\begin{figure}'   
    #in the main body, capture only text in between certain pre-identified delimiters, eg. from the ending of the abstract, figures, or equations to the beginning of the next figure, equation, acknowledgements or bibliography.
    matchtuple=re.findall(r'(?:\\end\{(equation|figure|eqnarray|align)\}(.*?)\\begin\{(equation|figure|eqnarray|align)\})', trim, flags=re.DOTALL)
    #Exit if there is no match
    if not matchtuple:
        print('no match')
        sys.exit(1)
    #Combine the extracted blocks of text into a single string    
    words=''
    for i in range(0,len(matchtuple)):
        words+=matchtuple[i][1]
    #count the words and add to the counts obtained for images and displayed math    
    wordlist=words.split()
    #for each image, add its wordcount:
    imgcount=0
    for i in range(0,fig1cols):
        imgcount+=(150/float(arlist[i])+20)
    for i in range(1,fig2cols+1):
        imgcount+=(300/float(arlist[-i])+40)
    #count the words for eqns:
    eqncount=eqn1cols*16+eqn2cols*32
    count=len(wordlist)+imgcount+eqncount
    print('words in main text (including inline equations): '+str(len(wordlist)))
    print('word equivalent of images: '+str(imgcount))
    print('word equivalent of displayed equations: '+str(eqncount))
    print('words excluding figures: '+str(eqncount+len(wordlist)) )
    print('total word count = '+str(count))
    
if __name__=='__main__':
    main()
