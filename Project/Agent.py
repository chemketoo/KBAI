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

from PIL import Image
from itertools import izip
import math

__author__ = "Bhanu Verma"

figureA_Image = None
figureB_Image = None
figureC_Image = None
figureD_Image = None
figureE_Image = None
figureF_Image = None
figureG_Image = None
figureH_Image = None
figure1_Image = None
figure2_Image = None
figure3_Image = None
figure4_Image = None
figure5_Image = None
figure6_Image = None
figure7_Image = None
figure8_Image = None

objectlist_A = []
objectlist_B = []
objectlist_C = []
objectlist_D = []
objectlist_E = []
objectlist_F = []
objectlist_G = []
objectlist_H = []
objectlist_1 = []
objectlist_2 = []
objectlist_3 = []
objectlist_4 = []
objectlist_5 = []
objectlist_6 = []
objectlist_7 = []
objectlist_8 = []


def init_objects():
    global objectlist_A, objectlist_B, objectlist_C, objectlist_1, objectlist_2, objectlist_3, \
        objectlist_4, objectlist_5, objectlist_6
    del objectlist_A[:]
    del objectlist_B[:]
    del objectlist_C[:]
    del objectlist_D[:]
    del objectlist_E[:]
    del objectlist_F[:]
    del objectlist_G[:]
    del objectlist_H[:]
    del objectlist_1[:]
    del objectlist_2[:]
    del objectlist_3[:]
    del objectlist_4[:]
    del objectlist_5[:]
    del objectlist_6[:]
    del objectlist_7[:]
    del objectlist_8[:]


def parse_problem(key_value, object_list):
    for object_name, object_value in sorted(object_list.iteritems()):
        pairs = object_value.attributes
        dict_objects = {}
        for attr_name, attr_value in pairs.iteritems():
            dict_objects[attr_name] = attr_value
            dict_objects['name'] = object_name
        store_attributes(key_value, dict_objects)


def load_image(key_value, file_name):
    global figureA_Image, figureB_Image, figureC_Image, figureD_Image, figureE_Image, figureF_Image, figureG_Image, \
        figureH_Image, figure1_Image, figure2_Image, figure3_Image, figure4_Image, figure5_Image, figure6_Image, \
        figure7_Image, figure8_Image
    if key_value == 'A':
        figureA_Image = Image.open(file_name)
    if key_value == 'B':
        figureB_Image = Image.open(file_name)
    if key_value == 'C':
        figureC_Image = Image.open(file_name)
    if key_value == 'D':
        figureD_Image = Image.open(file_name)
    if key_value == 'E':
        figureE_Image = Image.open(file_name)
    if key_value == 'F':
        figureF_Image = Image.open(file_name)
    if key_value == 'G':
        figureG_Image = Image.open(file_name)
    if key_value == 'H':
        figureH_Image = Image.open(file_name)
    if key_value == '1':
        figure1_Image = Image.open(file_name)
    if key_value == '2':
        figure2_Image = Image.open(file_name)
    if key_value == '3':
        figure3_Image = Image.open(file_name)
    if key_value == '4':
        figure4_Image = Image.open(file_name)
    if key_value == '5':
        figure5_Image = Image.open(file_name)
    if key_value == '6':
        figure6_Image = Image.open(file_name)
    if key_value == '7':
        figure7_Image = Image.open(file_name)
    if key_value == '8':
        figure8_Image = Image.open(file_name)


def store_attributes(key_value, dict_objects):
    global objectlist_A, objectlist_B, objectlist_C, objectlist_D, objectlist_E, objectlist_F, objectlist_G, \
        objectlist_H, objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6, objectlist_7, objectlist_8
    if key_value == 'A':
        objectlist_A.append(dict_objects)
    if key_value == 'B':
        objectlist_B.append(dict_objects)
    if key_value == 'C':
        objectlist_C.append(dict_objects)
    if key_value == 'D':
        objectlist_D.append(dict_objects)
    if key_value == 'E':
        objectlist_E.append(dict_objects)
    if key_value == 'F':
        objectlist_F.append(dict_objects)
    if key_value == 'G':
        objectlist_G.append(dict_objects)
    if key_value == 'H':
        objectlist_H.append(dict_objects)
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
    if key_value == '7':
        objectlist_7.append(dict_objects)
    if key_value == '8':
        objectlist_8.append(dict_objects)

        # Check A & C and apply to B and solution set


def map_vertically_advanced():
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
                 'transform': ['add', 'remove'],
                 'left-of': [],
                 'height': ['very small', 'small', 'medium', 'large', 'very large', 'huge'],
                 'width': ['very small', 'small', 'medium', 'large', 'very large', 'huge']
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6]

    rule_length = max(len(objectlist_A), len(objectlist_C))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': '', 'left-of': '', 'height': 0, 'width': 0})

    objectlist_A.sort(lambda x, y: cmp(len(x), len(y)))
    objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_C in objectlist_C:
                    for keyC, valueC in iter(sorted(dict_C.items())):
                        if keyC != 'name':
                            if valueA not in ref_rules[keyA]:
                                if keyA != 'inside' and keyA != 'above':
                                    ref_rules[keyA].append(valueA)
                            if valueC not in ref_rules[keyC]:
                                if keyC != 'inside' and keyC != 'above':
                                    ref_rules[keyC].append(valueC)
                            if keyA == keyC and i == j:
                                if keyA == 'inside' or keyA == 'above':
                                    rule_diff[j][keyA] = len(valueA) - len(valueC)
                                else:
                                    rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[keyC].index(valueC)
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

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        del temprule_diff[:]
        temprule_length = max(len(objectlist_B), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': '', 'left-of': '', 'height': 0, 'width': 0})

        # number_list.sort(lambda x, y: cmp(len(x), len(y)))
        # objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

        i = 0
        for dict_B in objectlist_B:
            for keyB, valueB in iter(sorted(dict_B.items())):
                if keyB != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueB not in ref_rules[keyB]:
                                    if keyB != 'inside' and keyB != 'above':
                                        ref_rules[keyB].append(valueB)
                                if valueN not in ref_rules[keyN]:
                                    if keyN != 'inside' and keyN != 'above':
                                        ref_rules[keyN].append(valueN)
                                if keyB == keyN and i == j:
                                    if keyB == 'inside' or keyB == 'above':
                                        temprule_diff[j][keyB] = len(valueB) - len(valueN)
                                    else:
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

    return -1


def find_solution_advanced():
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
                 'transform': ['add', 'remove'],
                 'left-of': [],
                 'height': ['very small', 'small', 'medium', 'large', 'very large', 'huge'],
                 'width': ['very small', 'small', 'medium', 'large', 'very large', 'huge']
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6, objectlist_7,
                     objectlist_8]

    rule_length = max(len(objectlist_A), len(objectlist_B))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': '', 'left-of': '', 'height': 0, 'width': 0})

    objectlist_A.sort(lambda x, y: cmp(len(x), len(y)))
    objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

    i = 0
    print len(objectlist_A)
    print len(objectlist_B)
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_B in objectlist_B:
                    for keyB, valueB in iter(sorted(dict_B.items())):
                        if keyB != 'name':
                            if valueA not in ref_rules[keyA]:
                                if keyA != 'inside' and keyA != 'above':
                                    ref_rules[keyA].append(valueA)
                            if valueB not in ref_rules[keyB]:
                                if keyB != 'inside' and keyB != 'above':
                                    ref_rules[keyB].append(valueB)
                            if keyA == keyB and i == j:
                                if keyA == 'inside' or keyA == 'above':
                                    rule_diff[j][keyA] = len(valueA) - len(valueB)
                                else:
                                    rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[
                                        keyB].index(valueB)
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

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        del temprule_diff[:]
        temprule_length = max(len(objectlist_C), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': '', 'left-of': '', 'height': 0, 'width': 0})

        number_list.sort(lambda x, y: cmp(len(x), len(y)))
        objectlist_C.sort(lambda x, y: cmp(len(x), len(y)))

        i = 0
        for dict_C in objectlist_C:
            for keyC, valueC in iter(sorted(dict_C.items())):
                if keyC != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueC not in ref_rules[keyC]:
                                    if keyC != 'inside' and keyC != 'above':
                                        ref_rules[keyC].append(valueC)
                                if valueN not in ref_rules[keyN]:
                                    if keyN != 'inside' and keyN != 'above':
                                        ref_rules[keyN].append(valueN)
                                if keyC == keyN and i == j:
                                    if keyC == 'inside' or keyC == 'above':
                                        temprule_diff[j][keyC] = len(valueC) - len(valueN)
                                    else:
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

        match = True
        for index in range(min(len(rule_diff), len(temprule_diff))):
            if rule_diff[index]['transform'] == 'add' or rule_diff[index]['transform'] == 'remove' \
                    or temprule_diff[index]['transform'] == 'add' or temprule_diff[index]['transform'] == 'remove':
                break
            if cmp(rule_diff[index], temprule_diff[index]) != 0:
                match = False
                break

        if match and rule_add_count == temprule_add_count and rule_remove_count == temprule_remove_count:
            temp_index = map_vertically_advanced()
            if temp_index == solution_index and solution_index != -1:
                print "Solved by both horizontal and vertical symmetry" + "\n"
                return solution_index
            else:
                if solution_index != -1:
                    print "Solved by horizontal symmetry" + "\n"
                    return solution_index
                elif temp_index != -1:
                    print "Solved by vertical symmetry" + "\n"
                    return temp_index

    return -1


def check_symmetry():
    global figureA_Image, figureB_Image, figureC_Image, figureD_Image, figureE_Image, figureF_Image, figureG_Image, \
        figureH_Image, figure1_Image, figure2_Image, figure3_Image, figure4_Image, figure5_Image, figure6_Image, \
        figure7_Image, figure8_Image

    value_array = []
    transpose_a = figureA_Image.transpose(Image.FLIP_LEFT_RIGHT)
    diff = find_difference(transpose_a, figureC_Image)

    if diff < 1:
        transpose_g = figureG_Image.transpose(Image.FLIP_LEFT_RIGHT)
        diff_1 = math.fabs(find_difference(transpose_g, figure1_Image) - diff)
        value_array.append(diff_1)
        diff_2 = math.fabs(find_difference(transpose_g, figure2_Image) - diff)
        value_array.append(diff_2)
        diff_3 = math.fabs(find_difference(transpose_g, figure3_Image) - diff)
        value_array.append(diff_3)
        diff_4 = math.fabs(find_difference(transpose_g, figure4_Image) - diff)
        value_array.append(diff_4)
        diff_5 = math.fabs(find_difference(transpose_g, figure5_Image) - diff)
        value_array.append(diff_5)
        diff_6 = math.fabs(find_difference(transpose_g, figure6_Image) - diff)
        value_array.append(diff_6)
        diff_7 = math.fabs(find_difference(transpose_g, figure7_Image) - diff)
        value_array.append(diff_7)
        diff_8 = math.fabs(find_difference(transpose_g, figure8_Image) - diff)
        value_array.append(diff_8)

        return value_array.index(min(value_array)) + 1
    else:
        return -1


def find_difference(first_figure, second_figure):
    pairs = izip(first_figure.getdata(), second_figure.getdata())
    if len(first_figure.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = first_figure.size[0] * first_figure.size[1] * 3
    # print "Difference (percentage):", (dif / 255.0 * 100) / ncomponents

    return (dif / 255.0 * 100) / ncomponents


def find_solution_visual():
    answer = check_symmetry()
    return answer


def map_vertically_basic():
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

    rule_length = max(len(objectlist_A), len(objectlist_C))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': ''})

    objectlist_A.sort(lambda x, y: cmp(len(x), len(y)))
    objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_C in objectlist_C:
                    for keyC, valueC in iter(sorted(dict_C.items())):
                        if keyC != 'name':
                            if valueA not in ref_rules[keyA]:
                                if keyA != 'inside' and keyA != 'above':
                                    ref_rules[keyA].append(valueA)
                            if valueC not in ref_rules[keyC]:
                                if keyC != 'inside' and keyC != 'above':
                                    ref_rules[keyC].append(valueC)
                            if keyA == keyC and i == j:
                                if keyA == 'inside' or keyA == 'above':
                                    rule_diff[j][keyA] = len(valueA) - len(valueC)
                                else:
                                    rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[keyC].index(valueC)
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

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        del temprule_diff[:]
        temprule_length = max(len(objectlist_B), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': ''})

        # number_list.sort(lambda x, y: cmp(len(x), len(y)))
        # objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

        i = 0
        for dict_B in objectlist_B:
            for keyB, valueB in iter(sorted(dict_B.items())):
                if keyB != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueB not in ref_rules[keyB]:
                                    if keyB != 'inside' and keyB != 'above':
                                        ref_rules[keyB].append(valueB)
                                if valueN not in ref_rules[keyN]:
                                    if keyN != 'inside' and keyN != 'above':
                                        ref_rules[keyN].append(valueN)
                                if keyB == keyN and i == j:
                                    if keyB == 'inside' or keyB == 'above':
                                        temprule_diff[j][keyB] = len(valueB) - len(valueN)
                                    else:
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

    return -1


def find_solution_basic():
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

    rule_length = max(len(objectlist_A), len(objectlist_B))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': ''})

    objectlist_A.sort(lambda x, y: cmp(len(x), len(y)))
    objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_B in objectlist_B:
                    for keyB, valueB in iter(sorted(dict_B.items())):
                        if keyB != 'name':
                            if valueA not in ref_rules[keyA]:
                                if keyA != 'inside' and keyA != 'above':
                                    ref_rules[keyA].append(valueA)
                            if valueB not in ref_rules[keyB]:
                                if keyB != 'inside' and keyB != 'above':
                                    ref_rules[keyB].append(valueB)
                            if keyA == keyB and i == j:
                                if keyA == 'inside' or keyA == 'above':
                                    rule_diff[j][keyA] = len(valueA) - len(valueB)
                                else:
                                    rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[
                                        keyB].index(valueB)
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

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        del temprule_diff[:]
        temprule_length = max(len(objectlist_C), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': ''})

        number_list.sort(lambda x, y: cmp(len(x), len(y)))
        objectlist_C.sort(lambda x, y: cmp(len(x), len(y)))

        i = 0
        for dict_C in objectlist_C:
            for keyC, valueC in iter(sorted(dict_C.items())):
                if keyC != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueC not in ref_rules[keyC]:
                                    if keyC != 'inside' and keyC != 'above':
                                        ref_rules[keyC].append(valueC)
                                if valueN not in ref_rules[keyN]:
                                    if keyN != 'inside' and keyN != 'above':
                                        ref_rules[keyN].append(valueN)
                                if keyC == keyN and i == j:
                                    if keyC == 'inside' or keyC == 'above':
                                        temprule_diff[j][keyC] = len(valueC) - len(valueN)
                                    else:
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

        match = True
        for index in range(min(len(rule_diff), len(temprule_diff))):
            if rule_diff[index]['transform'] == 'add' or rule_diff[index]['transform'] == 'remove' \
                    or temprule_diff[index]['transform'] == 'add' or temprule_diff[index]['transform'] == 'remove':
                break
            if cmp(rule_diff[index], temprule_diff[index]) != 0:
                match = False
                break

        if match and rule_add_count == temprule_add_count and rule_remove_count == temprule_remove_count:
            temp_index = map_vertically_basic()
            if temp_index == solution_index and solution_index != -1:
                print "Solved by both horizontal and vertical symmetry" + "\n"
                return solution_index
            else:
                if solution_index != -1:
                    print "Solved by horizontal symmetry" + "\n"
                    return solution_index
                elif temp_index != -1:
                    print "Solved by vertical symmetry" + "\n"
                    return temp_index

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
        print "Attempting to solve " + problem.name
        if problem.problemType == '2x2':
            prob = problem.figures
            for key, value in sorted(prob.iteritems()):
                figure = prob[key]
                object_list = figure.objects
                parse_problem(key, object_list)
            i = find_solution_basic()
            if i == -1:
                print "Hmmm, this looks tricky. I would skip this problem." + "\n"
            return i
        elif problem.problemType == '3x3':
            prob = problem.figures
            for key, value in sorted(prob.iteritems()):
                figure = prob[key]
                file_name = figure.visualFilename
                load_image(key, file_name)
            i = find_solution_visual()
            if i == -1:
                print "Hmmm, this looks tricky. I would skip this problem." + "\n"
            return i
        else:
            print "My creator has not equipped me to handle 3x3 problems yet. I would skip this problem." + "\n"
            return -1
