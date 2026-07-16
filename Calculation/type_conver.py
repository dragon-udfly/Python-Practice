# Type Conversion with float(), bool(), str(), int()


number_string = "50"
number_int = int(number_string)

print(f"Number in String {number_string}")
print(f"Number in Integer {number_int}")

number_float = float(number_int)
float_number_int = int(number_float)

print(f"Integer Number in Float {number_float}")
print(f"Float Number in Integer {float_number_int}")

number_bool = bool(number_int)
bool_number_int = int(number_bool)

print(f"Integer Number in Bool {number_bool}")
print(f"Bool number in Integer {bool_number_int}")