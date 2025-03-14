from product import Product
from customer import Customer
from cart import Cart
from order import Order

def main():

    products = [
        Product("Laptop",15000,5),
        Product("Telefon",10000,10),
        Product("Kulaklık",500,20)
    ]

    name = input("Müşteri Adınızı Girin: ")
    email = input("E-posta adresinizi girin: ")
    customer = Customer(name,email)

    cart = Cart()

    while True:
        print("\nÜrünler:")
        for i, product in enumerate(products):
            print(f"{i+1}. {product}")

        print("\nYapmak istediğiniz işlemi seçiniz:")
        print("1. Ürün ekle")
        print("2. Ürün çıkar")
        print("3. Sepeti görüntüle")
        print("4. Siparişi tamamla")
        print("5. Çıkış")

        choice = input("Seçiminizi Yapın: ")

        if choice == "1":
            product_index = int(input("Hangi ürünü eklemek istiyorsunuz? (Numara): ")) - 1
            if 0 <= product_index < len(products):
                quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                cart.add_product(products[product_index],quantity)

        elif choice == "2":
                print("\nSepetteki Ürünler:")
                cart.display_cart()
                try:
                    product_index = int(input("Hangi ürünü çıkarmak istiyorsunuz? (Numara): ")) - 1
                    product_name = list(cart.items.keys())[product_index] 
                    cart.remove_product(product_name)
                    print(f"{product_name} ürünü sepetten çıkarıldı.")
                except ValueError:
                    print("Lütfen geçerli bir ürün numarası girin.")
                except IndexError:
                    print("Sepetteki ürün numarasıyla uyuşmayan bir giriş yaptınız!")

        elif choice == "3":
                print("\nSepetinizdeki Ürünler:")
                cart.display_cart()

        elif choice == "4":
                print("\nSiparişiniz tamamlanıyor...")
                total_amount = cart.get_total()
                print(f"\nToplam Tutar: {total_amount} TL")
                order = Order(customer, cart)
                order.place_order()
                print("Siparişiniz başarıyla tamamlandı!")
                break
        
        elif choice == "5":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()

