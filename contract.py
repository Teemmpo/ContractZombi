
'''
https://bscscan.com/address/0xe9e7cea3dedca5984780bafc599bd69add087d56#readContract

https://eth.wiki/json-rpc/API

https://medium.com/@takahirookada/handle-smart-contract-on-ethereum-with-arduino-or-esp32-1bb5cbaddbf4
https://github.com/kopanitsa/web3-arduino
https://github.com/kopanitsa/web3-arduino/blob/master/src/Contract.cpp
https://dzone.com/articles/signing-and-verifying-ethereum-signatures#:~:text=Accounts%20can%20use%20their%20private,was%20signed%20by%20the%20signer.

https://ethereum.stackexchange.com/questions/1777/workflow-on-signing-a-string-with-private-key-followed-by-signature-verificatio


crear wallet
https://github.com/ludbb/secp256k1-py

'''

import web3
from web3 import Web3

class Contract:
    privateKey= []
    def __init__(self,_web3,address):
        self.web3= _web3
        self.contractAddress= address

    def str2hex(self,funtion):
        #https://python-forum.io/thread-3058.html
        return ''.join([('0'+hex(ord(c)).split('x')[1])[-2:] for c in funtion])

    def GenerateContractBytes(self,data):
        inn = "0x"
        ar=""
        cero='00000000'
        for i in data:
            a=hex(ord(i))
            #print(a)            
            ar= ar+ a[2:]
        inn= inn+ ar
        #print((inn))
        re= self.web3.sha3(inn)

        #"".join(str(ord(char)) for i in range(0,128))
        return re
    def Call(self,fron,to,gas,gasPrice,value,data):

        result= self.web3.EthCall(fron,to,gas,gasPrice,value,data)

    def GenerateBytesForUint(self,value):
        digits= len(str(value))
        cero="".join(str(0) for i in range(0,2+64-digits))
        h= "".join((int(i,16))[2:] for i in str(value))
        return cero, h # len(cero)+ len(h)

    def SetupContractData(self,funtion): 
        contractBytes= self.GenerateContractBytes(funtion)
        return contractBytes
    
    def SetPrivateKey(self,key):
        self.privateKey.append(key)

'''
web3= Web3("https://bsc-dataseed.binance.org/") 
contract_address = '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'
contract= Contract(web3,contract_address)
funtion= contract.SetupContractData('set(uint256)')
#call= funtion
#contract.call()
print((contract.GenerateBytesForUint(1200000000)))
'''

web3= Web3("https://bsc-dataseed.binance.org/") 
contract_address = '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'
contract= Contract(web3,contract_address)
#print(contract.GenerateContractBytes('baz(uint32 x, bool y)'))

'''

s = "baz(uint32,bool)"
a= "".join("{:04x}".format(ord(c)) for c in s)
print(a)
print()

a= ''.join(hex(ord(x))[2:] for x in 'baz(uint32,bool)')
a= '0x'+a
print(a,web3.sha3(a)['result'][0:10])

web3.sha3(a)

valor= 69
valor= hex(valor)[2:]
print(valor)

x= len(str(valor))
e= ""
for i in range(0,64-x):
    e=e+"0"
e=e+valor
print(e)


#def convertUint32(val):
'''


fron= "0xE512D04E883091Dba1E05b74Fef584CD76c549ad"
contrac= '0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56'
function= 'symbol()' # symbol , name , totalSupply , getOwner
a= ''.join(hex(ord(x))[2:] for x in function)
a= '0x'+a
sha= web3.sha3(a)['result'][0:10]
#print(a,sha)

def EthGasPrice(contrac,fron,sha):
    m = "eth_call"
    p= [{"to": contrac, "data":sha}, "latest"]
    js= web3.generateJson(m,p)
    #print(js)
    return web3.post(js)
# '{"jsonrpc":"2.0", "method":"eth_call", "params":[{"to": "0xb82020341122e7c8c4ba6551fd25950681af3570", "data": "0x0127efc5"}, "latest"], "id":1}'
#print(EthGasPrice(contrac,fron,sha))

qwe= EthGasPrice(contrac,fron,sha)['result'][:]
print(qwe)
qwe= EthGasPrice(contrac,fron,sha)['result'][2:]
print(qwe)
'''
q=''
ar=[]
count=1
for i in range(0,len(qwe)):
    #print(qwe[i]) 
    if count<=63:
        q=q+qwe[i]
        count+=1
    else:
        ar.append(q)
        count=1
        q=''
print(ar)
'''

'''
q=''
ar=[]
for i in range(1,len(qwe)+1):
    if i%65==0:        
        ar.append(q)
        q=''
    else:
        q=q+qwe[i-1]     
print(ar)
'''
print(len(qwe))
for i in range(0,int(len(qwe)/64)):
    print(qwe[i*64:(i+1)*64])









'''
string = EthGasPrice(contrac,fron,sha)['result'][2:]
print(int(string, 16))
print("".join(chr(int(string[i], 16)) for i in range(0,len(string))))
'''


'''
0000000000000000000000000000000000000000000000000000000000000020
000000000000000000000000000000000000000000000000000000000000000a
4255534420546f6b656e00000000000000000000000000000000000000000000

0000000000000000000000000000000000000000000000000000000000000020
000000000000000000000000000000000000000000000000000000000000000a
4255534420546f6b656e00000000000000000000000000000000000000000000

'''