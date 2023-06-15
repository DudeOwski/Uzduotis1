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



