# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Mason"
__date__ = "$9-Jan-2016 6:57:17 PM$"

def main():
    import re
    numOfLights = list(range(1000))
    lightArray = {}
    for x in numOfLights:
        lightArray[x] = {}
        for y in numOfLights:
            lightArray[x][y] = 0
    inputString = "turn on 887,9 through 959,629_turn on 454,398 through 844,448_turn off 539,243 through 559,965_turn off 370,819 through 676,868_turn off 145,40 through 370,997_turn off 301,3 through 808,453_turn on 351,678 through 951,908_toggle 720,196 through 897,994_toggle 831,394 through 904,860_toggle 753,664 through 970,926_turn off 150,300 through 213,740_turn on 141,242 through 932,871_toggle 294,259 through 474,326_toggle 678,333 through 752,957_toggle 393,804 through 510,976_turn off 6,964 through 411,976_turn off 33,572 through 978,590_turn on 579,693 through 650,978_turn on 150,20 through 652,719_turn off 782,143 through 808,802_turn off 240,377 through 761,468_turn off 899,828 through 958,967_turn on 613,565 through 952,659_turn on 295,36 through 964,978_toggle 846,296 through 969,528_turn off 211,254 through 529,491_turn off 231,594 through 406,794_turn off 169,791 through 758,942_turn on 955,440 through 980,477_toggle 944,498 through 995,928_turn on 519,391 through 605,718_toggle 521,303 through 617,366_turn off 524,349 through 694,791_toggle 391,87 through 499,792_toggle 562,527 through 668,935_turn off 68,358 through 857,453_toggle 815,811 through 889,828_turn off 666,61 through 768,87_turn on 27,501 through 921,952_turn on 953,102 through 983,471_turn on 277,552 through 451,723_turn off 64,253 through 655,960_turn on 47,485 through 734,977_turn off 59,119 through 699,734_toggle 407,898 through 493,955_toggle 912,966 through 949,991_turn on 479,990 through 895,990_toggle 390,589 through 869,766_toggle 593,903 through 926,943_toggle 358,439 through 870,528_turn off 649,410 through 652,875_turn on 629,834 through 712,895_toggle 254,555 through 770,901_toggle 641,832 through 947,850_turn on 268,448 through 743,777_turn off 512,123 through 625,874_turn off 498,262 through 930,811_turn off 835,158 through 886,242_toggle 546,310 through 607,773_turn on 501,505 through 896,909_turn off 666,796 through 817,924_toggle 987,789 through 993,809_toggle 745,8 through 860,693_toggle 181,983 through 731,988_turn on 826,174 through 924,883_turn on 239,228 through 843,993_turn on 205,613 through 891,667_toggle 867,873 through 984,896_turn on 628,251 through 677,681_toggle 276,956 through 631,964_turn on 78,358 through 974,713_turn on 521,360 through 773,597_turn off 963,52 through 979,502_turn on 117,151 through 934,622_toggle 237,91 through 528,164_turn on 944,269 through 975,453_toggle 979,460 through 988,964_turn off 440,254 through 681,507_toggle 347,100 through 896,785_turn off 329,592 through 369,985_turn on 931,960 through 979,985_toggle 703,3 through 776,36_toggle 798,120 through 908,550_turn off 186,605 through 914,709_turn off 921,725 through 979,956_toggle 167,34 through 735,249_turn on 726,781 through 987,936_toggle 720,336 through 847,756_turn on 171,630 through 656,769_turn off 417,276 through 751,500_toggle 559,485 through 584,534_turn on 568,629 through 690,873_toggle 248,712 through 277,988_toggle 345,594 through 812,723_turn off 800,108 through 834,618_turn off 967,439 through 986,869_turn on 842,209 through 955,529_turn on 132,653 through 357,696_turn on 817,38 through 973,662_turn off 569,816 through 721,861_turn on 568,429 through 945,724_turn on 77,458 through 844,685_turn off 138,78 through 498,851_turn on 136,21 through 252,986_turn off 2,460 through 863,472_turn on 172,81 through 839,332_turn on 123,216 through 703,384_turn off 879,644 through 944,887_toggle 227,491 through 504,793_toggle 580,418 through 741,479_toggle 65,276 through 414,299_toggle 482,486 through 838,931_turn off 557,768 through 950,927_turn off 615,617 through 955,864_turn on 859,886 through 923,919_turn on 391,330 through 499,971_toggle 521,835 through 613,847_turn on 822,787 through 989,847_turn on 192,142 through 357,846_turn off 564,945 through 985,945_turn off 479,361 through 703,799_toggle 56,481 through 489,978_turn off 632,991 through 774,998_toggle 723,526 through 945,792_turn on 344,149 through 441,640_toggle 568,927 through 624,952_turn on 621,784 through 970,788_toggle 665,783 through 795,981_toggle 386,610 through 817,730_toggle 440,399 through 734,417_toggle 939,201 through 978,803_turn off 395,883 through 554,929_turn on 340,309 through 637,561_turn off 875,147 through 946,481_turn off 945,837 through 957,922_turn off 429,982 through 691,991_toggle 227,137 through 439,822_toggle 4,848 through 7,932_turn off 545,146 through 756,943_turn on 763,863 through 937,994_turn on 232,94 through 404,502_turn off 742,254 through 930,512_turn on 91,931 through 101,942_toggle 585,106 through 651,425_turn on 506,700 through 567,960_turn off 548,44 through 718,352_turn off 194,827 through 673,859_turn off 6,645 through 509,764_turn off 13,230 through 821,361_turn on 734,629 through 919,631_toggle 788,552 through 957,972_toggle 244,747 through 849,773_turn off 162,553 through 276,887_turn off 569,577 through 587,604_turn off 799,482 through 854,956_turn on 744,535 through 909,802_toggle 330,641 through 396,986_turn off 927,458 through 966,564_toggle 984,486 through 986,913_toggle 519,682 through 632,708_turn on 984,977 through 989,986_toggle 766,423 through 934,495_turn on 17,509 through 947,718_turn on 413,783 through 631,903_turn on 482,370 through 493,688_turn on 433,859 through 628,938_turn off 769,549 through 945,810_turn on 178,853 through 539,941_turn off 203,251 through 692,433_turn off 525,638 through 955,794_turn on 169,70 through 764,939_toggle 59,352 through 896,404_toggle 143,245 through 707,320_turn off 103,35 through 160,949_toggle 496,24 through 669,507_turn off 581,847 through 847,903_turn on 689,153 through 733,562_turn on 821,487 through 839,699_turn on 837,627 through 978,723_toggle 96,748 through 973,753_toggle 99,818 through 609,995_turn on 731,193 through 756,509_turn off 622,55 through 813,365_turn on 456,490 through 576,548_turn on 48,421 through 163,674_turn off 853,861 through 924,964_turn off 59,963 through 556,987_turn on 458,710 through 688,847_toggle 12,484 through 878,562_turn off 241,964 through 799,983_turn off 434,299 through 845,772_toggle 896,725 through 956,847_turn on 740,289 through 784,345_turn off 395,840 through 822,845_turn on 955,224 through 996,953_turn off 710,186 through 957,722_turn off 485,949 through 869,985_turn on 848,209 through 975,376_toggle 221,241 through 906,384_turn on 588,49 through 927,496_turn on 273,332 through 735,725_turn on 505,962 through 895,962_toggle 820,112 through 923,143_turn on 919,792 through 978,982_toggle 489,461 through 910,737_turn off 202,642 through 638,940_turn off 708,953 through 970,960_toggle 437,291 through 546,381_turn on 409,358 through 837,479_turn off 756,279 through 870,943_turn off 154,657 through 375,703_turn off 524,622 through 995,779_toggle 514,221 through 651,850_toggle 808,464 through 886,646_toggle 483,537 through 739,840_toggle 654,769 through 831,825_turn off 326,37 through 631,69_turn off 590,570 through 926,656_turn off 881,913 through 911,998_turn on 996,102 through 998,616_turn off 677,503 through 828,563_turn on 860,251 through 877,441_turn off 964,100 through 982,377_toggle 888,403 through 961,597_turn off 632,240 through 938,968_toggle 731,176 through 932,413_turn on 5,498 through 203,835_turn on 819,352 through 929,855_toggle 393,813 through 832,816_toggle 725,689 through 967,888_turn on 968,950 through 969,983_turn off 152,628 through 582,896_turn off 165,844 through 459,935_turn off 882,741 through 974,786_turn off 283,179 through 731,899_toggle 197,366 through 682,445_turn on 106,309 through 120,813_toggle 950,387 through 967,782_turn off 274,603 through 383,759_turn off 155,665 through 284,787_toggle 551,871 through 860,962_turn off 30,826 through 598,892_toggle 76,552 through 977,888_turn on 938,180 through 994,997_toggle 62,381 through 993,656_toggle 625,861 through 921,941_turn on 685,311 through 872,521_turn on 124,934 through 530,962_turn on 606,379 through 961,867_turn off 792,735 through 946,783_turn on 417,480 through 860,598_toggle 178,91 through 481,887_turn off 23,935 through 833,962_toggle 317,14 through 793,425_turn on 986,89 through 999,613_turn off 359,201 through 560,554_turn off 729,494 through 942,626_turn on 204,143 through 876,610_toggle 474,97 through 636,542_turn off 902,924 through 976,973_turn off 389,442 through 824,638_turn off 622,863 through 798,863_turn on 840,622 through 978,920_toggle 567,374 through 925,439_turn off 643,319 through 935,662_toggle 185,42 through 294,810_turn on 47,124 through 598,880_toggle 828,303 through 979,770_turn off 174,272 through 280,311_turn off 540,50 through 880,212_turn on 141,994 through 221,998_turn on 476,695 through 483,901_turn on 960,216 through 972,502_toggle 752,335 through 957,733_turn off 419,713 through 537,998_toggle 772,846 through 994,888_turn on 881,159 through 902,312_turn off 537,651 through 641,816_toggle 561,947 through 638,965_turn on 368,458 through 437,612_turn on 290,149 through 705,919_turn on 711,918 through 974,945_toggle 916,242 through 926,786_toggle 522,272 through 773,314_turn on 432,897 through 440,954_turn off 132,169 through 775,380_toggle 52,205 through 693,747_toggle 926,309 through 976,669_turn off 838,342 through 938,444_turn on 144,431 through 260,951_toggle 780,318 through 975,495_turn off 185,412 through 796,541_turn on 879,548 through 892,860_turn on 294,132 through 460,338_turn on 823,500 through 899,529_turn off 225,603 through 483,920_toggle 717,493 through 930,875_toggle 534,948 through 599,968_turn on 522,730 through 968,950_turn off 102,229 through 674,529"
    inputCommands = inputString.split('_')
    puzzleNumber6 = input('Enter the puzzle Number:')
    print(puzzleNumber6)
    for commandString in inputCommands:
        command = re.search("([a-z]*.[a-z]*)", commandString)
        beginningCoor = re.search("([0-9]*,[0-9]*)", commandString)
        endCoor = re.search("through ([0-9]*,[0-9]*)", commandString)
        begCoorArray = beginningCoor.group(0).split(',');
        endCoorArray = endCoor.group(1).split(',');

        XRange = list(range(int(begCoorArray[0]), int(endCoorArray[0])+1))
        YRange = list(range(int(begCoorArray[1]), int(endCoorArray[1])+1))
        for x in XRange:
            for y in YRange:

                if command.group(0) == 'turn on':
                    if puzzleNumber6 == '1':
                        lightArray[x][y] = 1
                    if puzzleNumber6 == '2':
                        lightArray[x][y] = lightArray[x][y]+1
                if command.group(0) == 'turn off':
                    if puzzleNumber6 == '1':
                        lightArray[x][y] = 0
                    if puzzleNumber6 == '2':
                        lightArray[x][y] = lightArray[x][y]-1
                        if(lightArray[x][y] < 0):
                            lightArray[x][y] = 0
                if command.group(0) == 'toggle ':
                    if puzzleNumber6 == '1':
                        if lightArray[x][y] == 1:
                            lightArray[x][y] = 0
                        else:
                            lightArray[x][y] = 1
                    if puzzleNumber6 == '2':
                        lightArray[x][y] = lightArray[x][y]+2


    TurnedOnLights = 0;
    TotalBrightness = 0
    for x in lightArray:
        for y in lightArray[x]:
            if puzzleNumber6 == '1' and lightArray[x][y] == 1:
                TurnedOnLights = TurnedOnLights+1
            elif puzzleNumber6 == '2':
                TotalBrightness = TotalBrightness+lightArray[x][y]
    print('Number of Turned on Lights:'+str(TurnedOnLights))
    print('Total birghtness:'+str(TotalBrightness))
main()
