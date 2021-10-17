from ExternalAPI import explorerControl

class transactionConnection:

    def __init__(self):
        self.transaction = list()
        self.errorGas = list()

    def dataProcessing(self, data, symbol, contract, value):
        if data['isError'] == '1':
            # エラーだったらガス代だけ取得
            self.errorGas += [
                data['blockNumber'], data['timeStamp'], data['hash'],
                data['gas'], data['gasPrice'],
            ]

        else:
            # エラーじゃないならデータに追加
            self.transaction += [
                data['blockNumber'], data['timeStamp'], data['hash'], data['from'],
                data['to'], value, symbol, contract,
            ]

    def expantion(self, address, settingData, sBlock, eBlock):
        # settingからデータを取り出す
        url = settingData['scanUrl']
        api = settingData['scanApi']
        symbol = settingData['symbol']
        contract = settingData['address']

        # スキャンのインタンスを作成
        ins = explorerControl.explorerControl(url=url, api=api)
        ins.setAddress(address=address)

        # ノーマルトランザクションを取得
        normalTx = ins.normalTransactions(sBlock, eBlock)
        if normalTx['message'] == 'OK':
            # データ取得が成功したらデータの数だけループ
            for data in normalTx['result']:
                self.dataProcessing(data, symbol, contract, data['value'])

        # インターナルトランザクションを取得
        internalTX = ins.internalTransactions(sBlock, eBlock)
        if internalTX['message'] == 'OK':
            # データ取得が成功したらデータの数だけループ
            for data in normalTx['result']:
                self.dataProcessing(data, symbol, contract, data['value'])

        # スマートコンストラクトトランザクションを取得
        tokenTx = ins.tokenTransactions(sBlock, eBlock)
        if tokenTx['message'] == 'OK':
            # データ取得が成功したらデータの数だけループ
            for data in tokenTx['result']:
                value = int(data['value']) * (10 ** -int(data['tokenDecimal']))
                self.dataProcessing(data, data['tokenSymbol'], data['contractAddress'], value)

        # NFTデータを取得
        nftTx = ins.tokennfttxTransactions(sBlock, eBlock)
        if nftTx['message'] == 'OK':
            # データ取得が成功したらデータの数だけループ
            for data in nftTx['result']:
                value = int(data['value']) * (10 ** -int(data['tokenDecimal']))
                self.dataProcessing(data, data['tokenSymbol'], data['contractAddress'], value)
