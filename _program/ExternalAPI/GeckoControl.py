import json
import pycoingecko

class GeckoControl:
    #コンストラクタ
    def __init__(self):
        self.GecIns = pycoingecko.CoinGeckoAPI()

    #対応チェーンjsonを吐き出す関数
    def ReloadChain(self):
        #GeckoのAPIを叩く
        data = self.GecIns.get_asset_platforms()

        #ファイルの上書き保存
        with open('./GeckoChain.json', 'w') as file:
            json.dump(data, file, indent=4)

    #チェーンを設定する関数
    def SetChain(self, ChainName):
        self.Chain = ChainName
    
    #価格データを取り出す関数
    def GetPrice(self, ContAd, TimeStamp):
        #GeckoのAPIをたたく
        data = self.GecIns.get_coin_market_chart_range_from_contract_address_by_id(
            id = self.Chain,
            contract_address=ContAd,
            vs_currency = 'jpy',
            from_timestamp = str(TimeStamp),
            to_timestamp = str(TimeStamp+5000)
        )

        #価格データだけ取り出す
        result = data['prices'][0][1]
        return result
