import time
import datetime
import numpy as np
import matplotlib.pyplot as mplot
import matplotlib.ticker as mticker
import matplotlib.dates as mdates

stocks = 'AAPL', 'FB', 'UAA'

def graphData(stock):
	try:
		s = stock + '.txt'

		# load values and format the date
		date, closePrice, highPrice, lowPrice, openPrice, volume = np.loadtxt(s, delimiter=',', unpack=True, converters={0: mdates.strpdate2num('%Y%m%d')})

		f = mplot.figure()
		a = mplot.subplot(1,1,1) # plot a graph at the first position on a 1x1 plo
		a.plot(date, openPrice)
		a.plot(date, highPrice)
		a.plot(date, lowPrice)
		a.plot(date, closePrice)

		a.xaxis.set_major_locator(mticker.MaxNLocator(10))
		a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

		for label in a.xaxis.get_ticklabels():
			label.set_rotation(45)


		mplot.show()


	except Exception, e:
		print 'error in main:', str(e)


graphData('AAPL')