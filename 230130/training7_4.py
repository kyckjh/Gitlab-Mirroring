class calc:
    def insurance(time):
        if time % 30 != 0:
            return 30 * (time // 30 + 1)
        else:
            return time
    def distance(distance):
        if distance <= 100:
            return distance
        else:
            return 100 + (distance - 100) // 2
    

def fee(time, distance):
    result = 1200 * (time // 10)
    result += 525 * calc.insurance(time) // 30
    result += 170 * calc.distance(distance)
    return result

print(fee(600, 50)) #=> 91000
print(fee(600, 110)) #=> 100350
