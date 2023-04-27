import sys

# Take file string from input
inFile = sys.argv[1]
rmv = -1
# If rmv router exist
if len(sys.argv) > 2:
    rmv = int(sys.argv[2])
    
# Read file and preprocessing
Testcase = open(inFile, 'r')
TestcaseContents = Testcase.readlines()
Testcase.close()
N = int(TestcaseContents[0].strip())
TestcaseContents.pop(0)
top_matrix = []
for i in TestcaseContents:
    top_matrix.append(i.split())
top_matrix = [list( map(int, i) ) for i in top_matrix]

# If rmv router set router top_matrix to -1
if rmv != -1:
    for i in range(N):
        top_matrix[rmv - 1][i] = -1
    for i in range(N):
        top_matrix[i][rmv - 1] = -1

# Init final distance and next node Matrix
dist_mat = []
nextHop_mat = []

# Run through all nodes
for src in range(N):
    # Init temp arrays
    dist = [sys.maxsize] * N
    dist[src] = 0
    nextHop = []
    for i in range(N):
        if top_matrix[src][i] == -1:
            nextHop.append(-1)
        else:
            nextHop.append(i)
      
    done = [False] * N

    # Loop to update all minimum distance
    for i in range(N):
        # Find min distance node
        min_num = sys.maxsize
        for u in range(N):
            if dist[u] < min_num and done[u] == False:
                min_num = dist[u]
                min_index = u

        # Set the minimum distance vertex done
        done[min_index] = True

        # Update dist value of the adjacent vertices
        for j in range(N):
            if top_matrix[min_index][j] > 0 and done[j] == False:
                if dist[j] > dist[min_index] + top_matrix[min_index][j]:
                    dist[j] = dist[min_index] + top_matrix[min_index][j]
                    if min_index != src:
                        nextHop[j] = nextHop[min_index]
                        
    # add one for correct index
    nextHop = [x+1 for x in nextHop]
    # Save the final result to the matrix
    dist_mat.append(dist)
    nextHop_mat.append(nextHop)

if rmv != -1:
    for i in range(N):
        for j in range(N):
            if nextHop_mat[i][j] == 0:
                nextHop_mat[i][j] = -1
                
    for i in range(N):
        for j in range(N):
            if dist_mat[i][j] == sys.maxsize:
                dist_mat[i][j] = -1

# Write to file
if rmv == -1:
    # If no remove router
    outFile = inFile.split(".")[0] + "_GenTable.txt"
    Testcase = open(outFile, 'w')
    for i in range(N):
        Testcase.write("Routing table of router " + str(i + 1) + ":" + "\n")
        for j in range(N):
            Testcase.write(str(dist_mat[i][j]) + " " + str(nextHop_mat[i][j]) + "\n")
    Testcase.close()
else:
    # If there is remove router
    outFile = inFile.split(".")[0] + "_RmRouter" + str(rmv) +".txt"
    Testcase = open(outFile, 'w')
    for i in range(N):
        if i != (rmv - 1):
            Testcase.write("Routing table of router " + str(i + 1) + ":" + "\n")
            for j in range(N):
                Testcase.write(str(dist_mat[i][j]) + " " + str(nextHop_mat[i][j]) + "\n")
    Testcase.close()