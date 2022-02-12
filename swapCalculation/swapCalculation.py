import profile


class swapCalculation:
    def __init__(self) -> None:
        self.amount = {}
        self.averageCost = {}
        self.profit = 0
        self.LPamount = {}
        self.LPaverageCost = {}

    def addAmount(self, cryptoName:str, amount:float, averageCost:float):
        # 平均取得単価に追加
        if cryptoName in self.averageCost.keys():
            self.averageCost[cryptoName] = \
                ((self.averageCost[cryptoName] * self.amount[cryptoName]) + (averageCost * amount)) / (self.amount[cryptoName] + amount)
        else:
            # 初めて取り扱う通貨
            self.averageCost[cryptoName] = averageCost
            self.amount[cryptoName] = 0

        # 残高を追加
        self.amount[cryptoName] += amount

    def addSwapData(self, beforeCryptoName, beforeCryptoAmount, afterCryptoName, afterCryptoAmount, afterCryptoPrice):
        # スワップ後の通貨について平均取得単価を更新する
        if afterCryptoName in self.averageCost.keys():
            self.averageCost[afterCryptoName] = \
                ((self.averageCost[afterCryptoName] * self.amount[afterCryptoName]) + (afterCryptoPrice * afterCryptoAmount)) / (afterCryptoAmount + self.amount[afterCryptoName])
        else:
            # 初めて取り扱う通貨
            self.averageCost[afterCryptoName] = afterCryptoPrice / afterCryptoAmount
            self.amount[afterCryptoName] = 0
        
        # スワップ前後それぞれの量を残高に追加する
        self.amount[beforeCryptoName] -= beforeCryptoAmount
        self.amount[afterCryptoName] += afterCryptoAmount

        # 取引の内容について表示する
        print('スワップ前：' + beforeCryptoName + ' ' + str(beforeCryptoAmount) + '枚（平均取得単価：' + str(self.averageCost[beforeCryptoName]) + '）')
        print('スワップ後：' + afterCryptoName + ' ' + str(afterCryptoAmount) + '枚購入')
        print('損益計算：' + str(round((afterCryptoAmount*afterCryptoPrice) - (self.averageCost[beforeCryptoName]*beforeCryptoAmount), 5)) + 'の損益\n')

        self.profit += ((afterCryptoAmount*afterCryptoPrice) - (self.averageCost[beforeCryptoName]*beforeCryptoAmount))
    
    def makeLP(self, LPamount, cryptoList:list):
        '''
        cryptoList変数は2次元配列(nx3)とする
        [[取引通貨名1, 通貨名1価格, 取引通貨1量], [取引通貨名2, 通貨名2価格, 取引通貨2量], ...]
        '''

        # 変数初期化
        LPprice = 0
        LPname = []
        
        # LP作成に使った仮想通貨の数だけループ
        for i in range(len(cryptoList)):
            # LPの値段の計算
            crypto = cryptoList[i]
            LPprice += (crypto[1] * crypto[2])

            # LPの名前の作成
            LPname.append(crypto[0])  

            # LP作成前後の所持量を変更
            self.amount[crypto[0]] -= cryptoList[2]

            # 損益について計算する
            profit = ((crypto[1]*crypto[2]) - (self.averageCost[crypto[0]]*crypto[2]))
            self.profit += profit
            print(crypto[0] + '(平均取得単価:' + self.averageCost[crypto[0]] + ')を' + crypto[2] + '枚使用、' + profit + 'の損益')

        # LP組み合わせの文字列を作成
        LPname = ','.join(LPname.sort())

        # 平均取得単価についてを更新する
        if LPname in self.LPamount:
            self.LPaverageCost[LPname] = ((self.LPaverageCost[LPname] * self.LPamount) + (LPprice * LPamount)) / (self.LPamount + LPamount)
        else:
            # 初めて取り扱う通貨
            self.LPaverageCost[LPname] = LPprice / LPamount
            self.LPamount[LPname] = 0
            
    def releaseLP(self, LPamount, cryptoList:list):
        '''
        cryptoList変数は2次元配列(nx3)とする
        [[取引通貨名1, 通貨名1価格, 取引通貨1量], [取引通貨名2, 通貨名2価格, 取引通貨2量], ...]
        '''
        # 変数初期化
        take = 0
        LPname = []
        
        # LP作成に使った仮想通貨の数だけループ
        for i in range(len(cryptoList)):
            # LPの値段の計算
            crypto = cryptoList[i]

            # LPの名前の作成
            LPname.append(crypto[0])  

            # 解除後の通貨を保持量に追加
            self.addAmount(crypto[0], crypto[2], crypto[1])

            # 解除後に得た金額
            take += (crypto[1] * crypto[2])
        
        # LP組み合わせの文字列を作成
        LPname = ','.join(LPname.sort())

        # LPの保持量を変更
        self.LPamount -= LPamount

        # 損益を計算
        profit = (take - (self.LPaverageCost[LPname] * LPamount))
        print(LPname + 'のLP(平均取得単価:' + self.LPaverageCost[LPname] + ')を' + LPamount + '枚使用、' + profit + 'の損益')
