distance = int(input("ป้อนระยะทาง(กิโลเมตร) : "))
price = 35

if distance == 1:
    price = 35
    
elif   distance > 1 and distance <= 10:
    x_distance = (distance - 1)
    price += x_distance * 5.50
    distance -= x_distance
elif   distance > 10 and distance <= 20:
    x_distance = (distance - 1)
    price += x_distance * 5.50
    distance -= x_distance
elif   distance > 20 and distance <= 40:
    x_distance = (distance - 1)
    price += x_distance * 7.50
    distance -= x_distance
elif   distance > 40 :
    x_distance = (distance - 1)
    price += x_distance * 9
    distance -= x_distance

print("\nค่าแท็กซี่ทั้งหมด %.0f บาท"% price);   
