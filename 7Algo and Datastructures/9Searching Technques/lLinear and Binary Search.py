a = list(map(int,input('Enter any number of elements\n').split()))

key = int(input('enter key to search'))
'''
#1)Search by index() build in method which have linear time complexity like linear search
#when you try to search key which is not in list then produces 'ValueError: 2 is not in list'
#to handle error, use exception handling
try:
    print('key is found at position ',a.index(key)+1)
except Exception as e:
    print('key not found')
'''

#2)to reduce time complexity use binary search technique only if given data is in sorted manner
def binarySearch(a,key,low,high):
    if(low<=high):
        mid = (low+high)//2
        if(a[mid]==key):
            print('key is found at position ',mid+1)
            return
        elif(key<a[mid]):
            binarySearch(a,key,low,mid-1)
        elif(key>a[mid]):
            binarySearch(a,key,mid+1,high)
    else:
            print('key not found')
            
            
binarySearch(sorted(a),key,0,len(a)-1)
 



