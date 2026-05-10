def twist_sequence(arr: list[int], k: int) -> list[int]:
    
    if len(arr):

        k = k % len(arr)

        l, r = 0, len(arr) - 1

        # Reverse in Place    
        while l < r:
            # Swap In O(1)
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1
        # Reverse just a part
        l, r = 0, k - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r -  1
        
        # Reverse from K to last

        l, r = k, len(arr) - 1
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l, r = l + 1, r - 1
    
    return arr

print(twist_sequence([1,2], 101))

     