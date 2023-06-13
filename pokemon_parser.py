def parse_pokemon_data(pokemon_item, id_counter):
    name = pokemon_item.find('h2', class_='woocommerce-loop-product__title').text
    price = pokemon_item.find('span', class_='woocommerce-Price-amount amount').text
    sku = pokemon_item.find('a', class_='add_to_cart_button').get('data-product_sku', '')
    image_url = pokemon_item.find('img', class_='attachment-woocommerce_thumbnail').get('src', '')

    pokemon_data = {
        'id': id_counter,
        'name': name,
        'price': price,
        'sku': sku,
        'imageURL': image_url,
    }

    return pokemon_data
