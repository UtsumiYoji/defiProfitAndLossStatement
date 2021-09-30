from ExternalAPI import explorerControl

def expantion(address, settingData, sBlock, eBlock):
    #settingからデータを取り出す
    url = settingData['scanUrl']
    api = settingData['scanApi']
    symbol = settingData['symbol']
    contactAd = settingData['address']
    
    #スキャンのインタンスを作成
    ins = explorerControl.explorerControl(url=url, api=api)
    ins.setAddress(address=address)

    #データを格納する変数
    transaction = list()
    errorGas = list()

    #ノーマルトランザクションを取得
    normalTx = ins.normalTransactions(sBlock, eBlock)
    if normalTx['message'] == 'OK':
        #データ取得が成功したらデータの数だけループ
        for data in normalTx['result']:
            if data['isError'] == '1':
                #エラーだったらガス代だけ取得
                errorGas += [
                    data['blockNumber'], data['timeStamp'], data['hash'], 
                    data['gas'], data['gasPrice'],
                ]

            else:
                #エラーじゃないならデータに追加
                transaction += [
                    data['blockNumber'], data['timeStamp'], data['hash'], data['from'],
                    data['to'], data['value'], symbol, contactAd, 
                ]
    
    #インターナルトランザクションを取得
    internalTX = ins.internalTransactions(sBlock, eBlock)
    if internalTX['message'] == 'OK':
        #データ取得が成功したらデータの数だけループ
        for data in normalTx['result']:
            if data['isError'] == '1':
                #エラーだったらガス代だけ取得
                errorGas += [
                    data['blockNumber'], data['timeStamp'], data['hash'], 
                    data['gas'], data['gasPrice'],
                ]

            else:
                #エラーじゃないならデータに追加
                transaction += [
                    data['blockNumber'], data['timeStamp'], data['hash'], data['from'],
                    data['to'], data['value'], symbol, contactAd, 
                ]
    
    #スマートコンストラクトトランザクションを取得
    tokenTx = ins.tokenTransactions(sBlock, eBlock)
    nftTX = ins.tokennfttxTransactions(sBlock, eBlock)

    