def trukstami_skaiciai(nums):
    n = len(nums)
    trukstami = []
    
    # Pažymime, kurie skaičiai yra pasikartojantys
    for i in range(n):
        indeksas = abs(nums[i]) - 1
        if nums[indeksas] > 0:
            nums[indeksas] *= -1
    
    # Ieškome skaičių, kurie nėra pažymėti
    for i in range(n):
        if nums[i] > 0:
            trukstami.append(i + 1)
    
    return trukstami

# Pavyzdžio scenarijus 1
nums = [4, 3, 2, 7, 8, 2, 3, 1]
rezultatas = trukstami_skaiciai(nums)
print(rezultatas)  # Rezultatas: [5, 6]

# Pavyzdžio scenarijus 2
nums = [1, 1]
rezultatas = trukstami_skaiciai(nums)


