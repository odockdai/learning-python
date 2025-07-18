name = input("Nama kamu: ")
age = int(input("Usia: "))
temperature = float(input("Suhu tubuh (°C): "))

fahrenheit = temperature * 9/5 + 32
kelvin = temperature + 273.15

if temperature < 35.0:
    kategori = "hipotermia"
elif temperature > 37.5:
    kategori = "demam"
else:
    kategori = "normal"

print(f"Nama         : {name}")
print(f"Usia         : {age} tahun")
print(f"Suhu tubuh   : {temperature:.1f} °C = {fahrenheit:.1f} °F = {kelvin:.1f} K")
print(f"Kategori     : {kategori}")