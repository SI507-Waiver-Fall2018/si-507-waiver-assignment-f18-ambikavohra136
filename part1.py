
import tweepy
import nltk
import json
import sys

#authentication info
#note: I used Akshat Mishra's consumer token and secret authentication information since my developer account 
#was not being approved. As of July 2018, Twitter requires account review, and it was taking over a week.

consumer_token = "fzTKr5UJm5JEYdtMGo4359QYJ"
consumer_secret = "aVo6QqSjjNe18n3YW2uEsjEOovNMvFlrZYpGJK3WrWjeKLrX05"
access_token = "2470112398-BdgcMHVcYLBJkMYvDTNBQWuJYhCQC223ZxUQB4S"
access_token_secret = "UB8ANuStsE6GiRkOiKBlG8QIQm6WpJhLUQ6iuuPVaGkKs"

#consumer_token="49BmWVAmYNPQIsZKH6He5Vz4U"
#consumer_secret="x7jOBsbnKMWgUJIkO9Q2gwqdzZGQH4suR9EsLdsRBLpJd2z88g"
#access_token= "2470112398-ukyX7hgljgvatQ52F9DsBxhwsBT61hdatc0Cw4n"
#access_token_secret="csJX9ITJ3MVPqMLXk5Ewf8lzG4bXz4fhLkGeTi54ugnOx"


#authentication
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#get command line arguments using sys module
username = sys.argv[1]
countTweets = int(sys.argv[2])

#define words to ignore
stopWords = ['http', 'https','RT']

#get # of specified tweets from provided username (without retweets)
tweets = api.user_timeline(screen_name=username, count=countTweets, include_rts = 'false')
origtweets = len(tweets)

#instantiate variables for favorites and retweet
countFavorite = 0
countRetweet = 0

#insantiate list to keep processed tweet words
tweetWords = []

#iterate through tweets
for tweet in tweets:
	#print(tweet)
	countFavorite += tweet.favorite_count
	countRetweet += tweet.retweet_count
	tweetText = tweet.text
	#tokenize tweet
	tokens = nltk.word_tokenize(tweetText)
	for word in tokens:
		#filter through conditions
		if (word[0].isalpha() and (word not in stopWords) and len(word)>1):
			tweetWords.append(word)

#tag the valid tweet words with classifications for noun, verb, adj
tagged = nltk.pos_tag(tweetWords)
#print(tagged[0:2])

#instantiate lists for verbs, nouns, adjs
verbs = []
nouns = []
adjectives = []

#go through tagged words and classify each as noun, adj, or verb
for word,tag in tagged:
	#print(word)
	#print(tag)
	if tag == "NN":
		nouns.append(word)
	elif tag == "VB":
		verbs.append(word)
	elif tag =="JJ":
		adjectives.append(word)

#print(nouns)
#print(verbs)
#print(adjectives)

#instantiate a dictionary for most frequent verbs, adj, nouns
#key: word, value: frequency
freq_verbs = {}
freq_adjs = {}
freq_nouns = {}


#get count for verbs
for verb in verbs:
	if verb in freq_verbs.keys():
		freq_verbs[verb]+=1
	else:
		freq_verbs[verb]=1


#get count for adjs
for adj in adjectives:
	if adj in freq_adjs.keys():
		freq_adjs[adj]+=1
	else:
		freq_adjs[adj]=1


#get count for nouns
for noun in nouns:
	if noun in freq_nouns.keys():
		freq_nouns[noun]+=1
	else:
		freq_nouns[noun]=1

#sort each dictionary by value (2nd part of pair), descending
freq_nouns_sort = sorted(freq_nouns.items(), key=lambda x: x[1], reverse=True)
freq_verbs_sort = sorted(freq_verbs.items(), key=lambda x: x[1], reverse=True)
freq_adjs_sort = sorted(freq_adjs.items(), key=lambda x: x[1], reverse=True)

#get 5 most common verbs, adjs, nouns and their values
fivefreqNouns = freq_nouns_sort[:5]
fivefreqAdjs = freq_adjs_sort[:5]
fivefreqVerbs = freq_verbs_sort[:5]

#open csv file
file = open("noun_data.csv", "w")
#write headings
file.write("Noun,Number\n")
print("USER: " + username + "\n" + "TWEETS ANALYZED: " + str(countTweets))

print("\n")

#verb data
print("VERBS: ")
for verb in fivefreqVerbs:
	print(verb[0] + "(" + str(verb[1]) + ")" + "")


print("\n")

#adj data
print("ADJECTIVES: ")
for adj in fivefreqAdjs:
	print(adj[0] + "(" + str(adj[1]) + ")" + "")

print("\n")

#adj data
print("NOUNS: ")
for noun in fivefreqNouns:
	print(noun[0] + "(" + str(noun[1]) + ")" + "")
#write noun data to file
	file.write(noun[0] + "," + str(noun[1]) + "\n")

print("\n")

#print misc info
print("ORIGINAL TWEETS: " + str(origtweets))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): " + str(countFavorite))
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): " + str(countRetweet))

#end!
file.close()




