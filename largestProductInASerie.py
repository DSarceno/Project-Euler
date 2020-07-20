# @Author: Diego Sarceno
# 19.07.2020

# Problem 8 of Project Euler

'''
Tomamos el numero propuesto y vamos tomando paquetes de 13 y multiplicamos
cada uno de los digitos de los paquetes.
'''
# tomamos el numero dado en el problema
n = 73167176531330624919225119674426574742355349194934969835203127745063262395783180169848018694788518438586156078911294949545950137958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362228934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

package = 13

# se divide el 'n' en intervalos de 13
mayor = 0
for i in range(1000 - 13 + 1):
    x = str(n)[i:i + package]
    prod = 1
    for j in range(package):
        prod *= eval(x[j])
        if prod >= mayor:
            mayor = prod

print(mayor)
