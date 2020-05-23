from googlesearch import search
import requests

DATA_AS_COMBINED = "cmbd"
DATA_AS_COMBINED_WITH_SPACE = "cmbdws"
DATA_AS_ARRAY = "arr"

def gimme_info(query, data_format, maxi=None, mini=0, domain_filter="com", language_filter="en"):
    text_results = []
    my_results_list = []
    for i in search(query,        # The query you want to run
                    tld = domain_filter,  # The top level domain
                    lang = language_filter,  # The language
                    num = 1,     # Number of results per page
                    start = mini,    # First result to retrieve
                    stop = maxi,  # Last result to retrieve
                    pause = 0,  # Lapse between HTTP requests
                ):
        my_results_list.append(i)
        

    for link in my_results_list:
        f = requests.get(link)


        info = f.text.split('<')

        main_info = []

        for i in info:
            try:
                first = list(i)[0]
                if first == 'p':
                    inner_text = i.split(">")[1]
                    if(len(inner_text)>0):
                        main_info.append(inner_text)
            except:
                pass

        if(data_format == "cmbd"):
            main_info_combined = "".join(main_info)
            text_results.append(main_info_combined)

        elif(data_format == "cmbdws"):
            main_info_combined = "\n\n".join(main_info)
            text_results.append(main_info_combined)
            
        elif(data_format == "arr"):
            text_results.append(main_info)

        else:
            return "Please specify the data format you woud like"
            print("Please specify the data format you woud like")

    return text_results
