bill_money = int(input("Nhập số tiền hóa đơn ban đầu: "))

if bill_money >= 500000:
    bill_discount = bill_money * 0.1
else:
    bill_discount = 0
    
amount_payable = bill_money - bill_discount

print("\n === HÓA ĐƠN THAMH TOÁN RIKKEI STORE ===")
print(f"Số tiền được giảm giá là: {bill_discount} VND")
print(f"Tổng số tiền khách phải trả là: {amount_payable} VND")