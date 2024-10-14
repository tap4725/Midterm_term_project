import itertools
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


class apriori:
    def __init__(self, series):
        self.series = series

    def calculate_support(self, items):
        transactions = self.series
        counts = np.array([0]*len(self.series))
        for item in items:
            counts += transactions.str.count(item)
        return (np.where(counts >= len(items), 1, 0).sum()/len(transactions))*100

    def get_unique_items(self, transactions=None):
        if not transactions:
            transactions = self.series
        wasd = np.array([])
        for transaction in transactions:
            wasd = np.append(wasd, transaction.replace(" ", "").split(","))
        return set(wasd)

    def generate_item_sets(self, items, k=0):
        return list(itertools.combinations(items, r=k))

    def get_freq_items(self, min_support, items=None):
        if not items:
            items = self.get_unique_items()
        count = 1
        freq_items = []
        while True:
            temp = []
            for i in self.generate_item_sets(items, count):
                wasd = self.calculate_support(i)
                if wasd >= min_support:
                    print(f"Support for item-set{i}: {wasd}")
                    temp.append(i)
            if len(temp) > 0:
                freq_items += temp
                count += 1
            else:
                break
        return freq_items

    def get_associations(self, freq_items, min_conf):
        temp = []
        for _ in freq_items:
            if len(_) == 1:
                continue
            for items in itertools.permutations(_):
                try:
                    conf = (self.calculate_support(items) /
                            self.calculate_support(items[:-1]))*100
                except:
                    continue
                if conf >= min_conf and conf <= 100:
                    temp.append([items, conf])
        print("Association found")
        for items, conf in temp:
            print(f"{items[:-1]} -> {items[-1]}: {conf}")


if __name__ == "__main__":
    print("Welcome to tap47 codebase!\n This is cli for apiori algorith.")
    while True:
        print("Please select one transactional dataset. Each dataset has sample of 20 transactions.")
        selection = int(input(
            " 1. Amazon\n 2. Walmart \n 3. Costco \n 4. Instamart \n 5. Shoprite\n").strip())
        if selection in range(1, 6):
            df = pd.read_csv(
                f"data/supermarket_transactions_frequent_db_{selection}.csv")
            print("The dataset:")
            print(df["Items"])
            min_sup = int(
                input("Please enter minimum support: (range: [0-100]): ".strip()))

            ap = apriori(df["Items"])
            freq_items = ap.get_freq_items(min_sup)

            min_conf = int(
                input("Please enter minimum confidence: (range: [1-100]): ".strip()))
            ap.get_associations(freq_items, min_conf)

            if input("Do you want to use algorith again? (press any key / n): ").lower() == "n":
                break

        else:
            print("Invalid selection!")
