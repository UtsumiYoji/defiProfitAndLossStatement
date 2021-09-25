import openpyxl

class ExcelControl:
    def __init__(self) -> None:
        #ブックを開く
        self.wbAll = openpyxl.open('./ExcelPackage/ExcelTemplate/TransactionHistory.xlsx')
        self.wbOne = openpyxl.open('./ExcelPackage/ExcelTemplate/TransactionHistory.xlsx')
        self.wbTwo = openpyxl.open('./ExcelPackage/ExcelTemplate/TransactionHistory.xlsx')
        self.wbMul = openpyxl.open('./ExcelPackage/ExcelTemplate/TransactionHistory.xlsx')
    
        #シート
        self.shAll = self.wbAll['Template']
        self.shOne = self.wbOne['Template']
        self.shTwo = self.wbTwo['Template']
        self.shMul = self.wbMul['Template']

    def __del__(self) -> None:
        #保存
        self.wbAll.save('./Result/AllTx.xlsx')
        self.wbOne.save('./Result/SingleTx.xlsx')
        self.wbTwo.save('./Result/DoubleTx.xlsx')
        self.wbMul.save('./Result/MultiTx.xlsx')

        #クローズ
        self.wbAll.close()
        self.wbOne.close()
        self.wbTwo.close()
        self.wbMul.close()

    def Write(self, sh, data):
        #書き込む行(一番した)を定義
        row = sh.max_row + 1

        #書き込み
        for i in range(len(data)):
            sh.cell(row, i+1).value = data[i]

    def ExportTransaction(self, data:list) -> None:
        #Hashとチェーン名をくっつけたリストを作成
        HashList = [i[0]+i[2] for i in data]

        #取り出しデータの内部のデータ数分だけループ
        i = 0
        while (i < len(data)):
            #同じブロックidで何個履歴が残ってるか計算
            num = HashList.count(data[i][0]+data[i][2])

            #1個しか履歴がない場合
            if num == 1:
                self.Write(self.shOne, data[i])
            
            #2個しか履歴がない場合
            elif num == 2:
                self.Write(self.shTwo, data[i])
                self.Write(self.shTwo, data[i+1])

            #3個しか履歴がない場合
            else:
                for j in range(num):
                    self.Write(self.shMul, data[i+j])
            i += num
        
        #すべてのデータを一つのデータとしても出力
        for i in range(len(data)):
            self.Write(self.shAll, data[i])
