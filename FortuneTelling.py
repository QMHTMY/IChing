#!/usr/bin/python3
#coding: utf-8
#周易算卦程序
#2020.03.04
#Shieber

#大衍之数55=1+2+3+4+5++6+7+8+9+10
#周易算卦取50或55根蓍草为起始，后代取棋子，本程序直接用数字模拟
'''
    算法流程
    第零步：将50/55去掉部分，只留下49，代表总数。
    循环3次 第一步：将总数随机分为两数和，代表天和地，可称为天数和地数(例如13,36)。
      ^     第二步：将地数减1，这个1代表人数，合称天地人三才。
      |     第三步：1.将天数除以4，得到余数rem(可能是0,1,2,3)
      |             2.余数rem为0时，
      |               若天数大于等于4，则将余数rem改为4
      |               若天数为0，则余数rem仍为0
      |             3.将天数减去余数
      |     第四步：1.将地数除以4，得到余数rem(可能是0,1,2,3)
      |             2.余数rem为0时，
      |               若地数大于等于4，则将余数rem改为4
      |               若地数为0，则余数rem仍为0
      |             3.将地数减去余数
      |     第五步：将人数和第三四步中的余数加起来。
      |--<--第六步：将天/地数相加得到新总数，回到第一步。
'''
from random import seed, randint

#64挂名
gNames = {
    '111111':'乾','000000':'坤','010001':'屯','100010':'蒙',
    '010111':'需','111010':'颂','000010':'师','010000':'比',
    '110111':'小 畜','111011':'履','000111':'泰','111000':'否',
    '111101':'同人','101111':'大有','000100':'谦','001000':'豫',
    '011001':'随','100110':'蛊','000011':'临','110000':'观',
    '101001':'噬嗑','100101':'贲','100000':'剥','000001':'复',
    '111001':'无妄','100111':'大畜','100001':'颐','011110':'大过',
    '010010':'坎','101101':'离','011100':'咸','001110':'恒',
    '111100':'遁','001111':'大壮','101000':'晋','000101':'明夷',
    '110101':'家人','101011':'睽','010100':'蹇','001010':'解',
    '100011':'损','110001':'益','011111':'夬','111110':'姤',
    '011000':'萃','000110':'升','011010':'困','010110':'井',
    '011101':'革','101110':'鼎','001001':'震','100100':'艮',
    '110100':'渐','001011':'归妹','001101':'丰','101100':'旅',
    '110110':'巽','011011':'兑','110010':'涣','010011':'节',
    '110011':'中孚','001100':'小过','010101':'既济','101010':'未济'
    }

class ChouYi():
    def __init__(self):
        self.totalNum  = 50-1 #大衍数，必须写成50-1/55-6
        self.heavenNum = 0    #0为天数 爻变
        self.earthNum  = 0    #0为地数 爻变
        self.peopleNum = 1    #1为人数 不变
        self.remainNum = 0    #0为余数 爻变

    def getTianDiNum(self, totalNum):
        self.heavenNum = randint(0, totalNum - self.peopleNum) 
        self.earthNum  = totalNum - self.heavenNum 
        self.earthNum  -= self.peopleNum 

    def newTianDiNum(self, TianDiNum):
        rem = TianDiNum % 4
        if 0 == rem and TianDiNum>= 4:
            rem = 4
        return rem
    
    def YaoChange(self):
        #3次爻变
        for change in range(3):
            self.getTianDiNum(self.totalNum)
            rem1 = self.newTianDiNum(self.heavenNum)
            rem2 = self.newTianDiNum(self.earthNum)
            self.remainNum = rem1 + rem2 + self.peopleNum
            self.totalNum  = self.heavenNum - rem1 + self.earthNum - rem2

    def YaoNum(self):
        self.YaoChange()
        yaoNum = int(self.totalNum/4)
        return yaoNum 

def showGua(yaoNums):
    gua = []
    gname = ''
    for num in yaoNums:
        if num % 2:
            yao = '---'
            gname += '1'
        else:
            yao = '- -'
            gname += '0'
       
        if 6 == num or 7 == num:
            cyao = '---'
        if 9 == num or 8 == num: 
            cyao = '- -'
        gua.append((str(num), yao, cyao))

    print("挂名: "+gNames[gname]+'挂')
    for i in range(len(gua)):
        print(' '+gua[i][0]+'   '+gua[i][1]+'  '+gua[i][2]) 
    print("爻数 本挂 变挂")

if __name__ == "__main__":
    yaoNums = []
    for yao in range(6):
        chouyi = ChouYi()
        yaonum = chouyi.YaoNum()
        yaoNums.insert(0, yaonum)
    showGua(yaoNums)
