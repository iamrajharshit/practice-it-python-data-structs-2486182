from collections import Counter

def main():
    #Add code here
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    #sell 5 starters, 3 salads, and 3 entrees
    sales = Counter(STA001=5, SAL002=3, ENT004=3)
    #make 9 more starters and 1 more entree
    inventory=inventory-sales
    shipment_in={"STA001":9,"ENT004":1}
    inventory+= shipment_in
    print(inventory)

if __name__ == "__main__":
    main()