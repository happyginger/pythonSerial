'''
Created on 2014年10月30日

@author: Winter
'''
from binascii import hexlify, unhexlify

def formatPortSettins(settings):
    assert type(settings) is dict
    try:
        settings["baund"] = int(settings.get("baund", 9600))
        settings["bytesize"] = int(settings.get("bytesize", 8))
        settings["stopbits"] = int(settings.get("stopbits", 1))
    except Exception, msg:
        return False, msg
    
    return True, "success"
        
def checkData(data, _type):
    if data == '':
        return False, u"数据不能为空"

    errch, msg = None, "success"
    if _type == "hex":
        data = ''.join(data.split())
        if len(data) % 2 != 0:
            errch, msg = True, u"HEX模式下，数据长度必须为偶数"
        else:
            for ch in data.upper():
                if not ('0' <= ch <= '9' or 'A' <= ch <= 'F'):
                    errch, msg = ch, u"数据中含有非法的HEX字符"
                    break
                    
    return not errch, msg

toVisualHex = lambda data: ' '.join([hexlify(c) for c in data]).upper()
toHex = lambda data: ''.join([unhexlify(data[i:i+2]) for i in xrange(0, len(data), 2)])