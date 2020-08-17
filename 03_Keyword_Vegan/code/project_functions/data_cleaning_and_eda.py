import regex as re
from nltk import WordNetLemmatizer
from bs4 import BeautifulSoup

'''
This dictionary is for expanding contraxctions in the NLP project_3
It was taken from this stack overflow site: https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
'''

contractions = {"ain't": "am not / are not / is not / has not / have not",
    "aren't": "are not / am not",
    "can't": "cannot",
    "can't've": "cannot have",
    "'cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he'd": "he had / he would",
    "he'd've": "he would have",
    "he'll": "he shall / he will",
    "he'll've": "he shall have / he will have",
    "he's": "he has / he is",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how'll": "how will",
    "how's": "how has / how is / how does",
    "I'd": "I had / I would",
    "I'd've": "I would have",
    "I'll": "I shall / I will",
    "I'll've": "I shall have / I will have",
    "I'm": "I am",
    "I've": "I have",
    "isn't": "is not",
    "it'd": "it had / it would",
    "it'd've": "it would have",
    "it'll": "it shall / it will",
    "it'll've": "it shall have / it will have",
    "it's": "it has / it is",
    "let's": "let us",
    "ma'am": "madam",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "she'd": "she had / she would",
    "she'd've": "she would have",
    "she'll": "she shall / she will",
    "she'll've": "she shall have / she will have",
    "she's": "she has / she is",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so as / so is",
    "that'd": "that would / that had",
    "that'd've": "that would have",
    "that's": "that has / that is",
    "there'd": "there had / there would",
    "there'd've": "there would have",
    "there's": "there has / there is",
    "they'd": "they had / they would",
    "they'd've": "they would have",
    "they'll": "they shall / they will",
    "they'll've": "they shall have / they will have",
    "they're": "they are",
    "they've": "they have",
    "to've": "to have",
    "wasn't": "was not",
    "we'd": "we had / we would",
    "we'd've": "we would have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we're": "we are",
    "we've": "we have",
    "weren't": "were not",
    "what'll": "what shall / what will",
    "what'll've": "what shall have / what will have",
    "what're": "what are",
    "what's": "what has / what is",
    "what've": "what have",
    "when's": "when has / when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where has / where is",
    "where've": "where have",
    "who'll": "who shall / who will",
    "who'll've": "who shall have / who will have",
    "who's": "who has / who is",
    "who've": "who have",
    "why's": "why has / why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "you'd": "you had / you would",
    "you'd've": "you would have",
    "you'll": "you shall / you will",
    "you'll've": "you shall have / you will have",
    "you're": "you are",
    "you've": "you have"}


def soupify(html_string):
    '''
    `soupify` creates a function that pulls the html-formatted text, lowercases everything and then splits it into tokens to make it ready for conversion and lemmatizing.
    
    Paramters
    ---------
    html_string: str
        an string with html elements that will be converted into a plain text.

    Returns
    -------
    souped_tokens: list
        list of words converted from html formatting to plain string.
    '''

    soup = BeautifulSoup(html_string, features="lxml")
    souped_tokens = soup.find('p').text.lower().replace('’',"'").split()
    return souped_tokens



def convert_contraction(contraction,contraction_dict=contractions):
    '''
    Uses the contraction dictionary found on the website at the end of this documenetation and expands contractions into the first entry of the dictionary for that contraction.

    Parameters
    ----------
    contraction: str
        contraction to be expanded by dictionary
    contraction_dict: dict
        dictionary of contractions

    Returns
    -------
    result
        either the original word or the expanded form of the contraction


    https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
    '''
    try:
        result = contraction_dict[contraction].split(' / ')[0]
    except:
        result = contraction.replace("'","")

    return result


def clean_string(dirty_string, lemmatizer=WordNetLemmatizer()):
    '''Pass `dirty_string` through `soupify` and `convert_contraction` to finally lemmatize the data for parsing.'''
    souped_tokens = soupify(dirty_string)
    expanded_str = ' '.join([convert_contraction(token) for token in souped_tokens])
    regex_tokens = re.split(r'\W',expanded_str)
    lemmatized_str = ' '.join([lemmatizer.lemmatize(token.lower(), "n") for token in regex_tokens])
    return lemmatized_str.strip()