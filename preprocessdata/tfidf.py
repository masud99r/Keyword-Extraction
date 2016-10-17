import re
import numpy as np
import operator

from nltk.stem.snowball import EnglishStemmer  # load the stemmer module from NLTK
def convert_camel(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower()
def tf_idf(document_file):
    df_dict = {}
    processed_documents = []
    stemmer = EnglishStemmer()  # get an instance of SnowballStemmer for English
    total_doc=0
    with open(document_file, "r") as docs:
        for doc in docs:
            total_doc += 1
            unique_doc = {}
            doc_tokens = doc.split(" ")
            for i in range(0,len(doc_tokens)):
                token = doc_tokens[i].replace("\n","")
                stemmed_token = stemmer.stem(token)
                if stemmed_token=="":
                    #print ("test")
                    continue
                if unique_doc.__contains__(stemmed_token):
                    tf_count= int(unique_doc[stemmed_token])
                else:
                    tf_count = 0
                unique_doc[stemmed_token] = tf_count + 1

            for key, value in unique_doc.iteritems():
                if df_dict.__contains__(key):
                    count = int(df_dict[key])
                else:
                    count = 0
                #print ("count = " + str(count))
                df_dict[key] = count + 1

            processed_documents.append(unique_doc)
    #print processed_documents

    #print df_dict
    #print ("test")
    print (total_doc)
    idf_dict = {}
    for key, value in df_dict.iteritems():
        idf_val = 1+np.log10((total_doc*1.0)/float(value))
        idf_dict[key]=idf_val
    #print idf_dict

    tfidf_all_dict = []
    for i in range(0, len(processed_documents)):
        single_doc_tf = processed_documents[i]
        single_tfidf_dict = {}
        for key, value in single_doc_tf.iteritems():
            if value > 0:
                tf_sublin = 1+ np.log10(value) #sublinear tf scaling
            else:#should never happen
                tf_sublin=0
            if idf_dict.__contains__(key):
                idf_val = idf_dict[key]
            else:
                idf_val=0 #should never happen
            tfidf_val = tf_sublin*idf_val
            single_tfidf_dict[key]=tfidf_val
        sorted_tfidf_single = sorted(single_tfidf_dict.items(), key=operator.itemgetter(1),reverse=True)
        tfidf_all_dict.append(sorted_tfidf_single)


    sorted_idf = sorted(idf_dict.items(), key=operator.itemgetter(1),reverse=True)
    #print sorted_idf
    print tfidf_all_dict[1]


def main():
    tf_idf("sample.txt")
if __name__ == "__main__":
    main()