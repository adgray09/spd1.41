class Solution:
         
    def get_sum(self, n):
        sum = 0
        while (n != 0): 
      
            sum = sum + int(n % 10) 
            n = int(n/10) 
      
        return sum
    
    def get_product(self, n):
        product = 1
  
        while (n != 0): 
            product = product * (n % 10) 
            n = n // 10
  
        return product 

    def subtractProductAndSum(self, n: int) -> int:
        whole_product = self.get_product(n)
        whole_sum = self.get_sum(n)
        
        answer = whole_product - whole_sum
        return answer
    
# Variable: whole_sum
# Value: collects the whole sum of the numbers of the number added up 

# Variable: whole_product
# Value: collects the whole product of the numbers of the number multiplied 

# Variable: answer
# Value: returns the whole_product minus the whole_sum to give desired answer 