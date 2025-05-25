from collections import namedtuple,defaultdict
from csv import reader
from pprint import pprint




def main():
    #add code here
    res = defaultdict(int) # returns zero if key do not exsists
    with open("data/OrderItems.csv","r") as open_csv:
        read = reader(open_csv)
        Item=namedtuple("Item",next(read))

        for line in read:
            item = Item(*line)
            res[item.ProductID]+=int(item.Quantity)
    print(dict(res))

    

    return

if __name__ == "__main__":
    main()