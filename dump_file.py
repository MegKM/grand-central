
def add_size_price(self):
    total_price = self.price
    for size_option in self.size_option.all():
        if size_option.price > 0:
            total_price += size_option.price
            return total_price
        else:
            return total_price

SIDES_OPTIONS = (
    ('CO', 'Chips only'),
    ('SO', 'Salad only'),
    ('VO', 'Vegtables only'),
    ('CS', 'Chips & Salad'),
    ('CV', 'Chips & Vegetables'),
    ('SR', 'Steamed Rice'),
    ('BB', 'Baked Beans'),
    ('SP', 'Spaghetti')
)

ADDED_OPTIONS = (
    ('AC', 'Add chicken'),
    ('AB', 'Add bacon'),
    ('AA', 'Add chips'),
    ('CS', 'Add chips and salad'),
    ('CV', 'Add chips and vegtables'),
)
SIZE_OPTIONS = (
    ('SM', 'Small'),
    ('LG', 'Large'),
    ('HA', 'Half'),
    ('FU', 'Full')
)
GRAVY_OPTIONS = (
    ('PG', 'Pepper Gravy'),
    ('MG', 'Mushroom Gravy'),
    ('GR', 'Gravy')
)
COOK_OPTIONS = (
    ('PE', 'Poached Eggs'),
    ('FE', 'Fried Eggs'),
    ('SE', 'Scrambled Eggs'),
    ('GF', 'Grilled Fish'),
    ('FF', 'Fried Fish')
)
SAUCE_OPTIONS = (
    ('SC', 'Sweet chilli'),
    ('SM', 'Spicy Mayo'),
    ('DM', 'Dijon Mustard'),
    ('TS', 'Tomato Sauce')
)
REMOVABLE_OPTIONS = (
    ('EG', 'Egg'),
    ('BE', 'Beetroot'),
    ('ON', 'Onion'),
    ('LE', 'Lettuce'),
    ('CO', 'Coleslaw'),
)