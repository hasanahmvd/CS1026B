# Written by Syed Ahmed (sahme339)
# 21 March 2018
# CS 1026B Assignment 3
# Purpose: to evaluate and organize tweets by happiness score with evaluating keywords associated with a score       then using the results to determine the happiness score by location
import string
def main():
    # call input_keyword function to take in keywords form txt file into a dictionary 
    k_dict = input_keyword()
    # call input_tweets function to take in tweets form txt file into a list 
    t_list = input_tweets()
    # create dict to store tweet count and score
    time_zones = {'Pacific': [0,0],
               'Moutain': [0,0], 
               'Central': [0,0],
               'Eastern': [0,0]}
    # loop through tweets
    for x in t_list:
        # check that long and lat are in area
        if(x[0] is not None):
            # get score
            temp_score = t_happiness(x[4:], k_dict)
            # uodate count for that area
            time_zones[x[0]][0] = time_zones[x[0]][0] + 1
            # update score for that area
            time_zones[x[0]][1] = time_zones[x[0]][1] + temp_score
    # loop through time zones and print score and count
    for y in time_zones:
        print(y + " Zone Has " + str(time_zones[y][0]) +" tweets and " + str(time_zones[y][1]) +" happiness score")
    
    
# function to sote keywords from text into dict
def input_keyword():
    # open the user inoutted file
    file_name = open(str(input("Enter Keyword File name(omit .txt): ")) + '.txt', 'r',encoding="utf-8")
    # split file into lines
    file_lines = file_name.readlines()
    # create a dict to store keyword and values
    keyword_dict = {}
    # loop through lines in txt file
    for x in file_lines:
        # split sre line into word and score
        insert = x.split(',')
        # store word as key and score as value in dict
        keyword_dict[insert[0]] = int(insert[1])
    # return dict
    return keyword_dict


# function to sote tweets from text into list
def input_tweets():
    # open the user inputted file 
    file_name = open(str(input("Enter Tweets File name(omit .txt): ")) + '.txt', 'r',encoding="utf-8")
    # split files into lines
    file_lines = file_name.readlines()
    # create a dict to store tweet and info
    tweet_list = []
    # loop through lines in txt file
    for x in file_lines:
        # split each tweet into seperate items in a list
        insert = x.split()
        # append split line to main list
        tweet_list.append(t_info(insert))
        
    return tweet_list


# adjusts the tweet lists
def t_info(tweet_line):
    # make temp list
    info = []
    # take long and lat while getting rid og comma and brackets
    x_val = tweet_line[0][1:-1]
    y_val = tweet_line[1][:-1]
    # get the area form the long at lat
    info.append(c_lookup(float(x_val),float(y_val)))
    # replace long and lat with area name
    info = info + tweet_line[2:]
    # return adjusted list
    return info


# function to look up the area(time zone) 
def c_lookup(lat, long):
    # var for all coordinates
    pos1 = (49.189787, -67.444574)
    pos2 = (24.660845, -67.444574)
    pos3 = (49.189787, -87.518395)
    pos4 = (24.660845, -87.518395)
    pos5 = (49.189787, -101.998892)
    pos6 = (24.660845, -101.998892)
    pos7 = (49.189787, -115.236428)
    pos8 = (24.660845, -115.236428)
    pos9 = (49.189787, -125.242264)
    pos10 = (24.660845, -125.242264)   
    # if lat not within range set area as none
    if( lat > pos1[0] or lat < pos2[0]):
        region = None
    # if long not within range set area as none
    elif( long > pos1[1] or long < pos10[1]):
        region = None
    # nested if loop to compare coordinates with positions and set correct name
    else:
        if(long < pos5[1] ):
            if(long > pos7[1]):
                region = 'Moutain'
            else:
                region = 'Pacific'
        else:
            if(long > pos3[1]):
                region = 'Eastern'
            else:
                region = 'Central'
    # return area
    return region


# function to calculate happiness score    
def t_happiness(text_list, key_dict):
    # counter
    score = 0
    # loop through words
    for x in text_list:
        # strip punctuation away and put it into lower case
        word = x.lower().strip(string.punctuation)
        # if words are in keywords then add score
        if(word in key_dict.keys()):
            score = score + key_dict[word]
    # return the score
    return score

main()
    
