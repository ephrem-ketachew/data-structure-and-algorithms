class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.products = [1]
        self.last_zero_index = -1 

    def add(self, num: int) -> None:
        self.nums.append(num)
        if num == 0:
            self.last_zero_index = len(self.nums) - 1
            self.products.append(1)
        else:
            self.products.append(self.products[len(self.products) - 1] * num)
        
    def getProduct(self, k: int) -> int:
        # product = 1
        # for i in range(len(self.nums) - 1, len(self.nums) - k - 1, -1):
        #     product *= self.nums[i]
        # return product
        l = len(self.products)
        return self.products[l - 1] // self.products[l - 1 - k] if l - 1 - k > self.last_zero_index else 0
    
    
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)