# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
# from PIL import Image

objectlist_A = []
objectlist_B = []
objectlist_C = []
objectlist_1 = []
objectlist_2 = []
objectlist_3 = []
objectlist_4 = []
objectlist_5 = []
objectlist_6 = []


def init_objects():
    global objectlist_A, objectlist_B, objectlist_C, objectlist_1, objectlist_2, objectlist_3, \
        objectlist_4, objectlist_5, objectlist_6
    del objectlist_A[:]
    del objectlist_B[:]
    del objectlist_C[:]
    del objectlist_1[:]
    del objectlist_2[:]
    del objectlist_3[:]
    del objectlist_4[:]
    del objectlist_5[:]
    del objectlist_6[:]


def parse_problem(key_value, object_list):
    for object_name, object_value in sorted(object_list.iteritems()):
        pairs = object_value.attributes
        dict_objects = {}
        for attr_name, attr_value in pairs.iteritems():
            dict_objects[attr_name] = attr_value
            dict_objects['name'] = object_name
        store_attributes(key_value, dict_objects)


def store_attributes(key_value, dict_objects):
    global objectlist_A, objectlist_B, objectlist_C, objectlist_1, objectlist_2, objectlist_3, \
        objectlist_4, objectlist_5, objectlist_6
    if key_value == 'A':
        objectlist_A.append(dict_objects)
    if key_value == 'B':
        objectlist_B.append(dict_objects)
    if key_value == 'C':
        objectlist_C.append(dict_objects)
    if key_value == '1':
        objectlist_1.append(dict_objects)
    if key_value == '2':
        objectlist_2.append(dict_objects)
    if key_value == '3':
        objectlist_3.append(dict_objects)
    if key_value == '4':
        objectlist_4.append(dict_objects)
    if key_value == '5':
        objectlist_5.append(dict_objects)
    if key_value == '6':
        objectlist_6.append(dict_objects)

        # Check A & C and apply to B and solution set


def find_solution_alternate():
    rule_diff = []
    temprule_diff = []
    ref_rules = {'shape': [],  #
                 'size': ['very small', 'small', 'medium', 'large', 'very large', 'huge'],  # order matters
                 'fill': ['no', 'yes'],
                 'angle': [0, 45, 90, 135, 180, 225, 270, 315],  # order matters
                 'inside': [],
                 'above': [],
                 'alignment': ['bottom-left', 'bottom-right', 'top-left', 'top-right'],
                 'overlaps': [],
                 'transform': ['add', 'remove']
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6]
    # solution_list = [objectlist_3]
    # print objectlist_A
    # print objectlist_C
    # print ""

    rule_length = max(len(objectlist_A), len(objectlist_C))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': ''})

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_C in objectlist_C:
                    for keyC, valueC in iter(sorted(dict_C.items())):
                        if keyC != 'name':
                            if valueA not in ref_rules[keyA]:
                                ref_rules[keyA].append(valueA)
                            if valueC not in ref_rules[keyC]:
                                ref_rules[keyC].append(valueC)
                            # print keyA, keyC
                            if keyA == keyC and i == j:
                                rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[
                                    keyC].index(valueC)
                    # print ""
                    j += 1
        i += 1

    rule_add_count = -1
    rule_remove_count = -1
    if i > j:
        rule_remove_count = i - j
        for itr in range(j, i):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'remove'

    if i < j:
        rule_add_count = j - i
        for itr in range(i, j):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'add'

    # for index in range(len(rule_diff)):
    # print rule_diff[index]
    # print ""
    solution_index = 0

    # print objectlist_C
    # print objectlist_4
    # print ""

    for number_list in solution_list:
        solution_index += 1
        ref_rules['inside'] = []  # Hack for ignoring inside, need to code logic for this
        ref_rules['above'] = []  # Hack for ignoring inside, need to code logic for this
        del temprule_diff[:]
        temprule_length = max(len(objectlist_B), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': ''})
        i = 0
        for dict_B in objectlist_B:
            for keyB, valueB in iter(sorted(dict_B.items())):
                if keyB != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueB not in ref_rules[keyB]:
                                    ref_rules[keyB].append(valueB)
                                if valueN not in ref_rules[keyN]:
                                    ref_rules[keyN].append(valueN)
                                if keyB == keyN and i == j:
                                    temprule_diff[j][keyB] = ref_rules[keyB].index(valueB) - ref_rules[keyN].index(
                                        valueN)
                        j += 1
            i += 1

        temprule_add_count = -1
        temprule_remove_count = -1
        if i > j:
            temprule_remove_count = i - j
            for itr in range(j, i):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'remove'

        if i < j:
            temprule_add_count = j - i
            for itr in range(i, j):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'add'

                        # for index in range(len(temprule_diff)):
                        # print temprule_diff[index]
        # print ""

        match = True
        for index in range(min(len(rule_diff), len(temprule_diff))):
            if rule_diff[index]['transform'] == 'add' or rule_diff[index]['transform'] == 'remove' \
                    or temprule_diff[index]['transform'] == 'add' or temprule_diff[index]['transform'] == 'remove':
                break
            if cmp(rule_diff[index], temprule_diff[index]) != 0:
                match = False
                break
        if match and rule_add_count == temprule_add_count and rule_remove_count == temprule_remove_count:
            return solution_index

    # print ref_rules

    return -1

    # Check A & B and apply to C and solution set


def find_solution():
    rule_diff = []
    temprule_diff = []
    ref_rules = {'shape': [],  #
                 'size': ['very small', 'small', 'medium', 'large', 'very large', 'huge'],  # order matters
                 'fill': ['no', 'yes'],
                 'angle': [0, 45, 90, 135, 180, 225, 270, 315],  # order matters
                 'inside': [],
                 'above': [],
                 'alignment': ['bottom-left', 'bottom-right', 'top-left', 'top-right'],
                 'overlaps': [],
                 'transform': ['add', 'remove']
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6]
    # solution_list = [objectlist_6]
    # print objectlist_A
    # print objectlist_B
    # print ""

    rule_length = max(len(objectlist_A), len(objectlist_B))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': ''})

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_B in objectlist_B:
                    for keyB, valueB in iter(sorted(dict_B.items())):
                        if keyB != 'name':
                            if valueA not in ref_rules[keyA]:
                                ref_rules[keyA].append(valueA)
                            if valueB not in ref_rules[keyB]:
                                ref_rules[keyB].append(valueB)
                            if keyA == keyB and i == j:
                                rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[
                                    keyB].index(valueB)
                    j += 1
        i += 1

    # print i, j
    rule_add_count = -1
    rule_remove_count = -1
    if i > j:
        rule_remove_count = i - j
        for itr in range(j, i):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'remove'

    if i < j:
        rule_add_count = j - i
        for itr in range(i, j):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'add'

                    # for index in range(len(rule_diff)):
                    # print rule_diff[index]
    # print ""
    solution_index = 0

    # print objectlist_C
    # print objectlist_4
    # print ""

    for number_list in solution_list:
        solution_index += 1
        ref_rules['inside'] = []  # Hack for ignoring inside, need to code logic for this
        ref_rules['above'] = []  # Hack for ignoring inside, need to code logic for this
        del temprule_diff[:]
        temprule_length = max(len(objectlist_C), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': ''})
        i = 0
        for dict_C in objectlist_C:
            for keyC, valueC in iter(sorted(dict_C.items())):
                if keyC != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueC not in ref_rules[keyC]:
                                    ref_rules[keyC].append(valueC)
                                if valueN not in ref_rules[keyN]:
                                    ref_rules[keyN].append(valueN)
                                if keyC == keyN and i == j:
                                    temprule_diff[j][keyC] = ref_rules[keyC].index(valueC) - ref_rules[keyN].index(
                                        valueN)
                        j += 1
            i += 1

        temprule_add_count = -1
        temprule_remove_count = -1
        if i > j:
            temprule_remove_count = i - j
            for itr in range(j, i):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'remove'

        if i < j:
            temprule_add_count = j - i
            for itr in range(i, j):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'add'
                        # for index in range(len(temprule_diff)):
                        # print temprule_diff[index]
        # print ""

        match = True
        for index in range(min(len(rule_diff), len(temprule_diff))):
            if rule_diff[index]['transform'] == 'add' or rule_diff[index]['transform'] == 'remove' \
                    or temprule_diff[index]['transform'] == 'add' or temprule_diff[index]['transform'] == 'remove':
                break
            if cmp(rule_diff[index], temprule_diff[index]) != 0:
                match = False
                break
        if match and rule_add_count == temprule_add_count and rule_remove_count == temprule_remove_count:
            return solution_index

    # print ref_rules

    solution_index = find_solution_alternate()
    return solution_index


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self, problem):
        init_objects()
        # print problem.name
        if problem.hasVerbal:
            if problem.problemType == '2x2':
                prob = problem.figures
                for key, value in sorted(prob.iteritems()):
                    figure = prob[key]
                    object_list = figure.objects
                    # print "length of object_list is ", len(object_list)
                    parse_problem(key, object_list)
                    # print "----"
                    # print "********"

                i = find_solution()
                return i
            else:
                return -1
        else:
            return -1
