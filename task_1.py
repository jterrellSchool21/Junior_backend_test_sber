import pandas as pd
from datetime import datetime, timedelta
import utils

def str_to_time(dates):
    result = []
    for i in dates:
        result.append(datetime.strptime(i, '%d.%m.%Y'))
    return result

@utils.time_for_function
def non_payed(table):
    data = pd.read_csv(table, sep=';')
    deals = dict()
    for i in data["Deal"]:
        if i not in deals.keys():
            tmp = sum(data.loc[data["Deal"] == i]["Sum"])
            if tmp > 0:
                dates = str_to_time(data.loc[data["Deal"] == i]["Date"].tolist())
            min_date = min(dates)
            deals.update({i: [tmp, min_date.strftime("%d.%m.%Y"), (datetime.now() - 
                            min_date).days]})
    print(deals)

if __name__ == "__main__":
    non_payed("task_1.csv")