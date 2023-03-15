# Assignment Part #1
import pandas as pd
import numpy as np 

class PricesAnalytics():
    
    def median_price():
        # example prices list
        prices = [100000, 150000, 200000, 300000, 500000]

        # calculate median
        median_price = np.median(prices)

        # print result
        print("Median price:", median_price)
    
    def avg_price():
         # example prices list
        prices = [100000, 150000, 200000, 300000, 500000]

        # calculate average
        average_price = sum(prices) / len(prices)

        # print result
        print("Average price:", average_price)
    
    def price_distribution():
        import matplotlib.pyplot as plt

        # example prices list
        prices = [100000, 150000, 200000, 300000, 500000]

        # plot histogram of prices
        plt.hist(prices)

        # add labels
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.title("Price Distribution")

        # show plot
        plt.show()
    
    def price_trends():
        import matplotlib.pyplot as plt

        # example prices over time
        prices = [100000, 150000, 200000, 300000, 500000]
        years = [2010, 2011, 2012, 2013, 2014]

        # plot prices over time
        plt.plot(years, prices)

        # add labels
        plt.xlabel("Year")
        plt.ylabel("Price")
        plt.title("Price Trends")

        # show plot
        plt.show()
    