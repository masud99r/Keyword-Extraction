import re
def convert_camel(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1 \2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1 \2', s1).lower()
def tf_idf(document_file):
    df_dict = {}
    with open(document_file, "r") as docs:
        for doc in docs:
            doc_tokens = doc.split(" ")
            for i in range(0,len(doc_tokens)):
                count = int(df_dict[doc_tokens[i]])
                print ("count = "+count)
                count = count + 1
                df_dict[doc_tokens]=count
    print df_dict

def main():
    cluster = []
    fo = open("cluster2.txt", "w")

    with open("method_cluster_1.txt", "r") as ins:
        for line in ins:
            line_part = line.split("-")
            if len(line_part)>= 2:
                cluster.append(line_part[1])
                fo.write(convert_camel(line_part[1])+"\n")
                print (line_part[1])

if __name__ == "__main__":
    main()