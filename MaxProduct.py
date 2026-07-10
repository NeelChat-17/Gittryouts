class SubarrayNaive:
    def maximum_product(self, arr, max_pro):
        # I am using recursion to solve this
        p = 1
        while arr:
            if arr[0]==0:
                arr.remove(arr[0])
                return self.maximum_product(arr, max_pro)
            p = p*arr[0]
            arr.remove(arr[0])
            max_pro = max(p, max_pro)
        
        return max_pro

if __name__ == "__main__":
    sn = SubarrayNaive()
    arr = [2, 3, -2, 4]
    max_pro = arr[0]
    result = sn.maximum_product(arr, max_pro)
    print(result)