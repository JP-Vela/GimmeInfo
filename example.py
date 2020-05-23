import gimmeinfo as search

result = search.gimme_info(query="iPhone", data_format=search.DATA_AS_COMBINED, maxi=2, mini=0,language_filter="en")
print(result)

