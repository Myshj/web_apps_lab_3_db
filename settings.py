from domains import products, categories


DOMAIN = {
    'products': products,
    'categories': categories
}

MONGO_HOST = '192.168.99.100'
MONGO_PORT = 32769

# Skip these if your db has no auth. But it really should.
MONGO_USERNAME = ''
MONGO_PASSWORD = ''

MONGO_DBNAME = 'products'