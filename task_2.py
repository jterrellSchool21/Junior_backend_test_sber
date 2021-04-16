from datetime import datetime, timedelta
import pandas as pd
import utils

def str_to_time(dates):
    result = []
    for i in dates:
        if not isinstance(i, float):
            result.append(datetime.strptime(i, '%d.%m.%Y'))
    return result

@utils.time_for_function
def to_tab(table, MonthNumber=None):
    data = pd.read_csv(table, sep=';')
    months = [[] for i in range(12)]
    dates = str_to_time(data["Дата"].tolist())
    for i in range(len(dates)):
        part = float(data["Сумма"][i].replace(",", ".")) / 5
        for j in range(6, -1, -1):
            if (dates[i] - timedelta(days=j)).isoweekday() < 6:
                months[(dates[i] - timedelta(days=j)).month - 1].append(part)
    if isinstance(MonthNumber, int):
        print(f"{MonthNumber} : {sum(months[MonthNumber - 1]):.2f}")
    else:
        for i in range():
            print(f"{i + 1} : {sum(months[i - 1]):.2f}")

if __name__ == "__main__":
    # for i in range(12):
    #     to_tab("task_2.csv", i + 1)
    to_tab("task_2.csv", 2)