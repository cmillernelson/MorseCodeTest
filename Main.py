import datetime
import statistics

DATE_TIME = 0
PRICE = 1
UNITS = 2

# ASSUMPTION: The trades in the given file are already sorted by dateTime from earliest to most recent.
# Also, I know that putting the print statements straight into the calculation methods is garbage, but there are a lot
# of possible print statements if on time is given.


def main():
    file_name = input("Path of the sales file to read: ")
    file_info = import_file(file_name)
    input_times = input("Datetime(s) of trade or series of trades: ")
#   times = []
    times = input_times.split()
    # Convert input string(s) into datetime object(s)
    for entry in range(0, len(times)):
        times[entry] = datetime.datetime.strptime(times[entry], "%Y-%m-%dT%H:%M:%SZ")

    get_trade_stats(file_info, times)


# Imports a given file into a 2D list split on new lines and spaces
# For the purposes of this test, we'll assume that the file is exactly what we need it to be and nothing else
def import_file(file_name):
    file_info = []
    with open(file_name) as file:
        for line in file:
            file_info.append(line.split())

    # Now that the data is in the list of lists, we need to convert to datetime object, float, and int
    for transaction in file_info:
        transaction[0] = datetime.datetime.strptime(transaction[DATE_TIME], "%Y-%m-%dT%H:%M:%SZ")
        transaction[1] = float(transaction[1])
        transaction[2] = int(transaction[2])
    return file_info


# Helper method for calculateStatsmethods.
def get_trade_stats(file_info, times):
    if len(times) == 1:
        calculate_stats_for_one_time(file_info, times)
    else:
        return calculate_stats_for_two_times(file_info, times)


# Calculates statistics if one timestamp was entered
def calculate_stats_for_one_time(file_info, times):
    # In case a trade is entered from before the file starts keeping track
    if file_info[0][0] > times[0]:
        print("The price of the closest trade to this time was " + str(file_info[0][PRICE]))
        return file_info[0][PRICE]

    price_of_closest_time = file_info[0][PRICE]
    for trade in file_info:
        if times[0] == trade[DATE_TIME]:
            print("The price of the trade at this time was " + str(trade[PRICE]))
            return trade[PRICE]
        elif trade[DATE_TIME] > times[0]:
            print("The average price for the trades around this time was "
                  + str((price_of_closest_time + trade[PRICE]) / 2))
            return price_of_closest_time * trade[PRICE] / 2
        else:
            price_of_closest_time = trade[PRICE]

    # If the for loop ends and the time was never found or exceeded
    print("The price of the closest trade to this time was " + str(price_of_closest_time))
    return price_of_closest_time


# Calculates statistics if two timestamps were entered
def calculate_stats_for_two_times(file_info, times):
    prices_of_trades = []
    for trade in file_info:
        if times[0] <= trade[DATE_TIME] <= times[1]:
            prices_of_trades.append(trade[PRICE])

    print("The highest price of trades made during this time was " + str(max(prices_of_trades)))
    print("The lowest price of trades made during this time was " + str(min(prices_of_trades)))
    print("The average price of trades made during this time was " + str(statistics.mean(prices_of_trades)))
    print("The standard deviation in price of trades made during this time was "
          + str(statistics.stdev(prices_of_trades)))
    print("The median price of trades made during this time was " + str(statistics.median(prices_of_trades)))
    return [max(prices_of_trades), min(prices_of_trades), statistics.mean(prices_of_trades),
            statistics.stdev(prices_of_trades), statistics.median(prices_of_trades)]


if __name__ == '__main__':
    main()
