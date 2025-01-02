def print_products(products):
    for product in products:
        print(f" Hete aqui: {product}")
    if not products:
        print ("No hay productos disponibles")
        
        
        
def print_product_sorted_price (products):
     
    product_sorted_by_price= sorted(products, key= su_precio, reverse=True)
    for product in  product_sorted_by_price:
        print (product)
                    
                    
                    
def print_product_by_title(products):
    title = input ("introduce titulo de producto")
    for product in products:
        if title.lower() == product.title.lower():
            print (product)
            return
        
def create_products (products):
    title= input ("Introduce el titulo del producto")
    price= float(input("Introduce precio de producto"))
    quantity= int(input("introduce cantidad de nuevo porducto"))
    new_product= Product(title, price)
    products.append (new_product)
    print (new_product)
    
    

def update_products (products):
    title= input("Introduce producto a actualizar")
    nuevo_titulo= input("Introduce el nuevo título")
    nuevo_precio= float(input("Introduce el nuevo precio"))
    actualizado= False
    for product in products:
        if title.lower() == product.title.lower():
            product.title= nuevo_titulo
            product.price= nuevo_precio
            actualizado= True
            break
        if actualizado:
            print(product)
            print ("Producto actualizado")
        else:
            print ("Inténtelo más tarde, por favor")
            
            
def delete_by_title (products):
    title= input("Introduce titulo del producto a borrar")
            #actualizado= False
            #for product in products:
                #if title.lower() == product.title.lower():
                    #products.remove(product)
                    #actualizado= True
                    #break
            #if actualizado:
                #print ("Producto borrado")
            #else:
                #print ("No has borrado. Torpe")
            #DEL
    for i in enumerate (products):
        if title.lower()== product.title.lower():
            del products [i]
            print ("Producto eliminado correctamente")
            
def delete_products (products):
    products.clear()
    print ("Productos borrados correctamente")
    
    
product1= Product ("lupa", 10)
product2= Product ("micro", 200)
product3= Product ("bafle", 500)
product4= Product ("flautin", 1100)