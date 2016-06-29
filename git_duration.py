import git
from git import Repo
repo = Repo("php-src")  
list_of_commits = list(repo.iter_commits("master", max_count = 100))


def reverted_commits(list_of_commits):   # finds messages that have "revert" in them and returns the hex num for commit
	reverted_commits = []
	for commit in list_of_commits:
		messages = commit.message
		if "revert" in messages:
			reverted_commits.append(commit)
	return reverted_commits

revert_commits = reverted_commits(list_of_commits) #e in other functions


def revert_message(list_of_commits): # returns the message that contains "revert"
	len_revert_commits = len(revert_commits)
	commits = []
	for commit in list_of_commits:
		messages = commit.message
		if "revert" in messages:
			commits.append(messages)
			#if len(commits) != len_revert_commits:

	return commits

messages = revert_message(list_of_commits)

def hex(message): # returns the hex_num in string
	hex_num = []
	for string in message:
		for word in string.split():
			if len(word) > 20:
				hex_num.append(word)
				j = 0 
				for letter in hex_num:
					hex_num[j] = letter.strip(".")
					j+= 1
	return hex_num
string_commits = hex(messages)


def get_commit(entire_repo): #finds git commit of the string
	git_commit = []
	string_commits = hex(messages)
	for commit in entire_repo:
		for string in string_commits:
			if str(commit) == string:
				git_commit.append(commit)
	return git_commit


all_commits = list(repo.iter_commits())
init_commit = get_commit(all_commits)

def time(commits): # returns time of commit in epoch
	import time
	import datetime
	times = []
	for each in commits:
		times.append(each.committed_date) 
	return times

init_time = time(init_commit)
revert_time = time(revert_commits)

def difference(revert_time,init_time): #finds difference of times
	diff = []
	import datetime
	import dateutil.relativedelta
	for time in range(len(init_time)):
		time_one = datetime.datetime.fromtimestamp(revert_time[time])
		time_two = datetime.datetime.fromtimestamp(init_time[time])
		rd = dateutil.relativedelta.relativedelta(time_one, time_two)
		diff.append("%d:yrs, %d:mths, %d:d, %d:hrs, %d:min, %d:secs" % (rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds))
	return diff
	
print (difference(revert_time,init_time))

