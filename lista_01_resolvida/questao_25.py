horas = float(input("Horas de estudo planejadas: "))
if horas < 10:
    print("Quantidade muito baixa.")
elif horas > 40:
    print("Quantidade muito alta.")
else:
    print(f"Plano configurado com {horas:g} horas.")
