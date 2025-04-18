from . cart import Cart
# create a context processor that will add the cart to the context of all templates

def cart(request):
    #return the default data from our cart
    return {'cart':Cart(request)}
