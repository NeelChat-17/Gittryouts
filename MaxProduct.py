class SubarrayNaive:
    def maximum_product(self, arr, max_pro):
        # I will am using recursion to solve this
        p = 1
        while arr:
            i = 0
            if arr[i]==0:
                arr.remove(arr[i])
                return self.maximum_product(arr, max_pro)
            p = p*arr[i]
            arr.remove(arr[i])
            i += 1
            max_pro = max(p, max_pro)
        
        return max_pro

if __name__ == "__main__":
    sn = SubarrayNaive()
    arr = [2, 3, -2, 4]
    max_pro = arr[0]
    result = sn.maximum_product(arr, max_pro)
    print(result)
        
     
