
class PlusOneTest:
    def plusOne(self,digits):
        #run through the array, as I run through the array I want to individually add 
        #one to the element 
        #in the current interation at the index and run a if statement if it is a nine
        for i in range(len(digits)):
            if i == 9:
                digits[i] = 0
                digits.insert(i,1)
            digits[i] = digits[i] + 1
        return digits
digits = [9]
print(PlusOneTest().plusOne(digits))

        