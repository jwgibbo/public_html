#scopedemo.py

def num_changer(num):
    print(f"num_changer's num =", num)
    num = -1
    print(f"num_changer's num =", num)

def main():
    num = 5
    print(f"main's num =", num)
    num_changer(num)
    print(f"main's num =", num)

main()
