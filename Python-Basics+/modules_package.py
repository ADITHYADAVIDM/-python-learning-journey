import ecommerce.shipping # importing from packages
ecommerce.shipping.calc_shipping() # calling a func from a package !tedius
from ecommerce.shipping import calc_shipping # now func can be used without prefix
import converter # import a whole module
from converter import lbs_to_kg # import a specific function from a module
import utils

# in line 3 if more functions are to be imported then do...from x import y, z...etc
# or from x(package) import y(module)...then call y.fun() each time wroks both ways
print(lbs_to_kg(70))
print(converter.kg_to_lbs(70))
list = [1, 2, 3, 6, 9, 5]
print(utils.find_max(list))
calc_shipping()