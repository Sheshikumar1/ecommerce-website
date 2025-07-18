class Cart():
    def __init__(self,request):
        self.session=request.session

        # get the cart from the session if it exists

        cart=self.session.get('session_key')

        #if the cart does not exist, create a cart

        if 'session_key' not in request.session:
            cart=self.session['session_key']={}

        # make sure the cart avaiable all of the pages of the site

        self.cart=cart
    
    def add(self,product):
        product_id=str(product.id)

        #logic
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]={'price':str(product.price)}

        self.session.modified=True

    def __len__(self):
        return len(self.cart)