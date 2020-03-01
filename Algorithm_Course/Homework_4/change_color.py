def find_and_count(i, j, first_color, input_data, count) :
    
    # out of bound, do nothing
    if ( i < 0 or i >= height or j < 0 or j >= width ) : 
        return count

    # set current_color as current input index's color to check whether they are connected.
    current_color = input_data[i][j]

    # not same color, do nothing
    if first_color != current_color :
        return count

    # if condition meet
    elif check_matrix[i][j] == 0: 

        # count added
        count += 1 

        # set check status
        check_matrix[i][j] = 1

        # go right and check color
        count = find_and_count(i+1, j, first_color, input_data, count)

        # go left and check color
        count  = find_and_count(i-1, j, first_color, input_data, count) 

        # go down and check color
        count  = find_and_count(i, j+1, first_color, input_data, count)

        # go up and check color
        count  = find_and_count(i, j-1, first_color, input_data, count)
    
    return count 

if __name__ == "__main__":

    global count_list, check_matrix
    
    # input row and column and convert to list
    input_size = list(map(int, input().split()))
    input_data = list()

    # insert each cloumn data[0,1] for each row
    for i in range(input_size[0]) :
        input_data.append((list(map(int, input().split()))[0:input_size[1]]))

    height = len(input_data)
    width = len(input_data[0])

    # create a n*n matrix ,avoiding to go through the same point
    check_matrix = [[0 for i in range(width)] for i in range(height)]
    count_list = list()

    # check each point in data
    for i in range(height) :
        for j in range(width) :
            count = 0
            count_list.append(find_and_count(i,j,input_data[i][j],input_data,count))

    print(max(count_list))   