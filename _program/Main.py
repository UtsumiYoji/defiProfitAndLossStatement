import json
from ExternalAPI import ExplorerControl

class Main:

    def __init__(self):
        #設定ファイルの読み来い
        self.setting = json.load(open('./setting.json', 'r'))

    def main(self):
        #アドレスの入力
        print('計算処理したいアドレスを入力してネ！')
        address = input('>>>')

        #各種インスタンスを作成
        explorerIns = {}
        for key in self.setting.keys():
            #辞書にインスタンスを追加
            explorerIns[key] = ExplorerControl.ExplorerControl(
                self.setting[key]['scanUrl'],
                self.setting[key]['scanApi'],
            )

            #アドレスを設定
            explorerIns[key].setAddress(address)

        #チェーンの数ループ
        for key in explorerIns.keys():
            normalTx = explorerIns[key].normalTransactions(0, 99999999)
            print(normalTx)

Main().main()

#テストに使えそうなトランザクション沢山あるアドレス
#0x8894E0a0c962CB723c1976a4421c95949bE2D4E3

#自分のアドレス
#0x306C2A0beD3Aaf28D4CeA4da2CfCEC9CC50E6119