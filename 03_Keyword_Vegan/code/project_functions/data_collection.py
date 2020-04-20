import requests
import pandas as pd

def get_data_json(pull_no, base_url, url_paramaters): 
    '''
    Pull data item from json designated by url and url parameters.

    Parameters
    ==========
    pull_no: int
    	counts number of pulls requested

    base_url: str
    	base url for the request
    	default: (url = 'https://api.pushshift.io/reddit/submission/search')

    url_paramaters: dict
    	dictionary of request paramters

    Returns
    =======
	data: list
		list of values stored in under the 'data' key in the responses json.
    '''

    # print the pull number and subreddit we will submit a request to
    print(f"r/{url_paramaters['subreddit']}")
    print(f"Pull number {pull_no + 1}")
        
    # Call to pushshiftIO
    res = requests.get(base_url, url_paramaters)

    # Print the url, showing the parameters in case there is an error.
    # print(res.url)

    data = res.json()['data'] 

    return data



def create_doc(vegan_bool, post):
    '''
    Receive a post and the vegan-value (0 or 1) and return 
    the dictionary of the desired values: `title`, `selftext`.

    Parameters
    ----------
    vegan_bool: int (0,1)
    	whether the post is from r/Vegan or not
    post: dict
    	post from the subreddit as a dictionary

    Returns
    -------
    doc: dictionary
    	document to be appended to the batch of documents before being appended to the corpus.
    '''

    # Instantiate document dictionary with title and vegan_bool value

    doc = {
        'title': post['title'],
        'vegan': vegan_bool
    }
    
    # If selftext exists, add it to the document, otherwise insert None and warn user
    try:
        doc['selftext'] = post['selftext']
    except:
        doc['selftext'] = None
        # print(f"post_id: {post['id']} no selftext. Appending title only.")
        # print(doc)
              
    return doc



def append_to_corpus(batch, corpus):
    '''
    Convert batch into a dataframe and append it to the corpus csv.
    Returns the oldest posts time stamp.

    Parameters
    ----------
    batch: list
    	list of dictionaries to be appended to the corpus
   	corpus: str = '../data/train.csv'
   		file location for the corpus csv
    '''

    # Convert batch_list of documents into a dataframe.
    df_batch = pd.DataFrame(batch,index=None)

    # Concatenate new dataframe to corpus from csv.
    with open(corpus, 'a') as f:
        df_batch[['title','selftext','vegan']].to_csv(f, header=False, index=False)
              
    print(f"{len(df_batch)} documents appended to corpus.")

             
              
              
