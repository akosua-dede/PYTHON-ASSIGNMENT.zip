# Trotro fare calculator

route = input("enter your preferred route (Accra-Medina / Accra-Tema / Accra- Kasoa): ")
passengers = int(input('enter number of passengers'))

# Find fare based on your rout
if route == "Accra-Medina":
   fare = 5
elif route == "Accra-Kasoa":
      fare = 10
elif route == "Accra-Tema":
     fare = 8
else :
    print("invalid route enterd")

# calculate total fare
total_fare = fare * passengers

#Display fare
print("Your fare is:GHS",total_fare)





