itemdict = {'Винотовка': ('в',25, 3),
            'Пистолет': ('п',15, 2),
            'Боекомплект': ('б',15, 2),
            'Аптечка': ('а',20, 2),
            'Ингалятор': ('и',5, 1),
            'Нож': ('н',15, 1),
            'Топор': ('т',20, 3),
            'Оберег': ('о',25, 1),
            'Фляжка': ('ф',15, 1),
            'Антидот': ('д',10, 1),
            'Еда': ('к',20, 2),
            'Арбалет': ('р',20, 2)
            }


print('=================================== Первое задание ===================================')
def get_area_value_symbol(itemdict):
    symbol = [itemdict[item][0] for item in itemdict]
    value = [itemdict[item][1] for item in itemdict]
    are = [itemdict[item][2] for item in itemdict]
    return symbol,are,value

def point(itemdict):
    totalPoint = sum([itemdict[item][1] for item in itemdict]) - 10
    return totalPoint

def get_memtable(itemdict, A = 9):
    symbol, area, value = get_area_value_symbol(itemdict)
    n = len(value)

    V = [[0 for a in range(A + 1)] for i in range(n+1)]

    for i in range(n+1):
        for a in range(A+1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif i == 4 and a == 1:
                V[i][a] = 5
            elif area[i-1] <= a:
                V[i][a] = max(value[i-1] + V[i-1][a - area[i - 1]], V[i-1][a])
            else: V[i][a] = V[i-1][a]
    return V, value, area, symbol

def seclect_item(itemdict, A = 9):
    V,value, area, symbol = get_memtable(itemdict)
    n = len(value)
    res = V[n][A]
    itemList = []

    for i in range(n, 0, -1):
        if i == 4:
            itemList.append((symbol[4], value[4], area[4]))
            res -= value[4]
            A -= area[4]
        elif res != V[i-1][A]:
            itemList.append((symbol[i-1], value[i-1], area[i-1]))
            res -= value[i-1]
            A -= area[i-1]
    return itemList

def Result():
    newItem = seclect_item(itemdict)
    line1 = []
    line2 = []
    line3 = []
    SurvivalPoint = 0
    for i in newItem:
        i = list(i)
        if i[1] == 5:
            line1.append(i[0])
            SurvivalPoint += i[1]
        elif len(line1) <= 1 and i[2] == 1:
                line1.append(i[0])
                SurvivalPoint += i[1]
        elif len(line2) <= 2:
            if i[2] == 1 and len(line2) <= 2:
                line2.append(i[0])
                SurvivalPoint += i[1]
            elif i[2] == 2 and len(line2) <= 1:
                line2.append(i[0])
                line2.append(i[0])
                SurvivalPoint += i[1]
        elif len(line3) <= 2:
            if  i[2] == 3:
                line3.append(i[0])
                line3.append(i[0])
                line3.append(i[0])
                SurvivalPoint += i[1]
    print(SurvivalPoint)
    SurvivalPoint = 2*SurvivalPoint - point(itemdict)
    return line1, line2, line3, SurvivalPoint

element = Result()
for i in range(len(element)):
    if i != 3:
        print(element[i])
    else:
        print(f'Итоговые очки выживания: {element[i]}')

print('=================================== первое допзадание ===================================')

def get_new_memtable(itemdict, A=7):
    symbol, area, value = get_area_value_symbol(itemdict)
    n = len(value)

    V = [[0 for a in range(A + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for a in range(A + 1):
            if i == 0 or a == 0:
                V[i][a] = 0
            elif area[i - 1] <= a:
                V[i][a] = max(value[i - 1] + V[i - 1][a - area[i - 1]], V[i - 1][a])
            else:
                V[i][a] = V[i - 1][a]
    return V[n][A]

def result():
    new_total = get_new_memtable(itemdict)
    survival_score = 2 * new_total - int(point(itemdict)) - 10
    if survival_score < 0:
        print('Итоговые очки выживания =' , survival_score)
        print('Нет решения для случая с инвентарём в 7 ячеек, потому что максимальные итоговые очки выживания = -15 (меньше 0)')

result()

print('\n')
print('=================================== второе допзадание ===================================')

def newList(itemdict):
    symbol,area, value  = get_area_value_symbol(itemdict)
    new_item = []

    for i in range(len(value)):
        if value[i] == 20 and area[i] == 2:
            new_item.append((symbol[i], area[i]))
        elif value[i] == 15 and area [i] == 1:
            new_item.append((symbol[i], area[i]))
        elif area[i] == 3:
            new_item.append((symbol[i], area[i]))

    item_List = Result()
    line1 = item_List[0]
    point1 = item_List[3]
    line2 = []
    line3 = item_List[2]
    line2_1 = []
    line3_1 = []

    for i in new_item:
        if len(line2) <= 2 and i[1] == 1:
            if i[0] != 'ф' and i[0] != 'о' and i[0] != 'и' :
                line2.append(i[0])
        elif len(line2) <= 1 and i[1] == 2:
            line2.append(i[0])
            line2.append(i[0])
    for i in new_item:
        if len(line2_1) <= 2 and i[1] == 1:
            if i[0] != 'ф' and i[0] != 'о' and i[0] != 'и' :
                line2_1.append(i[0])
        elif len(line2_1) <= 1 and i[1] == 2 and i[0] != 'а':
            line2_1.append(i[0])
            line2_1.append(i[0])
        elif i[1] == 3 and i[0] == 'в':
            line3_1.append(i[0])
            line3_1.append(i[0])
            line3_1.append(i[0])

    print("Первая комбинация")
    print(f'Итоговые очки выживания = {point1}')
    print(str(line1) + '\n' + str(line2) + '\n' + str(line3))
    print("Вторая комбинация")
    print(f'Итоговые очки выживания = {point1}')
    print(str(line1) + '\n' + str(line2_1) + '\n' + str(line3_1))

newList(itemdict)