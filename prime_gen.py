import math
import time


class Prime():
    def _get_generator(self):
        D = {}
        q = 2
        
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]
            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]
            
            q += 1

    def at(self, n: int) -> int:
        count = 0
        for i in self._get_generator():
            if count >= n:
                return i
            count += 1

    def check(self, n: int) -> int:
        if n % 2 == 0 and n > 2: 
            return False
        return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
    
    def performance(self, start, stop):
        increases = []
        
        x = time.time()
        for i in range(start, stop+1):
            # print(i)
            _ = []

            now = time.time()
            Prime().at(i)
            _.append(time.time() - now)

            now = time.time()
            Prime().at(i+1)
            _.append(time.time() - now)

            increases.append(sum(_)/len(_))
            
        took = time.time() - x

        mean = sum(increases)/len(increases)
        first = increases[0]
        median = increases[len(increases)//2]
        last = increases[-1]

        print(f"start {start}, stop {stop}")
        print("time took :", took)
        print("datas     :", len(increases))
        print("incremental average     :  {0:.72f}".format(mean))
        print("incremental first       :  {0:.72f}".format(first))
        print("incremental median      :  {0:.72f}".format(median))
        print("incremental last        :  {0:.72f}".format(last))

        print()
        the_data_y_avg = took/mean
        the_data_y_fst = took/first
        the_data_y_mdn = took/median
        the_data_y_lst = took/last
        print("theoretical yield data avg  : {0:.4f} data".format(the_data_y_avg))
        print("theoretical yield data fst  : {0:.4f} data".format(the_data_y_fst))
        print("theoretical yield data mdn  : {0:.4f} data".format(the_data_y_mdn))
        print("theoretical yield data last : {0:.4f} data".format(the_data_y_lst))
        print("      final yield data avg  : {0:.4f} %".format(len(increases) / the_data_y_avg * 100))
        print("      final yield data fst  : {0:.4f} %".format(len(increases) / the_data_y_fst * 100))
        print("      final yield data mdn  : {0:.4f} %".format(len(increases) / the_data_y_mdn * 100))
        print("      final yield data lst  : {0:.4f} %".format(len(increases) / the_data_y_lst * 100))

        print()
        the_time_mean_yield = mean * len(increases)
        the_time_first_yield = first * len(increases)
        the_time_median_yield = median * len(increases)
        the_time_last_yield = last * len(increases)
        print("theoretical time yield avg  : {0:.4f} second".format(the_time_mean_yield))
        print("theoretical time yield fst  : {0:.4f} second".format(the_time_first_yield))
        print("theoretical time yield mdn  : {0:.4f} second".format(the_time_median_yield))
        print("theoretical time yield lst  : {0:.4f} second".format(the_time_last_yield))
        print("      final time yield avg  : {0:.4f} %".format(took / the_time_mean_yield * 100))
        print("      final time yield fst  : {0:.4f} %".format(took / the_time_first_yield * 100))
        print("      final time yield mdn  : {0:.4f} %".format(took / the_time_median_yield * 100))
        print("      final time yield lst  : {0:.4f} %".format(took / the_time_last_yield * 100))