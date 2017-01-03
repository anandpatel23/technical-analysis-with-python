# only pull once per stock
# urllib2 opens http urls (authentication, redirections, cookies, etc.)
import urllib2
# timer not to overload sites
import time

stockToPull = 'AAPL' # AAPL, FB, UAA
stockRange = '1y' # 1y, 10d

def pullData(stock):
	try:
		# one time creation of stock's data to be stored here
		fileLine = stock + '.txt'
		urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=' + stockRange + '/csv'
		# visit, open, and split url
		openedSite = urllib2.urlopen(urlToVisit).read()
		splitSite = openedSite.split('\n')

		# grab valid lines after values esction
		for eachLine in splitSite:
			splitLine = eachLine.split(',')
			if len(splitLine) == 6:
				if 'values' not in eachLine:
					# append, don't write to not clear file
					saveFile = open(fileLine, 'a')
					lineToWrite = eachLine + '\n'
					saveFile.write(lineToWrite)

		print 'Pulled', stock
		print 'sleeping.'
		time.sleep(1)
		print 'sleeping..'
		time.sleep(1)
		print 'sleeping...'
		time.sleep(1)
		print 'done'

	except Exception, e:
		print 'error in main():', str(e)

pullData(stockToPull)