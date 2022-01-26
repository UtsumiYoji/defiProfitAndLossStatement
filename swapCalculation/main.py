from __future__ import print_function


class swapCalculation:
    def __init__(self) -> None:
        self.amount = {}
        self.averageCost = {}

    def addAmount(self, cryptoName:str, amount:float, averageCost:float):
        # 初めて扱う通貨なら0残高を追加
        if not cryptoName in self.amount.keys():
            self.amount[cryptoName] = 0

        # 平均取得単価に追加
        if cryptoName in self.averageCost.keys():
            self.averageCost[cryptoName] = \
                ((self.averageCost[cryptoName] * self.amount[cryptoName]) + (averageCost * amount)) / (self.amount[cryptoName] + amount)
        else:
            self.averageCost[cryptoName] = averageCost

        # 残高を追加
        self.amount[cryptoName] += amount

    def addSwapData(self, beforeCryptoName, beforeCryptoAmount, afterCryptoName, afterCryptoAmount, afterCryptoPrice):
        # 初めて扱う通貨なら残高を追加
        if not afterCryptoName in self.amount.keys():
            self.amount[afterCryptoName] = 0

        # スワップ後の通貨について平均取得単価を更新する
        if afterCryptoName in self.averageCost.keys():
            self.averageCost[afterCryptoName] = \
                ((self.averageCost[afterCryptoName] * self.amount[afterCryptoName]) + (afterCryptoPrice * afterCryptoAmount)) / (afterCryptoAmount + self.amount[afterCryptoName])
        else:
            self.averageCost[afterCryptoName] = afterCryptoPrice
        
        # スワップ前後それぞれの量を残高に追加する
        self.amount[beforeCryptoName] -= beforeCryptoAmount
        self.amount[afterCryptoName] += afterCryptoAmount

        # 取引の内容について表示する
        print('スワップ前：' + beforeCryptoName + ' ' + beforeCryptoAmount + '枚（平均取得単価：' + self.averageCost[beforeCryptoName] + '）')
        print('スワップ後：' + afterCryptoName + ' ' + afterCryptoAmount + '枚購入')
        print('損益計算：' + str(round((afterCryptoAmount*afterCryptoPrice) - (self.averageCost[beforeCryptoName]*beforeCryptoAmount), 5)) + 'の損益\n')
