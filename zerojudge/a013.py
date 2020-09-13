while True:
    try:
        temp = input()

        roman1 = temp.split(" ")[0]
        roman2 = temp.split(" ")[1]
        num1 = 0
        num2 = 0

        dic = {"M":1000,"CM":900,"D":500,"CD":400,"C":100,"XC":90,"L":50,"XL":40,"X":10,"IX":9,"V":5,"IV":4,"I":1}

        #羅馬轉數字
        while len(roman1) > 0 :
            if len(roman1) >= 2 and roman1[0]+roman1[1] in dic.keys() :
                num1 += dic[roman1[0]+roman1[1]]
                roman1 = roman1.replace(roman1[0]+roman1[1],"",1)
            elif roman1[0] in dic.keys() :
                num1 += dic[roman1[0]]
                roman1 = roman1.replace(roman1[0],"",1)

        while len(roman2) > 0 :
            if len(roman2) >= 2 and roman2[0]+roman2[1] in dic.keys() :
                num2 += dic[roman2[0]+roman2[1]]
                roman2 = roman2.replace(roman2[0]+roman2[1],"",1)
            elif roman2[0] in dic.keys() :
                num2 += dic[roman2[0]]
                roman2 = roman2.replace(roman2[0],"",1)

        #相減,取絕對值
        num = abs(num1 - num2)

        #數字轉羅馬
        i = 0
        roman = ""

        while num > 0 :
            if num >= list(dic.values())[i] :
                num = num - list(dic.values())[i]
                roman += list(dic.keys())[i]
            if num < list(dic.values())[i] :
                i += 1

        if roman == "" :
            roman = "ZERO"

        print(roman)

    except:
        break
