#get each test case coverage infomation
import re
import random
setState=set()
setBlock=set()
setBranch=set([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 132, 133, 134, 135, 136, 138, 139, 140, 141, 142, 143, 145, 146, 147, 149, 151, 152, 153, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 172, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 190, 191, 192, 193, 194, 195, 196, 197, 198, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 227, 228, 229, 230, 232, 233, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 254, 255, 257, 258, 259, 260, 261, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 297, 299, 300, 302, 304, 310, 312, 313, 314, 315, 316, 317, 318, 319, 321, 322, 324, 325, 327, 328, 329, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 348, 349, 350, 351, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 409, 410, 411, 412, 413, 415, 416, 417, 418, 419, 420, 421, 422, 423, 425, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 439, 440, 441, 443, 444, 445, 446, 447, 449, 452, 453, 455, 456, 457, 458, 459, 460, 461, 462, 463, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 482, 483, 484, 485, 486, 487, 489, 492, 493, 494, 495, 496, 498, 499, 500, 501, 502, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 546, 547, 548, 549, 550, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 564, 565, 566, 567, 568, 570, 571, 572, 573, 574, 576, 577, 578, 579, 580, 582, 583, 584, 585, 588, 590, 591, 592, 593, 594, 595, 596, 598, 599, 600, 602, 603, 604, 605, 606, 607, 608, 610, 611, 612, 613, 614, 616, 617, 619, 621, 622, 623, 624, 626, 627, 628, 630, 631, 632, 633, 636, 637, 638, 639, 640, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 666, 667, 668, 669, 670, 672, 673, 674, 676, 677, 678, 679, 680, 696, 697, 698, 699, 700, 701, 702, 703, 705, 706, 707, 708, 710, 711, 712, 713, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730, 731, 732, 734, 735, 736, 737, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748, 749, 750, 751, 752, 753, 755, 756, 757, 758, 759, 760, 761, 762, 763, 765, 766, 767, 768, 769, 770, 771, 772, 773, 775, 776, 777, 778, 779, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 861, 862, 863, 865, 866, 867, 868, 869, 871, 872, 873, 874, 875, 877, 879, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 903, 904, 905, 906, 907, 909, 910, 911, 912, 913, 915, 916, 917, 918, 919, 921, 922, 923, 924, 925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947, 948, 951, 952, 953, 954, 955, 956, 957, 958, 960, 961, 962, 963, 964, 967, 968, 969, 970, 971, 972, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1076, 1077, 1078, 1079, 1080, 1081, 1083, 1084, 1085, 1086, 1087, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1109, 1110, 1111, 1112, 1113, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186])
def writeCoverage(inFileNum,proName):
    #with open(r'D:/space_2.0/%s/info/overallCovInfo.txt'%(proName),'w') as outf:
		#outf.write('test%d coverage info\n'%(testNum))
    with open(r'D:/space_2.0/%s/test_gcov/test1.txt'%(proName),'r') as inf:
        branchCount = 0
        stateCov=[]
        blockCov=[]
        branchCov=[]
        for line in inf.readlines():
            #state coverage info
            # m=re.match(r'.*([\d+,])[:]\s+(\d+)[:].*',line)
            # if m:
            #     stateCov.append(m.group(2))
            #     setState.add(m.group(2))
            #block coverage info
            m=re.match(r'.*[:]\s+(\d+)-block\s+(\d+).*',line)
            if m:
                blockCov.append('%s:%s'%(m.group(1),m.group(2)))
                setBlock.add('%s:%s'%(m.group(1),m.group(2)))
            #branch coverage info
            # m=re.match(r'branch.*',line)
            # if m:
            #     branchCount=branchCount+1
            # m=re.match(r'branch\s+\d+\s+taken\s+(\d+)%.*',line)
            # if m and int(m.group(1))>0:
            #     branchCov.append(branchCount)
            #     setBranch.add(branchCount)
		# outf.write('state coverage info\n');
		# for statement in stateCov:
			# outf.write('%s,'%(statement))
		# outf.write('\n');

		# outf.write('block coverage info\n');
		# for block in blockCov:
			# outf.write('%s,'%(block))
		# outf.write('\n')

		# outf.write('branch coverage info\n');
		# for branch in branchCov:
			# outf.write('%d,'%(branch))
		# outf.write('\n')

def createTestSuite(proName):
    # testSuite = []
    # suiteStateCovInfo = []
    # suiteBlockCovInfo = []
    # suiteBranchCovInfo = []
    # testStateCovInfo = set()
    # testBlockCovInfo = set()
    # testBranchCovInfo = set()
    # allBranchCovInfo = set()

    #get covfile info
    covFileInfo=[]
    with open(r'D:/space_2.0/%s/info/overallCovInfo.txt'%(proName),'r') as covInfoF:
        for line in covInfoF.readlines():
            covFileInfo.append(line.strip())
    stateFile=open(r'D:/space_2.0/%s/info/stateFile.txt'%(proName),'w')
    blockFile=open(r'D:/space_2.0/%s/info/blockFile.txt'%(proName),'w')
    branchFile=open(r'D:/space_2.0/%s/info/branchFile.txt'%(proName),'w')
    # random select a test case from test p
    for i in range(500):
        testSuite = []
        suiteStateCovInfo = []
        suiteBlockCovInfo = []
        suiteBranchCovInfo = []
        while(len(testSuite) < 20):
            ranNum=random.randint(1,13525)
            lineNum=0;
            for line in covFileInfo:
                lineNum=lineNum+1
                m=re.match(r'test(\d+)\s+coverage\s+info.*',line)
                if m and ranNum == int(m.group(1)):
                    break
            s=covFileInfo[lineNum-1+6].split(',')
            s.pop()
            if(ranNum not in testSuite):
                testSuite.append(ranNum)
                suiteStateCovInfo.append(covFileInfo[lineNum-1+2])
                suiteBlockCovInfo.append(covFileInfo[lineNum-1+4])
                suiteBranchCovInfo.append(covFileInfo[lineNum-1+6])
        stateFile.write('test suite%d\ntest case:'%(i+1))
        for num in testSuite:
            stateFile.write('%d,'%(num))
        stateFile.write('\n')
        for cov in suiteStateCovInfo:
            stateFile.write('%s|'%(cov))
        stateFile.write('\n')

        blockFile.write('test suite%d\ntest case:' % (i + 1))
        for num in testSuite:
            blockFile.write('%d,' % (num))
        blockFile.write('\n')
        for cov in suiteBlockCovInfo:
            blockFile.write('%s|' % (cov))
        blockFile.write('\n')

        branchFile.write('test suite%d\ntest case:' % (i + 1))
        for num in testSuite:
            branchFile.write('%d,' % (num))
        branchFile.write('\n')
        for cov in suiteBranchCovInfo:
            branchFile.write('%s|' % (cov))
        branchFile.write('\n')

    stateFile.close()
    blockFile.close()
    branchFile.close()

def getAvgSuiteSize(proName):
    suiteSize=[]
    with open(r'D:/space_2.0/%s/info/stateFile.txt'%(proName),'r') as inFileF:
        for line in inFileF.readlines():
            m=re.match(r'test\s+case:(.*),\n',line)
            if m:
                suiteSize.append(len(m.group(1).split(',')))
    sum=0
    for size in suiteSize:
        sum=sum+size
    print sum/len(suiteSize)

if __name__=='__main__':
    writeCoverage(13525,'space')
    # print setBranch
    #createTestSuite('space')
    # getAvgSuiteSize('space')
    print 'setState:%d,setBlock:%d,setBranch:%d'%(len(setState),len(setBlock),len(setBranch))