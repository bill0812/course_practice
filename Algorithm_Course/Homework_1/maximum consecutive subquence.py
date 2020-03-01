# use algorithm that teacher mentioned in class.
# use suffix max and global max to record current max sum
def findmax(each_pillar):
    global_max = 0
    suffix_max = 0
    for i in range(len(each_pillar)) :
        if suffix_max + each_pillar[i] > global_max : 
            suffix_max = suffix_max + each_pillar[i]
            global_max = suffix_max
        elif suffix_max + each_pillar[i] > 0 :
            suffix_max = suffix_max + each_pillar[i]
        else :
            suffix_max = 0

    return global_max 

if __name__ == "__main__":

    input_data = input("input numbers : ")
    each_pillar = list(map(int, input_data.split()))
    sum_array , original_max = 0 , 0
    
    # find one-way maximum first
    original_max = findmax(each_pillar)

    # change original mind which is about non circular
    # Cuz its a kind of loop , so make it to an negative one
    # then we know the sum of all inputs
    # then we convert the original inputs to negative one
    # compute max sequence . Finally , we have to add it back to the sum.
    # which means that, if we map the negative input's max sequence to original one, the numbers
    # cause the original input's sum smaller. (minimize the original input)
    # so we have to add it back.
    for i in range(0,len(each_pillar)): 
        sum_array += each_pillar[i] 
        each_pillar[i] = -each_pillar[i]

    # compare two maximum sum ( one-way and circlular )
    if sum_array + findmax(each_pillar) > original_max :
        print(sum_array + findmax(each_pillar))
    else :
        print(original_max)

    