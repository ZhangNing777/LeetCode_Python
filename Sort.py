class Solution:
    #"冒泡排序"
    def bubbleSort(self,l:[int]) -> list:
        for i in range(0,len(l)):
            for j in range(0,len(l)-i-1):
                if l[j+1] < l[j]:
                    temp = l[j+1]
                    l[j+1] = l[j]
                    l[j] = temp
        return l

    def bubbleSort1(self,l:[int]) -> list:
        for i in range (len(l), 0, -1):
            for j in range(0, i-1):
                if l[j+1] < l[j]:
                    temp = l[j+1]
                    l[j+1] = l[j]
                    l[j] = temp
        return l

    #"选择排序"
    def selectionSort(self,l:[int]) -> list:
        for i in range(0,len(l)):
            index = i
            for j in range(i,len(l)):
                if l[j] < l[index]:
                    index = j
                temp = l[index]
                l[index] = l[i]
                l[i] = temp
        return l

    #"插入排序"
    def insertionSort(self,l:[int]) -> list:
        for i in range(0,len(l)-1):
            current = l[i+1]
            index = i
            while index >= 0 and current < l[index]:
                l[index+1] = l[index]
                index -= 1
            l[index+1] = current
        return l

    #"希尔排序"
    def shellSort(self,l:[int]) -> list:
        gap = len(l) // 2
        while gap > 0:
            for i in range(gap,len(l)):
                temp = l[i]
                index = i - gap
                while index >= 0 and l[index] > temp:
                    l[index + gap] = l[index]
                    index -= gap
                l[index + gap] = temp
            gap //= 2
        return l

    #"归并排序"
    def mergeSort(self,l:[int]) -> list:
        if len(l) < 2:
            return l
        mid = len(l) // 2
        list1 = list.copy(l[0 : mid])
        list2 = list.copy(l[mid : len(l)])

        a = Solution()

        return a.merge(a.mergeSort(list1),a.mergeSort(list2))

    def merge(self,list1:[int],list2:[int]) -> list:
        result = list1 + list2
        i = j = 0
        for index in range(0,len(list1)+len(list2)):                
            if i >= len(list1):
                result[index] = list2[j]
                j += 1
            elif j>= len(list2):
                result[index] = list1[i]
                i += 1
            elif (list1[i] > list2[j]):                
                result[index] = list2[j]  
                j += 1              
            else:
                result[index] = list1[i]
                i += 1
        return result

    
    # "快速排序"
    def quickSort(self,l:[int]) -> list:
        if len(l) >= 2:
            mid = l[len(l)//2]
            left = []
            right = []
            l.remove(mid)
            for i in range(0,len(l)):
                if l[i] <= mid:
                    left.append(l[i])
                else:
                    right.append(l[i])
            return self.quickSort(left) + [mid] + self.quickSort(right)
        else:
            return l
    

    #"堆排序"
    # def heapSort(self,l:[int]) -> list:
        
    #     return l

    def change(self,l:[int]) -> list:
        n = len(l)
        while n > 1:
            if n%2 == 1:
                for i in range(n,1,-2):
                    index = i
                    if l[index-1] < l[i-2]:
                        index = i-1
                    if l[index-1] > l[i//2-1]:
                        a = l[index-1]
                        l[index-1] = l[i//2-1]
                        l[i//2-1] = a    

            if n%2 == 0:
                if l[n-1] > l[n//2-1]:
                    a = l[n-1]
                    l[n-1] = l[n//2-1] 
                    l[n//2-1] = a
                for i in range(n-1,1,-2):
                    index = i
                    if l[index-1] < l[i-2]:
                        index = i-1
                    if l[index-1] > l[i//2-1]:
                        a = l[index-1]
                        l[index-1] = l[i//2-1]
                        l[i//2-1] = a

            a = l[0]
            l[0] = l[n-1]
            l[n-1] = a
            n -= 1

        return l


    
    # 计数排序
    def contingSort(self,l:[int]) -> list:
        lmin = l[0]
        lmax = l[0]
        for i in range(1,len(l)):
            if l[i] > lmax:
                lmax = l[i]
            elif l[i] < lmin:
                lmin = l[i]

        count = [0 for i in range(lmax-lmin+1)]

        for i in range(0,len(l)):
            a = l[i] - lmax
            b = 0
            b+=1
            count[a-1] = b
            a = 0

        x = 0

        for i in range(0,len(count)):
            while count[i] != 0:
                l[x] = i + lmin
                x += 1
                count[i] -= 1
        
        return l

    #"桶排序"
    def bucketSort(self,l:[int]) ->list:
        max = l[0]
        for i in range(0,len(l)):
            if l[i] > max:
                max = l[i]

        a = max//10

        bucket = [[0 for f in range(10)] for g in range(a+1)]

        for i in range(0,len(l)):
            m = l[i]//10
            n = l[i]%10
            bucket[m][n] += 1

        x = 0

        for i in range(0,a+1):
            for j in range(0,9):
                while bucket[i][j] != 0:
                    l[x] = i*10 + j
                    x += 1
                    bucket[i][j] -= 1

        return l

    #"基数排序"
    def radixSort(self,l:[int]) -> list:
        max = l[0]
        for i in range(0,len(l)):
            if l[i] > max:
                max = l[i]
        index = 0
        while max != 0:
            max //= 10
            index += 1
        
        m = 10 
        n = 1

        for i in range(0,index):
            bucket = [[0 for f in range(1)] for g in range(10)]
            for j in range(0,len(l)):
                a = l[j]%m//n
                bucket[a].append(l[j])
            x = 0
            for j in range(0,10):
                for k in range (1,len(bucket[j])):
                    l[x] = bucket[j][k]
                    x += 1
            m *= 10
            n *= 10
            

        return l


        
        
a = Solution()

print(a.change([1,7,6,3,7,4,5,12,13,14]))
