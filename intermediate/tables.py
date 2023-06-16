from prettytable import PrettyTable

table = PrettyTable()
field = ["Pokemons", "Type"]
rows = [["Pikachu", "Electric"], [
    "Charezar", "Fire"], ["Sqauddle", "Water"]]
table.field_names = field
table.add_rows(rows)
print(table)
