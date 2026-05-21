class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # Шаг 1: Идем слева направо. 
        # В res[i] записываем произведение всех чисел ДО индекса i.
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Шаг 2: Идем справа налево.
        # Умножаем уже имеющийся в res[i] префикс на суффикс (произведение чисел ПОСЛЕ i).
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res