


playagain = 0 

print('Welcome to the bitcoin Calculater. In this application you will be able to learn about the history of bitcoin, find the current value of a bitcoin as well as be able to search from past months and weeks on what bitcoins were valued at.')

raw_input('Enter if you would like to start')

while(playagain == 0):
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
		print("Since bitcoin has been public since 2013 what year would you like to see? ")
		year = raw_input('2010, 2011, 2012, 2013, 2014')
		if (year == '2010'):
			print('Now what month would you like to see? ')
			m1 = raw_input('Aug, Sept, Oct, Nov, Dec')
			if (m1 == "Aug"):
				print("The average price of a bitcoin was .065 USD")
			if (m1 == "Sept"):
				print("The average price of a bitcoin was .062 USD")
			if (m1 == "Oct"):
				print("The average price of a bitcoin was .10 USD")
			if (m1 == "Nov"):
				print("The average price of a bitcoin was .27 USD")
			if (m1 == "Dec"):
				print("The average price of a bitcoin was .24 USD ")
		if (year == '2011'):
			print('Now what month would you like to see? ')
			m2 = raw_input('Jan, Feb, Mar, Apr May, Jun, Jul Aug, Sept, Oct, Nov, Dec')
			if (m2 == 'Jan'):
				print("The average price of a bitcoin was .39 USD")
			if (m2 == 'Feb'):
				print("The average price of a bitcoin was .90 USD")
			if (m2 == 'Mar'):
				print('The average price of a bitcoin was .85 USD')
			if (m2 == "Apr"):
				print('The average price of a bitcoin was 1.50 USD')
			if (m2 == "May"):
				print('The average price of a bitcoin was 6.38 USD')
			if (m2 == "Jun"):
				print('The average price of a bitcoin was 18.55 USD')
			if (m2 == "Jul"):
				print('The average price of a bitcoin was 14.10 USD')
			if (m2 == "Aug"):
				print('The average price of a bitcoin was 9.75 USD')
			if (m2 == "Sep"):
				print('The average price of a bitcoin was 5.76 USD')
			if (m2 == "Oct"):
				print('The average price of a bitcoin was 3.30 USD')
			if (m2 == "Nov"):
				print('The average price of a bitcoin was 2.61 USD')
			if (m2 == "Dec"):
				print('The average price of a bitcoin was 3.51 USD')
		if (year == '2012'):
			print('Now what month would you like to see?  ')
			m3 = raw_input('Jan, Feb, Mar, Apr May, Jun, Jul Aug, Sept, Oct, Nov, Dec')
			if (m3 == 'Jan'):
				print("The average price of a bitcoin was 6.11 USD")
			if (m3 == 'Feb'):
				print("The average price of a bitcoin was 5.06 USD")
			if (m3 == 'Mar'):
				print('The average price of a bitcoin was 4.88 USD')
			if (m3 == "Apr"):
				print('The average price of a bitcoin was 4.98 USD')
			if (m3 == "May"):
				print('The average price of a bitcoin was 5.06 USD')
			if (m3 == "Jun"):
				print('The average price of a bitcoin was 6.03 USD')
			if (m3 == "Jul"):
				print('The average price of a bitcoin was 8.04 USD')
			if (m3 == "Aug"):
				print('The average price of a bitcoin was 10.88 USD')
			if (m3 == "Sep"):
				print('The average price of a bitcoin was 11.46 USD')
			if (m3 == "Oct"):
				print('The average price of a bitcoin was 11.58 USD')
			if (m3 == "Nov"):
				print('The average price of a bitcoin was 11.51 USD')
			if (m3 == "Dec"):
				print('The average price of a bitcoin was 13.33 USD')
		if (year == '2013'):
			print('Now what month would you like to see? ')
			m3 = raw_input('Jan, Feb, Mar, Apr May, Jun, Jul Aug, Sept, Oct, Nov, Dec')
			if (m3 == 'Jan'):
				print("The average price of a bitcoin was 16.31 USD")
			if (m3 == 'Feb'):
				print("The average price of a bitcoin was 25.93 USD")
			if (m3 == 'Mar'):
				print('The average price of a bitcoin was 58.14 USD')
			if (m3 == "Apr"):
				print('The average price of a bitcoin was 115.19 USD')
			if (m3 == "May"):
				print('The average price of a bitcoin was 112.81 USD')
			if (m3 == "Jun"):
				print('The average price of a bitcoin was 108.39 USD')
			if (m3 == "Jul"):
				print('The average price of a bitcoin was 83.60 USD')
			if (m3 == "Aug"):
				print('The average price of a bitcoin was 105.80 USD')
			if (m3 == "Sep"):
				print('The average price of a bitcoin was 124.33 USD')
			if (m3 == "Oct"):
				print('The average price of a bitcoin was 156.50 USD')
			if (m3 == "Nov"):
				print('The average price of a bitcoin was 517.00 USD')
			if (m3 == "Dec"):
				print('The average price of a bitcoin was 799.00 USD')
		if (year == '2014'):
			print('Now what month would you like to see? ')
			m4 = raw_input('Jan, Feb, Mar, Apr May, Jun, Jul Aug, Sept, Oct, Nov, Dec')
			if (m4 == 'Jan'):
				print("The average price of a bitcoin was 800 USD")
			if (m4 == 'Feb'):
				print("The average price of a bitcoin was 565 USD")
			if (m4 == 'Mar'):
				print('The average price of a bitcoin was 452 USD')
			if (m4 == "Apr"):
				print('The average price of a bitcoin was 448.27 USD')
			if (m4 == "May"):
				print('The average price of a bitcoin was 635.60 USD')
			if (m4 == "Jun"):
				print('The average price of a bitcoin was 640.01 USD')
			if (m4 == "Jul"):
				print('The average price of a bitcoin was 579.04 USD')
			if (m4 == "Aug"):
				print('The average price of a bitcoin was 483.37 USD')
			if (m4 == "Sep"):
				print('The average price of a bitcoin was 387.14 USD')
			if (m4 == "Oct"):
				print('The average price of a bitcoin was 337.00 USD')
			if (m4 == "Nov"):
				print('The average price of a bitcoin was 376.72 USD')
			if (m4 == "Dec"):
				print('The average price of a bitcoin was 317.00 USD')
	print("Would you like to continue learning about Bitcoins?")
	value = raw_input("Yes or No")
		
	if(value == 'Yes'):
		playagain = 0
	if(value == 'No'):
		playagain = 1

