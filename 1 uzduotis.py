def likutis_po_pirkimo(kainos, pinigai):
    min_likutis = pinigai
    results = [likutis_po_pirkimo]
    
    
    for i in range(len(kainos)):
        for j in range(i+1, len(kainos)):
            
            bendra_kaina = kainos[i] + kainos[j]
            likutis = pinigai - bendra_kaina
        
            if likutis >= 0 and likutis < min_likutis:
                min_likutis = likutis

    return results
