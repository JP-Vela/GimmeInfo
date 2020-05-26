# gimmeinfo
A simple web scraper that takes in a search query and returns a specified number of results of text. from web pages.

#Insitallation

1. Run the setup.py script to make sure you have all the dependencies installed

2. Copy gimmeinfo.py and __init__.py to your project directory

3. Import  the file by using import gimmeinfo

#Getting started
Using GimmeInfo is very simple, all you need to do is run the gimme_info function.
Here is a quick example of how to use the function:
result = gimmeinfo.gimme_info(query="iPhone", data_format=search.DATA_AS_COMBINED, maxi=2, mini=0,language_filter="en")

query is the specific search query such as a google search

data_format specifies the form you want the return value in.
There are currently the following three data formats:
1. DATA_AS_COMBINED             The data in each website as one big string
2. DATA_AS_COMBINED_WITH_SPACE                The data in each website as one big string with newlines in between each paragraph
3. DATA_AS_ARRAY                The data in each website seperated into different elements of an array

max is the last result wanted

mini is the first result wanted

language_filter is the specified language code to filter out websites in any other language
