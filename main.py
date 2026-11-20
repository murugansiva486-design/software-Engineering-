from shop.database import initialize
from shop.products import list_products
from shop.cart import add_to_cart, view_cart, checkout

def main():
    initialize()
    while True:
        print("\n=== ONLINE SHOPPING SYSTEM ===")
        print("1. View Products\n2. Add to Cart\n3. View Cart\n4. Checkout\n5. Exit")
        ch=input("Enter choice: ").strip()
        if ch=="1":
            for p in list_products(): print(f"{p[0]} | {p[1]} | Rs.{p[2]:.2f} | Stock: {p[3]}")
        elif ch=="2":
            try: print(add_to_cart(int(input("Product ID: ")), int(input("Quantity: "))))
            except ValueError: print("Enter valid numbers.")
        elif ch=="3":
            items=view_cart()
            if not items: print("Cart is empty.")
            for x in items: print(f"{x[1]} x {x[2]} = Rs.{x[3]:.2f}")
        elif ch=="4": print(checkout())
        elif ch=="5": print("Thank you for shopping!"); break
        else: print("Invalid choice.")
if __name__=="__main__": main()
