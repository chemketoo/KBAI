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
            # print attr_name, attr_value
        store_attributes(key_value, dict_objects)


def store_attributes(key_value, dict_objects):
    global objectlist_A, objectlist_B, objectlist_C, objectlist_1, objectlist_2, objectlist_3, \
        objectlist_4, objectlist_5, objectlist_6
    if key_value == 'A':
        objectlist_A.append(dict_objects)
        # print objectlist_A
    if key_value == 'B':
        objectlist_B.append(dict_objects)
        # print objectlist_B
    if key_value == 'C':
        objectlist_C.append(dict_objects)
        # print objectlist_C
    if key_value == '1':
        objectlist_1.append(dict_objects)
        # print objectlist_1
    if key_value == '2':
        objectlist_2.append(dict_objects)
        # print objectlist_2
    if key_value == '3':
        objectlist_3.append(dict_objects)
        # print objectlist_3
    if key_value == '4':
        objectlist_4.append(dict_objects)
        # print objectlist_4
    if key_value == '5':
        objectlist_5.append(dict_objects)
        # print objectlist_5
    if key_value == '6':
        objectlist_6.append(dict_objects)
        # print objectlist_6


def find_solution():
    rule = {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
            'overlaps': ''}
    ref_rules = {'shape': [],  #
                 'size': ['small', 'medium', 'large', 'very large', 'huge'],  # order matters
                 'fill': [],
                 'angle': [0, 45, 90, 135, 180, 225, 270, 315],  # order matters
                 'inside': [],
                 'above': [],
                 'alignment': ['bottom-left', 'bottom-right', 'top-left', 'top-right'],
                 'overlaps': []
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6]

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            j = 0
            for dict_B in objectlist_B:
                for keyB, valueB in iter(sorted(dict_B.items())):
                    if valueA not in ref_rules[keyA]:
                        ref_rules[keyA].append(valueA)
                    if valueB not in ref_rules[keyB]:
                        ref_rules[keyB].append(valueB)
                    if keyB == keyA and i == j:
                        rule[keyA] = ref_rules[keyA].index(valueA) - ref_rules[keyB].index(valueB)
                j += 1
        i += 1

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        temp_rule = {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                     'overlaps': ''}
        i = 0
        for dict_C in objectlist_C:
            for keyC, valueC in iter(sorted(dict_C.items())):
                j = 0
                for dict_N in number_list:
                    for keyN, valueN in iter(sorted(dict_N.items())):
                        if valueC not in ref_rules[keyC]:
                            ref_rules[keyC].append(valueC)
                        if valueN not in ref_rules[keyN]:
                            ref_rules[keyN].append(valueN)
                        if keyN == keyC and i == j:
                            temp_rule[keyC] = ref_rules[keyC].index(valueC) - ref_rules[keyN].index(valueN)
                    j += 1
            i += 1

        if cmp(rule, temp_rule) == 0:
            return solution_index

    return -1


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
