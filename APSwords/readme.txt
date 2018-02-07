Hello!

Welcome to the APSwords README.

ABOUT:

APSwords.py is a short script I wrote in Python 3 to count the number of words in a .tex file according to the APS guidelines found here: https://journals.aps.org/authors/length-guide.

The program counts words in a string in the simplest possible way, by using string.split() and counting the length of the resulting list.

The difficult part is identifying which blocks of text in the .tex file should be counted in this way.

In summary, APSwords.py counts everything in the main body of the text (between the abstract and the acknowledgements) except for blocks of text enclosed by designated tokens, including \begin{figure}...\end{figure}, \begin{equation}...\end{equation}. 

Word count equivalents for figures and displayed equations are computed separately from the user inputs of the image aspect ratios and the number of lines of displayed equations in the main body. 

This is a work in progress.

USAGE:

1. Name the file you want to count "text2.tex".
2. Download APSwords.py to the same folder as "test2.tex". 
3. Open up a terminal, navigate to the folder, and type "python3 APSwords.py"

-Jacques
