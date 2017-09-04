import unittest
import datetime
from Main import calculate_stats_for_one_time
from Main import calculate_stats_for_two_times


class SalesStatsTestCase(unittest.TestCase):
    def test_calculate_stats_for_one_time(self):
        trade_info = [[datetime.datetime.strptime("2017-03-01T13:37:59Z", "%Y-%m-%dT%H:%M:%SZ"), float(21.37), int(100)],
                      [datetime.datetime.strptime("2017-04-25T17:11:55Z", "%Y-%m-%dT%H:%M:%SZ"), float(20.18), int(55)],
                      [datetime.datetime.strptime("2017-05-19T05:49:34Z", "%Y-%m-%dT%H:%M:%SZ"), float(23.09), int(21)],
                      [datetime.datetime.strptime("2017-06-12T09:51:21Z", "%Y-%m-%dT%H:%M:%SZ"), float(17.21), int(80000)]]
        time_given = [datetime.datetime.strptime("2017-05-19T05:49:34Z", "%Y-%m-%dT%H:%M:%SZ")]
        self.assertEqual(calculate_stats_for_one_time(trade_info, time_given), 23.09)

    def test_calculate_stats_for_two_times(self):
        trade_info = [[datetime.datetime.strptime("2017-03-01T13:37:59Z", "%Y-%m-%dT%H:%M:%SZ"), float(21.37), int(100)],
                      [datetime.datetime.strptime("2017-04-25T17:11:55Z", "%Y-%m-%dT%H:%M:%SZ"), float(20.18), int(55)],
                      [datetime.datetime.strptime("2017-05-19T05:49:34Z", "%Y-%m-%dT%H:%M:%SZ"), float(23.09), int(21)],
                      [datetime.datetime.strptime("2017-06-12T09:51:21Z", "%Y-%m-%dT%H:%M:%SZ"), float(17.21), int(80000)]]
        times_given = [datetime.datetime.strptime("2017-03-01T13:37:59Z", "%Y-%m-%dT%H:%M:%SZ"),
                       datetime.datetime.strptime("2017-05-19T05:49:34Z", "%Y-%m-%dT%H:%M:%SZ")]

#       Good lord, this is why I shouldn't put print statements in calculation methods...
        self.assertEqual(calculate_stats_for_two_times(trade_info, times_given)[0], 23.09)
        self.assertEqual(calculate_stats_for_two_times(trade_info, times_given)[1], 20.18)
        self.assertAlmostEqual(calculate_stats_for_two_times(trade_info, times_given)[2], 21.5467, places=2)
        self.assertAlmostEqual(calculate_stats_for_two_times(trade_info, times_given)[3], 1.46302, places=2)
        self.assertEqual(calculate_stats_for_two_times(trade_info, times_given)[4], 21.37)


if __name__ == '__main__':
    unittest.main()
