import urllib

def read_text():
    
    ''' Reads and Prints the content of file.
        NOTE: The file should in the same folder containing the script.
    '''
    
    fileName = raw_input("Enter the file name: ")
    quotes = open(fileName)
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    
    ''' Connects to 'What do you love meta search engine from Google'
        and check for the cuss words.
        Returns 'True' if our file contains cuss words.
    '''
    
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = connection.read()
    print(output)
    connection.close()


read_text()
