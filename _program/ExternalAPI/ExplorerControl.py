import requests

class explorerControl:
    def __init__(self, url:str, api:str) -> None:
        #Scanのurlとapiをインスタンスに格納
        self.url = url
        self.api = api

    def setAddress(self, address:str) -> None:
        #アドレスをインスタンスに格納
        self.address = address

    def normalTransactions(self, startBlock:int, endBlock:int):
        #リクエストURLを構成
        request = 'https://' + self.url + '/api?module=account&action=txlist' + \
            '&address=' + self.address + \
            '&startblock=' + str(startBlock) + '&endblock=' + str(endBlock) + \
            '&sort=asc&apikey=' + self.api

        #リクエストを送信，返す
        return requests.get(request).json()

    def internalTransactions(self, startBlock:int, endBlock:int):
        #リクエストURLを構成
        request = 'https://' + self.url + '/api?module=account&action=txlistinternal' + \
            '&address=' + self.address + \
            '&startblock=' + str(startBlock) + '&endblock=' + str(endBlock) + \
            '&sort=asc&apikey=' + self.api
        
        #リクエストを送信，返す
        return requests.get(request).json()

    def tokenTransactions(self, startBlock:int, endBlock:int):
        #リクエストURLを構成
        request = 'https://' + self.url + '/api?module=account&action=tokentx' + \
            '&address=' + self.address + \
            '&startblock=' + str(startBlock) + '&endblock=' + str(endBlock) + \
            '&sort=asc&apikey=' + self.api

        #リクエストを送信，返す
        return requests.get(request).json()

    def tokennfttxTransactions(self, startBlock:int, endBlock:int):
        #リクエストURLを構成
        request = 'https://' + self.url + '/api?module=account&action=tokennfttx' + \
            '&address=' + self.address + \
            '&startblock=' + str(startBlock) + '&endblock=' + str(endBlock) + \
            '&sort=asc&apikey=' + self.api
        
        #リクエストを送信，返す
        return requests.get(request).json()

    def contractAbi(self, contractAddress:str):
        #リクエストURLを構成
        request = 'https://' + self.url + '/api?module=contract&action=getabi' + \
            '&address=' + contractAddress + \
            '&apikey=' + self.api
    
        #リクエストを送信，返す
        return requests.get(request).json()

    def getTransaction(self, hash:str):
        #リクエストURLを構成
        request = 'https://' + self.url + '/api?module=proxy&action=eth_getTransactionByHash' + \
            '&txhash=' + hash + '&apikey=' + self.api

        #リクエストを送信，返す
        return requests.get(request).json()