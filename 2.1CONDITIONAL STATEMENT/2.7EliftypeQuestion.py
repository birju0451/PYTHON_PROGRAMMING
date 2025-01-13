cost_price=int(input("enter cp:"))
selling_price=int(input("enter sp:"))
if selling_price>cost_price:
    print("sellor has made profite")
    print("total profite:",selling_price-cost_price)
elif selling_price<cost_price:
    print("sellor has incorred of loss")
    print("total loss:",cost_price-selling_price)

else:
    print("sellor has no profit and no loss")