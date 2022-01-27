
def plus_one(num):
    ans = num + 1
    return ans

def int_changer(chump):
    print("chump: ", chump)
    chump = -1000
    print("chump: ", chump)

def list_changer(lump):
    print("type(lump): ", type(lump))
    lump[0] = -1000
    lump = [7,7,7]

def main():
    #num = 5
    #next_num = plus_one(num)
    #print(next_num)
    #print("num: ", num)
    #int_changer(num)
    #print("num: ", num)

    nums = [5,10,15]
    nums2 = nums
    print(nums2)
    list_changer(nums2)
    print(nums)


#only global function call
main()
