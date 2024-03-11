# Project 4 – Graduate Rate (2017-2018)
# Name: Berfredd Quezon
# Instructor: Dr. S. Einakian
# Section: 11
# classes and functionalities will be provided here

# class Division
class Division:

    def __init__(self, id: int, div_name: str):
        self.id = id
        self.division_name = div_name

    def __repr__(self):
        return 'ID: {}, Division: {}'.format(self.id, self.division_name)

    def __eq__(self, other):
        return (self is other or
                type(other) == Division and
                self.id == other.id and
                self.division_name == other.division_name)


# class Graduate
class Graduate:

    def __init__(self, id: int, major: str, bachelor: tuple, master: tuple, doctor: tuple):
        self.id = id
        self.major = major
        self.bachelor = bachelor
        self.master = master
        self.doctor = doctor

    def __repr__(self):
        return ('ID: {}, Major: {}, Bachelor\'s: {}, Master\'s: {}, Doctor\'s: {}'.format
                (self.id, self.major, self. bachelor, self.master, self.doctor))

    def __eq__(self, other):
        return (self is other or
                type(other) == Graduate and
                self.id == other.id and
                self.major == other.major and
                self.bachelor == other.bachelor and
                self.master == other.master and
                self.doctor == other.doctor)

# Design Recipe
# read file and return list of strings
# input: string
# output: list of string
# example: graduate.csv =  3200,Agriculture operations and related sciences,,,,,,
#                 3201,Agriculture general ,1096,1098,120,181,11,3
#                 3400,Computer and information sciences and support services,,,,,,
#                 3401,Computer and information sciences ,17024,3683,7948,3269,508,140

# read_file('graduate.csv') -> ['3200,Agriculture operations and related sciences,,,,,,\n',
#                             '3201,Agriculture general ,1096,1098,120,181,11,3\n',
#                             '3400,Computer and information sciences and support services,,,,,,\n',
#                             '3401,Computer and information sciences ,17024,3683,7948,3269,508,140']
def read_file(file_name: str) -> list[str]:
    try:
        out_file = open(file_name, 'r')
    except:
        exit('Cannot access file')
    out_file.readline()
    out_file.readline()
    out_file.readline()
    output = out_file.readlines()
    out_file.close()
    return output


# Design Recipe
# create list of Division objects
# input: list of strings
# output: list of Division objects
# example:
# input =  ['3200,Agriculture operations and related sciences,,,,,,\n',
#           '3201,Agriculture general ,1096,1098,120,181,11,3\n',
#           '3400,Computer and information sciences and support services,,,,,,\n',
#           '3401,Computer and information sciences ,17024,3683,7948,3269,508,140']
#
# create_division(input) -> [Division(3200, 'Agriculture operations and related sciences'),
#                            Division(3400, 'Computer and information sciences and support services')]
# check to see if id has two 0's
def create_division(list_str: list[str]) -> list[Division]:
    divisions = []
    for line in list_str:
        line = line.split(',')
        if '00' in line[0]:
            div = Division(int(line[0]), line[1])
            divisions.append(div)
    return divisions

# create list of Graduate objects
# input: list of strings
# output: list of Graduate objects
# example: list =  ['3200,Agriculture operations and related sciences,,,,,,\n',
#                   '3201,Agriculture general ,1096,1098,120,181,11,3\n',
#                   '3400,Computer and information sciences and support services,,,,,,\n',
#                   '3401,Computer and information sciences ,17024,3683,7948,3269,508,140']
#
# create_graduate(list) -> [Graduate(3201, 'Agriculture general ', (1096,1098), (120,181),(11,3)),
#                           Graduate(3401, 'Computer and information sciences ',(17024,3683),(7948,3269),(508,140))]
def create_graduate(list_str: list[str]) -> list[Graduate]:
    graduates = []
    for line in list_str:
        line = line.split(',')
        if '00' not in line[0]:
            grad = Graduate(int(line[0]), line[1], (int(line[2]), int(line[3])),
                            (int(line[4]), int(line[5])), (int(line[6]), int(line[7])))
            graduates.append(grad)
    return graduates


# Design Recipe
# create files for each division
# input: list of division objects and list of graduate objects
# output: csv file
# example: file.csv =  3200,Agriculture operations and related sciences,,,,,,
#                          3201,Agriculture general ,1096,1098,120,181,11,3
#                          3400,Computer and information sciences and support services,,,,,,
#                          3401,Computer and information sciences ,17024,3683,7948,3269,508,140
#
# create_files(create_division(read_file('file.csv')),create_graduate(read_file('file.csv')) -> None
def create_files(lst_div_obj: list[Division], lst_grad_obj: list[Graduate]):
    for div in lst_div_obj:
        file_name = div.division_name.split()[0]+'.csv'
        out_file = open(file_name,'w')
        header = ('This table shows Bachelor\'s, master\'s, and doctor\'s degrees conferred by postsecondary institutions, of '
                  'student and discipline division: 2017-18\n'
                  'ID, Major, Bachelor, Master, Doctor\n')
        out_file.write(header)
        for grad in lst_grad_obj:
            if str(div.id)[0:2] in str(grad.id):
                b_tot = grad.bachelor[0] + grad.bachelor[1]
                m_tot = grad.master[0] + grad.master[1]
                d_tot = grad.doctor[0] + grad.doctor[1]
                out_file.write(str(grad.id)+','+str(grad.major)+','+str(b_tot)+','+str(m_tot)+','+str(d_tot)+'\n')
        out_file.close()


# Design Recipe
# find total and average graduate for all divisions
# input: list of division objects and list of graduate objects
# output: tuple
# example: test.csv =  3200,Agriculture operations and related sciences,,,,,,
#                      3201,Agriculture general ,1096,1098,120,181,11,3
#                      3400,Computer and information sciences and support services,,,,,,
#                      3401,Computer and information sciences ,17024,3683,7948,3269,508,140
#                      3600,Education,,,,,,
#                      3618,Educational/instructional technology ,27,35,1404,3772,69,108
#                      3800,Engineering technologies/construction trades/mechanics and repairers,,,,,,
#                      3855,Engineering design,1,1,43,34,2,0
#
# divisions = create_division(read_file('test.csv'))
# graduates = create_graduate(read_file('test.csv'))
# find_total_avg_all_divisions(division, graduates) -> [(2509,418.17),(32572,5428.67),(5415,902.5),(81,13.5)]
def find_total_avg_all_divisions(lst_div_obj: list[Division], lst_grad_obj: list[Graduate]) -> list[tuple]:
    total_avg = []
    for div in lst_div_obj:
        for grad in lst_grad_obj:
            if str(div.id)[0:2] in str(grad.id):
                tot = grad.bachelor[0] + grad.bachelor[1] + grad.master[0] + grad.master[1] + grad.doctor[0] + grad.doctor[1]
                total_avg.append((tot,round((tot/6),2)))
    return total_avg


# Design Recipe
# find (female, male) graduate rate for given major
# input: list of graduate objects and a string
# output: tuple
# example:
# graduates = [Graduate(3855, 'Engineering Design ',(17024,3683),(7948,3269),(508,140)),
#              Graduate(3201, 'Agriculture general ', (1096,1098), (120,181),(11,3)),
#              Graduate(3856, 'Packaging science ',(17024,3683),(7948,3269),(508,140))]
#
# find_graduate_rate_major(graduates, 'Agriculture general') -> (1227,1282)
def find_graduate_rate_major(lst_grad_obj: list[Graduate], major_name: str) -> tuple:
    male_tot = 0
    fem_tot = 0
    for grad in lst_grad_obj:
        if major_name in grad.major:
            male_tot += grad.bachelor[0] + grad.master[0] + grad.doctor[0]
            fem_tot += grad.bachelor[1] + grad.master[1] + grad.doctor[1]
    return fem_tot,male_tot


# HELPER FUNCTION
# input: list of strings
# output: list of Graduate objects, string
# example:
# input: [Graduate(3855, 'Engineering Design ',(17024,3683),(7948,3269),(508,140)),
#         Graduate(3201, 'Agriculture general ', (1096,1098), (120,181),(11,3)),
#         Graduate(3856, 'Packaging science ',(17024,3683),(7948,3269),(508,140))]
#
# total_grad_in_div(input, 3800) -> (219,292)
def total_grad_in_div(grad_list: list[Graduate], id:str) -> tuple:
    male_tot = 0
    fem_tot = 0
    for grad in grad_list:
        if str(grad.id)[0:2] == id[0:2]:
            male_tot += grad.bachelor[0] + grad.master[0] + grad.doctor[0]
            fem_tot += grad.bachelor[1] + grad.master[1] + grad.doctor[1]
    return fem_tot,male_tot


# IGNORE THIS CODE
# input: list of strings
# output: bool
# example:
# input =  ['3200,Agriculture operations and related sciences,,,,,,\n',
#           '3201,Agriculture general ,1096,1098,120,181,11,3\n',
#           '3400,Computer and information sciences and support services,,,,,,\n',
#           '3401,Computer and information sciences ,17024,3683,7948,3269,508,140']
# check_div(input)
# def check_div(list_str: list[str]) -> bool:
#     for line in list_str:
#         line = line.split(',')
#         if  in line[0]:
#             return True
#     return False