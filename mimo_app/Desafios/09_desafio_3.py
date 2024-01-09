# MIMO - 09 - Tuplas, dicionários e conjuntos - Desafio 3

# Os campistas precisam saber quais equipamentos de acampamento são recomendados para uma viagem!

# Verifique se há uma chave no dicionário para equipamentos de cozinha de acampamento.

# Salve o valor em uma variável kitchen_items .

recommended_camp_gear = {
 "clothes": ("Rain jacket", "Hiking boots"),
 "camp_kitchen": ("Portable stove", "Frying pan") 
}
kitchen_items = "camp_kitchen" in recommended_camp_gear
print(kitchen_items)