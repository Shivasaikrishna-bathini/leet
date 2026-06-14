class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        ptr = 0
        
        for num in range(1, n + 1):
            if ptr == len(target):
                break
            
            operations.append("Push")
            
            if num != target[ptr]:
                operations.append("Pop")
            else:
                ptr += 1
        
        return operations