import json

class colors:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    ENDC = '\033[0m'

def printc(color, message):
    print('|' + color + message.ljust(15) + colors.ENDC, end='')

class Setting():
    '''Отримання налаштувань з файлу'''
    open_json_file = open('setting.json', 'r')
    read_json_file = json.load(open_json_file)
    
    def get_width_aquarium():
        return Setting.read_json_file['aquarium_w']

    def get_height_aquarium():
        return Setting.read_json_file['aquarium_h']
    
    def get_static_algae():
        return Setting.read_json_file['static_algae']

    def get_predator_fish():
        return Setting.read_json_file['predator_fish']

    def get_prey_fish():
        return Setting.read_json_file['prey_fish']


class CreateFish():
    def create_prey_fish():
        return 'HM129'

    def create_predator_fish():
        return 'PM129'
    
class CreateAquarium():
# Функція створення акваріума
    def create_aquarium():
        w = Setting.get_width_aquarium()
        h = Setting.get_height_aquarium()
        len_aqua = int(w) * int(h)
        aquarium = []
        i = 0
        while i < len_aqua:
            aquarium.append('')
            i += 1 
        return aquarium

class CreateStaticElement():
    def create_algae():
        return 'G'

aqua1 = CreateAquarium.create_aquarium()

# Заповнення водоростями
def set_static_algae_from_aquarium():
    global aqua1
    static_g = Setting.get_static_algae()
    set_com = int(len(aqua1) / int(static_g) - 1)
    a = set_com
    i = 0
    while i < int(static_g):
        aqua1[set_com] = CreateStaticElement.create_algae()
        i += 1
        set_com = set_com + a
    return aqua1
set_static_algae_from_aquarium()

# Заповнення рибками хижаками
def set_predator_fish():
    global aqua1
    static_pf = Setting.get_predator_fish()
    set_com = int(len(aqua1) / int(static_pf) - 1)
    a = set_com
    i = 0
    while i < int(static_pf):
        if aqua1[set_com] == '':
            aqua1[set_com] = CreateFish.create_predator_fish()
            set_com = set_com + a
        else:
            aqua1[set_com + 1] = CreateFish.create_predator_fish()
            set_com = set_com + a
        i += 1

    return aqua1
set_predator_fish()

def set_prey_fish():
    global aqua1
    static_pf = Setting.get_prey_fish()
    set_com = int(len(aqua1) / int(static_pf) - 1)
    a = set_com
    i = 0
    while i < int(static_pf):
        if aqua1[set_com] == '':
            aqua1[set_com] = CreateFish.create_prey_fish()
            set_com = set_com + a
        else:
            aqua1[set_com + 1] = CreateFish.create_prey_fish()
        i += 1
    return aqua1

set_prey_fish()

# Функція віднімання енергії
def update_energy_minus(fish):
    global aqua1
    a = []
    for i in fish:
        a.append(i)
    new_energy = int(a[4]) - 1
    if new_energy > 0:
        a[4] = str(new_energy)
        new_fish = ''.join(a)
        return new_fish
    else:
        energy_low = ''
        return energy_low
    
# Функція додавання енергії
def update_energy_plus(fish):
    global aqua1
    a = []
    new_fish = fish
    for i in fish:
        a.append(i)
    new_energy = int(a[4]) + 3
    if new_energy > 9:
        return new_fish
    else:
        a[4] = str(new_energy)
        new_fish = ''.join(a)
    return new_fish



# Функція оновлення віку рибок, якщо вік більше 9 то рибка помирає
def update_fish_old(fish):
    global aqua1
    a = []
    for i in fish:
        a.append(i)
    new_old = int(a[2]) + 1
    a[2] = str(new_old)
    
    if int(a[2]) <= 3:
        a[3] = '1'
    elif int(a[2]) >= 3 and int(a[2]) <= 6:
        a[3] = '2'
    elif int(a[2]) >= 6 and int(a[2]) <= 9:
        a[3] = '3'
        a[2] = '9'
    else:
        hollow_cell = ''

        return hollow_cell

    new_fish = ''.join(a)

    return(new_fish)

# Функція порівняння рибок
def equ_cell(fish1, fish2):
    global aqua1
    if fish2 == '':
        return True
    # return True

def crt():
    new_aqua = []
    ii = 0
    l_aq = len(aqua1)
    while ii < l_aq:
        new_aqua.append('')
        ii += 1
    return new_aqua
new_aqua = crt()

def go_fish():
    global aqua1
    global new_aqua
    i = 0
    len_arr = len(aqua1)

    #Створив пустий масив на основі акваріума.

    while i < len_arr:
        # Додає вік у рибки
        if aqua1[-i] == '':
            pass

        elif aqua1[-i].startswith('PF') or aqua1[-i].startswith('PM'):
            new_old_fish = update_fish_old(aqua1[-i])
            aqua1[-i] = new_old_fish
            stat_num = -i + 3
            if aqua1[-i] != '':
                if aqua1[stat_num].startswith('HM') or aqua1[stat_num].startswith('HF'):
                    new_energy_plus = update_energy_plus(aqua1[-i])
                    aqua1[-i] = new_energy_plus
                else:
                    new_energy = update_energy_minus(aqua1[-i])
                    aqua1[-i] = new_energy

            new_aqua[stat_num] = aqua1[-i]
            new_aqua[-i] = ''

        elif aqua1[-i].startswith('HM') or aqua1[-i].startswith('HF'):
            new_old_fish2 = update_fish_old(aqua1[-i])
            aqua1[-i] = new_old_fish2
            new_energy = update_energy_minus(aqua1[-i])
            aqua1[-i] = new_energy
            stat_num2 = -i + 2
            if aqua1[stat_num2] == 'G':
                new_energy_plus2 = update_energy_plus(aqua1[-i])
                aqua1[-i] = new_energy_plus2
            elif aqua1[stat_num2].startswith('HM') or aqua1[stat_num2].startswith('HF'):
                stat_num2 += 1 
            new_aqua[stat_num2] = aqua1[-i]
            new_aqua[-i] = ''

        elif aqua1[-i] == 'G':
            
            new_aqua[-i] = 'G'
        i += 1
    aqua1.clear()
    aqua1 = new_aqua.copy()
    return new_aqua




def view_aquarium():
    jk = go_fish()
    len_aqua = len(jk)
    r = 0
    nn = 0
    print("===========================================================================================")
    while r < len_aqua:
        if nn == int(Setting.get_width_aquarium()):
            print('')
            nn = 0
        nn += 1
        if str(jk[r]).startswith('HM'):
            printc(colors.CYAN, str(jk[r]))
        elif str(jk[r]).startswith('PM'):
            printc(colors.GREEN, str(jk[r]))
        else:
            printc(colors.YELLOW, str(jk[r]))

        r += 1
    print('')
    print('============================================================================================')


while True:
    view_aquarium()
    j = input('Enter')
