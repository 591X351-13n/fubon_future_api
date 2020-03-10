import win32event
import win32com
from xmltodict import parse as xmlParser
import fubon_api
from getpass import getpass

# Product ID
mMTX = 'MXFC0'  # mini-Taiwan Stock Index


def queryParser(retTuple):
    retVal, xmlStr = retTuple
    if retVal >= 0:
        xmlDict = xmlParser(xmlStr)
    else:
        raise Exception
    return xmlDict['Result']['Data']


class FutureProduct:
    def __init__(self, miscDict):
        self.ProductType = miscDict['@ProductType']  # 0: Future, 1: Stock
        self.CommID      = miscDict['@CommID']       # Product ID
        self.CommName    = miscDict['@CommName']     # Product Name
        self.BS          = miscDict['@BS']           # B: Buy, S: Sold
        self.Price       = miscDict['@Price']
        self.AvgPrice    = miscDict['@AvgPrice']

        self.Qty = 0
        self.Gain = 0
        self.Deposit = 0
        self.Cost = 0


class FutureOrder:
    def __init__(self, miscDict):
        self.AID        = miscDict['@AID']
        self.TDate      = miscDict['@TDate']        # Trade Date
        self.OID        = miscDict['@OID']          # Order ID (serial)
        self.OrderNo    = miscDict['@OrderNo']      # Order Number

        self.Cond       = miscDict['@Cond']         # Order Condition (R: ROD, F: FOK, I: IOC)
        self.PriceType  = miscDict['@PriceType']    # Price Condition (0: limited, 4: market, 24: range market price)
        self.Offset     = miscDict['@Offset']       # Order Type (0: new, 1: close out, 2: auto, 4: day trade)
        self.Qoriginal  = miscDict['@Qoriginal']    # Original order Qty
        self.Qcurrent   = miscDict['@Qcurrent']     # Current order Qty
        self.Qmatched   = miscDict['@Qmatched']     # Done (matched) Qty
        self.CanModify  = miscDict['@CanModify']    # Order modify-able (Y/N)
        self.CanCancel  = miscDict['@CanCancel']    # Order cancel-able (Y/N)

        self.StateMsg   = miscDict['@StateMsg']     # Order state

        self.Closed     = miscDict['@Closed']
        self.Product = FutureProduct(miscDict)


class FubonAccount:
    def __init__(self, miscDict):
        self.FBID       = miscDict['@FBID']         # Dealer (Merchant) code
        self.BID        = miscDict['@BID']          # Dealer branch code
        self.AID        = miscDict['@AID']          # User Account
        self.Key        = miscDict['@Key']          # User Key
        self.DispAID    = miscDict['@Disp-aid']     # UI-display account
        self.MsgKey     = miscDict['@MsgKey']       # Request key (account)
        self.MsgServer  = miscDict['@MsgServerID']  # Request server

        self.StockHolding = {}
        self.FutureHolding = {}


class FubonQuote:
    def __init__(self, dllHolder, ID, PWD):
        self.dllHolder = dllHolder
        self.ID = ID
        self.PWD = PWD
        self.Name = None
        self.UID = None
        self.AuthKey = None
        self.StockAccount = None
        self.FutureAccount = None

        self.login()

    def login(self):
        xmlDict = queryParser(self.dllHolder.eLogin(self.ID, self.PWD, ""))
        self.Name = xmlDict['Global']['Name']
        self.UID = xmlDict['Global']['UID']
        self.AuthKey = xmlDict['Global']['AuthKey']

        self.StockAccount = FubonAccount(xmlDict['Row'][0])
        self.FutureAccount = FubonAccount(xmlDict['Row'][1])

        print('Fubon Quote Login Success !!')

    def logout(self):
        self.dllHolder.eLogout()
        print('Fubon Qoute Logout Success !!')

    def querySelfOpenInt(self):
        _dict = queryParser(self.dllHolder.efPosition(self.FutureAccount.MsgKey, ""))
        if not _dict:
            pass
        else:
            pass

    def querySelfOrder(self):
        _dict = queryParser(self.dllHolder.efQueryAll(self.FutureAccount.MsgKey, ""))
        if not _dict:
            pass
        else:
            rspList = _dict['Row']
            self.order = []
            for rsp in rspList:
                self.order.append(FutureOrder(rsp))
            pass


if __name__ == '__main__':
    dll = win32com.client.Dispatch('{60F749A4-6180-42BA-B9A3-5F2F657809DC}')
    id = getpass('ID: ')
    pwd = getpass('Password: ')
    FBQ = FubonQuote(dll, id, pwd)
    FBQ.querySelfOpenInt()
    FBQ.querySelfOrder()
    FBQ.logout()
