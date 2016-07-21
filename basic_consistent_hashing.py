
#Method 1
def consistentHashing(self, n):
    # Write your code here
    '''
    if the maximal interval is [x,y] and it belongs to machine id z,
    when you add a new machine with id n, you should divide [x,y,z]
    into 2 intervals:
    [x, (x+y)/2,z]
    [(x+y)/2+1, y, n]
    
    '''
    #base case
    if n == 1:
        return [[0,359,1]]
    if n == 2:
        return [[0,179,1],[180,359,2]]
    
    res = [[0,179,1],[180,359,2]]
    count = 1
    for i in xrange(3,n+1):
        index = 0
        #find max range
        for j in xrange(1,len(res)):
            if res[j][1] - res[j][0] + 1 > \
               res[index][1] - res[index][0] + 1:
                index = j
        x,y,machine = res[index]
        new_y = (x+y)/2
        res[index][1] = new_y
        res.append([new_y+1,y,i])
    
    return res
            
            
#Method 2
#priority queue/heap: but the order couldn't be maintained
import heapq
def consistentHashing(self, n):
    # Write your code here
    '''
    if the maximal interval is [x,y] and it belongs to machine id z,
    when you add a new machine with id n, you should divide [x,y,z]
    into 2 intervals:
    [x, (x+y)/2,z]
    [(x+y)/2+1, y, n]
    
    '''
    #base case
    if n == 1:
        return [[0,359,1]]
    if n == 2:
        return [[0,179,1],[180,359,2]]
    
    res = [[0,179,1],[180,359,2]]
    heap = []
    heapq.heappush(heap,(-180,0))
    heapq.heappush(heap,(-180,1))
    count = 1
    for i in xrange(3,n+1):
        range_,index=heapq.heappop(heap)
        '''
        for j in xrange(1,len(res)):
            if res[j][1] - res[j][0] + 1 > \
               res[index][1] - res[index][0] + 1:
                index = j
        '''
        x,y,machine = res[index]
        new_y = (x+y)/2
        res[index][1] = new_y
        res.append([new_y+1,y,i])
        heapq.heappush(heap,(range_/2,len(res)-1))
        heapq.heappush(heap,(range_/2,index))
        
    return res
