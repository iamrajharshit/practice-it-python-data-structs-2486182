from collections import deque
def main():
    foods = deque(maxlen=5)
    foods.append("STA001")

    ordered_foods=["DES003","STA002","ENT004","ENT001"]
    foods.extend(ordered_foods)
    foods.append("DES00X")

    foods.appendleft("DES005")
    print(foods)
    #add code here

    return

if __name__ == "__main__":
    main()