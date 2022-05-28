import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
def recommend_hotel(location, description):
    description=description.lower()
    word_tokensize(description)
    stop_words=stopwords.words('English')
    lemm=WordNetLemmatizer()
    filtered ={word for word in description if not in stop_words}
    filtered_set =set()
    for fs in filtered:
            filtered_set.add(lemm.lemmatize(fs))
            
    country =data[data['countries']==location.lower()]
    country =country.set_index(np.arrange(country.shape[0]))
    list1=[];   list2 =[]; cos=[];
    for i in range(country.shape[0]):
        temp_token = word_tokensize(country["tags"][i])
        temp_set =[word for word in temp_token if not word in stop_words]
        temp2_set= set()
        for s in temp_set:
            temp2_set.add(lemm.lemmatize(s))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    country['similarity']=cos
    country = country.sort_values(by='similarity',ascending=False)
    country.drop_duplicates(subset='Hotel_Name', keep='first', inplace=True)
    country.sort_values('Average_score',ascending=False,implace=True)
    country.reset_index(inplace=True)
    return country[["Hotel_Name","Average_score","Hotel_Address"]].head()

