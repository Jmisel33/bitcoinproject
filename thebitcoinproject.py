 

print('Welcome to the bitcoin Calculater. In this application you will be able to learn about the history of bitcoin, find the current value of a bitcoin as well as be able to search from past months and weeks on what bitcoins were valued at.')

raw_input('Enter if you would like to start')

print('What would you like to see?')

print("If youd like to see the history of Bitcoin type history")
print("If youd like to see the Current Value type cv")
print("If youd like to see the value of bitcoins since they went public type charts")
choice = raw_input("What would like to see?")
 





if (choice == 'history'):
	print("In November 2008, a paper was posted on the internet under the name Satoshi Nakamoto titled bitcoin: A Peer-to-Peer Electronic Cash System. This paper detailed methods of using a peer-to-peer network to generate what was described as 'a system for electronic transactions without relying on trust'. In January 2009, the bitcoin network came into existence with the release of the first open source bitcoin client and the issuance of the first bitcoins with Satoshi Nakamoto mining the first block of bitcoins ever known as the genesis block, which had a reward of 50 bitcoins. The value of the first bitcoin transactions were negotiated by individuals on the bitcointalk forums with one notable transaction of 10,000 BTC used to indirectly purchase two pizzas delivered by Papa John's.")
	print("On 6 August 2010, a major vulnerability in the bitcoin protocol was spotted. Transactions 	werent properly verified before they were included in the transaction log or blockchain, which let users bypass bitcoins economic restrictions and create an indefinite number of bitcoins. On 15th August, the vulnerability was exploited; over 184 billion bitcoins were generated in a transaction, and sent to two addresses on the network. Within hours, the transaction was spotted and erased from the transaction log after the bug was fixed and the network forked to an updated version of the bitcoin protocol. This was the only major security flaw found and exploited in bitcoins history")

if (choice == 'cv'):
	print("As of today Monday May 15th, the curent value of a bitcoin is $1715.21 Which is 1200 dollars more than it was last year at the same date.")
if (choice == 'charts'):
	print("Since bitcoin has been public since 2013 what year would you like to see?")
	year = raw_input('2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017')
	if (year == '2010'):
		print('Now what month would you like to see?')
		m1 = raw_input('Aug, Sept, Oct, Nov, Dec')
		if (m1 == "Aug"):
			print("The average price of a bitcoin was .065 USD")
		if (m1 == "Sept"):
			print("The average price of a bitcoin was .062 USD")
		