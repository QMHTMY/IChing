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
  '111111':['乾  ','一    '],'000000':['坤  ','二    '],
  '010001':['屯  ','三    '],'100010':['蒙  ','四    '],
  '010111':['需  ','五    '],'111010':['颂  ','六    '],
  '000010':['师  ','七    '],'010000':['比  ','八    '],
  '110111':['小畜','九    '],'111011':['履  ','十    '],
  '000111':['泰  ','十一  '],'111000':['否  ','十二  '],
  '111101':['同人','十三  '],'101111':['大有','十四  '],
  '000100':['谦  ','十五  '],'001000':['豫  ','十六  '],
  '011001':['随  ','十七  '],'100110':['蛊  ','十八  '],
  '000011':['临  ','十九  '],'110000':['观  ','二十  '],
  '101001':['噬嗑','二十一'],'100101':['贲  ','二十二'],
  '100000':['剥  ','二十三'],'000001':['复  ','二十四'],
  '111001':['无妄','二十五'],'100111':['大畜','二十六'],
  '100001':['颐  ','二十七'],'011110':['大过','二十八'],
  '010010':['坎  ','二十九'],'101101':['离  ','三十  '],
  '011100':['咸  ','三十一'],'001110':['恒  ','三十二'],
  '111100':['遁  ','三十三'],'001111':['大壮','三十四'],
  '101000':['晋  ','三十五'],'000101':['明夷','三十六'],
  '110101':['家人','三十七'],'101011':['睽  ','三十八'],
  '010100':['蹇  ','三十九'],'001010':['解  ','四十  '],
  '100011':['损  ','四十一'],'110001':['益  ','四十二'],
  '011111':['夬  ','四十三'],'111110':['姤  ','四十四'],
  '011000':['萃  ','四十五'],'000110':['升  ','四十六'],
  '011010':['困  ','四十七'],'010110':['井  ','四十八'],
  '011101':['革  ','四十九'],'101110':['鼎  ','五十  '],
  '001001':['震  ','五十一'],'100100':['艮  ','五十二'],
  '110100':['渐  ','五十三'],'001011':['归妹','五十四'],
  '001101':['丰  ','五十五'],'101100':['旅  ','五十六'],
  '110110':['巽  ','五十七'],'011011':['兑  ','五十八'],
  '110010':['涣  ','五十九'],'010011':['节  ','六十  '],
  '110011':['中孚','六十一'],'001100':['小过','六十二'],
  '010101':['既济','六十三'],'101010':['未济','六十四']
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

    name = gNames[gname]
    print("挂名: "+name[0].strip()+'挂'+name[1])

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
