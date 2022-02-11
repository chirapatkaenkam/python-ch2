price = int(input("รับค่าราคาสินค้า:"))
vat = price*(7/100)
disc = price (5/100)
total = price-disc+vet
print("ภาษีมูลค่าเพิ่ม %.3F % vat,"บาท")
print("ส่วนลด %.3f" % disc,"บาท")
