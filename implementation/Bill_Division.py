def bonAppetit(bill, k, b):
    ac_bill = (sum(bill) - bill[k])//2
    if b-ac_bill==0:
        return "Bon Appetit"
    else:
        return b-ac_bill
    

k = 1
bill = [3,10,2,9]
# b = 12
b= 7
print(bonAppetit(bill, k, b))