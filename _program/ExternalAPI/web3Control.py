from web3 import Web3, HTTPProvider

class web3Control:
    def __init__(self, url:str) -> None:
        #web3インスタンスを格納
        self.w3 = Web3(HTTPProvider(url))

        #コントラクトインスタンスを格納するための変数
        self.contract = {}

    def readContract(self, address:str, abi:dict):
        self.contract[address] = self.w3.eth.contract(address=address, abi=abi)

    def decodeInputdata(self, inputdata:str, address:str):
        #デコード作業
        result = self.contract[address].decode_function_input(inputdata)

        #結果を返す
        return result