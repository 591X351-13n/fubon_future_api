# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.6.2 |Anaconda custom (64-bit)| (default, Jul 20 2017, 12:30:02) [MSC v.1900 64 bit (AMD64)]
# From type library 'FubonE01API.ocx'
# On Tue Mar 10 22:21:10 2020

# 'FubonE01API'
# makepy_version = '0.5.01'
# python_version = 0x30602f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg = pythoncom.Empty
defaultNamedNotOptArg = pythoncom.Empty
defaultUnnamedArg = pythoncom.Empty

CLSID = IID('{98F7A444-661E-42D3-AAFE-CFE106E020DA}')
MajorVersion = 9
MinorVersion = 3
LibraryFlags = 10
LCID = 0x0

from win32com.client import DispatchBaseClass


class _Fbs_MsgServ2(DispatchBaseClass):
    CLSID = IID('{ABB84942-39DD-40CB-A176-8C508EE59CAD}')
    coclass_clsid = IID('{1A2CEB38-FAB7-434C-B797-D2978FD6908D}')

    def MsgServer_AddMsg(self, bsMsgKey=defaultNamedNotOptArg, Fubon_Mananger=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809349, LCID, 1, (24, 0), ((8, 1), (9, 1)), bsMsgKey
                                         , Fubon_Mananger)

    def MsgServer_Connect(self, Fubon_Mananger=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809347, LCID, 1, (24, 0), ((9, 1),), Fubon_Mananger
                                         )

    def MsgServer_Disconnect(self):
        return self._oleobj_.InvokeTypes(1610809348, LCID, 1, (24, 0), (), )

    def MsgServer_RemoveMsg(self, bsMsgKey=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809350, LCID, 1, (24, 0), ((8, 1),), bsMsgKey
                                         )

    _prop_map_get_ = {
    }
    _prop_map_put_ = {
    }

    def __iter__(self):
        "Return a Python iterator for this object"
        try:
            ob = self._oleobj_.InvokeTypes(-4, LCID, 3, (13, 10), ())
        except pythoncom.error:
            raise TypeError("This object does not support enumeration")
        return win32com.client.util.Iterator(ob, None)


class _Fubon_Mananger_API_2(DispatchBaseClass):
    CLSID = IID('{EF592E6F-0455-4D83-B168-C7D40EA4B899}')
    coclass_clsid = IID('{60F749A4-6180-42BA-B9A3-5F2F657809DC}')

    def AddPreSignData(self, PID=defaultNamedNotOptArg, PWD=defaultNamedNotOptArg, File_=defaultNamedNotOptArg,
                       MessageStr=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809356, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'AddPreSignData', None,
                                 PID
                                 , PWD, File_, MessageStr)

    def CASign(self, strContent=defaultNamedNotOptArg, IDNO=defaultNamedNotOptArg, CAID=defaultNamedNotOptArg,
               CLSID=defaultNamedNotOptArg
               , DataSignature=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809361, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'CASign', None,
                                 strContent
                                 , IDNO, CAID, CLSID, DataSignature)

    def Check_GROUP(self, AID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809363, 1, (3, 0), ((8, 1), (16392, 3)), 'Check_GROUP', None, AID
                                 , MSGXML)

    def Check_ID_ACC(self, MsgKey=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809364, LCID, 1, (3, 0), ((8, 1),), MsgKey
                                         )

    def Check_Login(self, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809362, 1, (3, 0), ((16392, 3),), 'Check_Login', None, MSGXML
                                 )

    def Ekey_AddPreSignData(self, PID=defaultNamedNotOptArg, PWD=defaultNamedNotOptArg, File_=defaultNamedNotOptArg,
                            MessageStr=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809357, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'Ekey_AddPreSignData',
                                 None, PID
                                 , PWD, File_, MessageStr)

    def Find_AID_Count_F(self):
        return self._oleobj_.InvokeTypes(1610809434, LCID, 1, (2, 0), (), )

    def Find_AID_Count_S(self):
        return self._oleobj_.InvokeTypes(1610809435, LCID, 1, (2, 0), (), )

    def Find_AID_by_ID(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809372, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def Find_AID_by_ID_F(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809374, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def Find_AID_by_ID_S(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809373, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def Find_MsgKey_by_ID(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809375, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def Find_MsgKey_by_ID_F(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809377, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def Find_MsgKey_by_ID_S(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809376, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def GetServerTime(self, ServerTime=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809410, 1, (3, 0), ((16392, 3), (16392, 3)), 'GetServerTime', None, ServerTime
                                 , MSGXML)

    def Get_Check_FUTURE_OPEN(self):
        return self._oleobj_.InvokeTypes(1610809345, LCID, 1, (11, 0), (), )

    def Get_Check_Session(self):
        return self._oleobj_.InvokeTypes(1610809346, LCID, 1, (11, 0), (), )

    def Get_Check_TAIEMG_OPEN(self):
        return self._oleobj_.InvokeTypes(1610809464, LCID, 1, (11, 0), (), )

    def Get_Check_TSE_OPEN(self):
        return self._oleobj_.InvokeTypes(1610809344, LCID, 1, (11, 0), (), )

    def SetTopMostWindow(self, hWnd=defaultNamedNotOptArg, Topmost=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809458, 1, (3, 0), ((16387, 3), (16395, 3)), 'SetTopMostWindow', None, hWnd
                                 , Topmost)

    def Set_Trans_Position(self, enable=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809347, LCID, 1, (3, 0), ((11, 1),), enable
                                         )

    def ShowForm(self):
        return self._oleobj_.InvokeTypes(1610809459, LCID, 1, (24, 0), (), )

    def eBill(self, MsgKey_=defaultNamedNotOptArg, stockid=defaultNamedNotOptArg, FromDate=defaultNamedNotOptArg,
              ToDate=defaultNamedNotOptArg
              , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809429, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'eBill', None,
                                 MsgKey_
                                 , stockid, FromDate, ToDate, MSGXML)

    def eDayTrade(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809430, 1, (3, 0), ((8, 1), (16392, 3)), 'eDayTrade', None, MsgKey_
                                 , MSGXML)

    def eLogin(self, login_id=defaultNamedNotOptArg, login_pass=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809385, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eLogin', None, login_id
                                 , login_pass, MSGXML)

    def eLogin_CID(self, CID=defaultNamedNotOptArg, login_id=defaultNamedNotOptArg, login_pass=defaultNamedNotOptArg,
                   MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809383, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'eLogin_CID', None, CID
                                 , login_id, login_pass, MSGXML)

    def eLogin_MsgServ(self, login_id=defaultNamedNotOptArg, login_pass=defaultNamedNotOptArg,
                       ObjMsgServ=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809384, 1, (3, 0), ((8, 1), (8, 1), (9, 1), (16392, 3)), 'eLogin_MsgServ', None,
                                 login_id
                                 , login_pass, ObjMsgServ, MSGXML)

    def eLogin_MsgServ_CID(self, CID=defaultNamedNotOptArg, login_id=defaultNamedNotOptArg,
                           login_pass=defaultNamedNotOptArg, ObjMsgServ=defaultNamedNotOptArg
                           , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809382, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (9, 1), (16392, 3)),
                                 'eLogin_MsgServ_CID', None, CID
                                 , login_id, login_pass, ObjMsgServ, MSGXML)

    def eLogout(self):
        return self._oleobj_.InvokeTypes(1610809378, LCID, 1, (3, 0), (), )

    def eLogout_MsgServ(self, ObjMsgServ=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809379, LCID, 1, (3, 0), ((9, 1),), ObjMsgServ
                                         )

    def eMatch(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809426, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eMatch', None, MsgKey_
                                 , TT, MSGXML)

    def eMatchOne(self, MsgKey_=defaultNamedNotOptArg, OrderNo=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809427, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eMatchOne', None, MsgKey_
                                 , OrderNo, MSGXML)

    def eModifyOrder(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg,
                     OT=defaultNamedNotOptArg
                     , OID=defaultNamedNotOptArg, OrderNo=defaultNamedNotOptArg, stockid=defaultNamedNotOptArg,
                     BS=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg
                     , Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg,
                     MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809439, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'eModifyOrder', None, MsgKey_
                                 , Type_, TT, OT, OID, OrderNo
                                 , stockid, BS, Qty, Qcurrent, Qmatch
                                 , PreOrder, MSGXML)

    def eOrder(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, OT=defaultNamedNotOptArg,
               BS=defaultNamedNotOptArg
               , stockid=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg,
               Price=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809436, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'eOrder',
                                 None, MsgKey_
                                 , TT, OT, BS, stockid, Qty
                                 , PriceType, Price, MSGXML)

    def eOrder2(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, BS=defaultNamedNotOptArg,
                stockid=defaultNamedNotOptArg
                , Qty=defaultNamedNotOptArg, Price=defaultNamedNotOptArg, P10=defaultNamedNotOptArg,
                PayType=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809437, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'eOrder2', None, MsgKey_
                                 , TT, BS, stockid, Qty, Price
                                 , P10, PayType, MSGXML)

    def eQueryAll(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809422, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eQueryAll', None, MsgKey_
                                 , TT, MSGXML)

    def eQueryOne(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID_OrderNo=defaultNamedNotOptArg,
                  MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809421, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'eQueryOne', None, MsgKey_
                                 , Type_, OID_OrderNo, MSGXML)

    def eQueryOrder(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809424, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eQueryOrder', None, MsgKey_
                                 , TT, MSGXML)

    def eRtPosition(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809432, 1, (3, 0), ((8, 1), (16392, 3)), 'eRtPosition', None, MsgKey_
                                 , MSGXML)

    def eShowReg_Server_IP(self, Kind=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809366, LCID, 1, (8, 0), ((8, 1),), Kind
                                         )

    def eShowVersion(self):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809365, LCID, 1, (8, 0), (), )

    def eTDate(self, Type_Kind=defaultNamedNotOptArg, TradeDate=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809386, 1, (3, 0), ((8, 1), (16392, 3), (16392, 3)), 'eTDate', None, Type_Kind
                                 , TradeDate, MSGXML)

    def efEquity(self, MsgKey_=defaultNamedNotOptArg, Currency_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809413, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'efEquity', None, MsgKey_
                                 , Currency_, MSGXML)

    def efEquity_AID(self, AID=defaultNamedNotOptArg, Currency_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809412, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'efEquity_AID', None, AID
                                 , Currency_, MSGXML)

    def efMatch(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809387, 1, (3, 0), ((8, 1), (16392, 3)), 'efMatch', None, MsgKey_
                                 , MSGXML)

    def efMatch_AID(self, AID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809389, 1, (3, 0), ((8, 1), (16392, 3)), 'efMatch_AID', None, AID
                                 , MSGXML)

    def efMatch_ID(self, ID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809388, 1, (3, 0), ((8, 1), (16392, 3)), 'efMatch_ID', None, ID
                                 , MSGXML)

    def efModifyOrder(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                      OrderNo=defaultNamedNotOptArg
                      , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg, Qcurrent=defaultNamedNotOptArg,
                      Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                      , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809398, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder', None, MsgKey_
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, MSGXML)

    def efModifyOrder1(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                       OrderNo=defaultNamedNotOptArg
                       , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg, Qcurrent=defaultNamedNotOptArg,
                       Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                       , Session=defaultNamedNotOptArg, Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809462, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder1', None, MsgKey_
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, Session, Cond
                                 , MSGXML)

    def efModifyOrder2(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg,
                       OID=defaultNamedNotOptArg
                       , OrderNo=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                       Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg
                       , PreOrder=defaultNamedNotOptArg, Session=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809484, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder2', None, MsgKey_
                                 , TDate, Type_, OID, OrderNo, Qty
                                 , ProductType, Qcurrent, Qmatch, PreOrder, Session
                                 , MSGXML)

    def efModifyOrder_AID(self, AID=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                          OrderNo=defaultNamedNotOptArg
                          , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                          Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                          , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809399, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder_AID', None, AID
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, MSGXML)

    def efModifyOrder_AID1(self, AID=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                           OrderNo=defaultNamedNotOptArg
                           , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                           Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                           , Session=defaultNamedNotOptArg, Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809463, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder_AID1', None, AID
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, Session, Cond
                                 , MSGXML)

    def efModifyOrder_AID2(self, AID=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg,
                           OID=defaultNamedNotOptArg
                           , OrderNo=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg,
                           ProductType=defaultNamedNotOptArg, Qcurrent=defaultNamedNotOptArg,
                           Qmatch=defaultNamedNotOptArg
                           , PreOrder=defaultNamedNotOptArg, Session=defaultNamedNotOptArg,
                           MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809485, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder_AID2', None, AID
                                 , TDate, Type_, OID, OrderNo, Qty
                                 , ProductType, Qcurrent, Qmatch, PreOrder, Session
                                 , MSGXML)

    def efOrder(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                CommID=defaultNamedNotOptArg
                , CommID_EP=defaultNamedNotOptArg, CommID_YM=defaultNamedNotOptArg, CommID_CP=defaultNamedNotOptArg,
                BS=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg
                , Price=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg,
                Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809393, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (16392, 3)), 'efOrder', None, MsgKey_
                                 , TDate, ProductType, CommID, CommID_EP, CommID_YM
                                 , CommID_CP, BS, PriceType, Price, Qty
                                 , Offset, Cond, MSGXML)

    def efOrder_2(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                  CommID=defaultNamedNotOptArg
                  , CommID_EP=defaultNamedNotOptArg, CommID_YM=defaultNamedNotOptArg, CommID_CP=defaultNamedNotOptArg,
                  BS=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg
                  , Price=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg,
                  Cond=defaultNamedNotOptArg, CommID2=defaultNamedNotOptArg
                  , CommID_EP2=defaultNamedNotOptArg, CommID_YM2=defaultNamedNotOptArg,
                  CommID_CP2=defaultNamedNotOptArg, BS2=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809395, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'efOrder_2', None, MsgKey_
                                 , TDate, ProductType, CommID, CommID_EP, CommID_YM
                                 , CommID_CP, BS, PriceType, Price, Qty
                                 , Offset, Cond, CommID2, CommID_EP2, CommID_YM2
                                 , CommID_CP2, BS2, MSGXML)

    def efOrder_AID(self, AID=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                    CommID=defaultNamedNotOptArg
                    , CommID_EP_=defaultNamedNotOptArg, CommID_YM=defaultNamedNotOptArg,
                    CommID_CP_=defaultNamedNotOptArg, BS=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg
                    , Price=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg,
                    Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809394, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (16392, 3)), 'efOrder_AID', None, AID
                                 , TDate, ProductType, CommID, CommID_EP_, CommID_YM
                                 , CommID_CP_, BS, PriceType, Price, Qty
                                 , Offset, Cond, MSGXML)

    def efOrder_AID_2(self, AID=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                      CommID=defaultNamedNotOptArg
                      , CommID_EP_=defaultNamedNotOptArg, CommID_YM=defaultNamedNotOptArg,
                      CommID_CP_=defaultNamedNotOptArg, BS=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg
                      , Price=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg,
                      Cond=defaultNamedNotOptArg, CommID2=defaultNamedNotOptArg
                      , CommID_EP2_=defaultNamedNotOptArg, CommID_YM2=defaultNamedNotOptArg,
                      CommID_CP2_=defaultNamedNotOptArg, BS2=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809396, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'efOrder_AID_2', None, AID
                                 , TDate, ProductType, CommID, CommID_EP_, CommID_YM
                                 , CommID_CP_, BS, PriceType, Price, Qty
                                 , Offset, Cond, CommID2, CommID_EP2_, CommID_YM2
                                 , CommID_CP2_, BS2, MSGXML)

    def efPosition(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809401, 1, (3, 0), ((8, 1), (16392, 3)), 'efPosition', None, MsgKey_
                                 , MSGXML)

    def efPosition_AID(self, AID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809402, 1, (3, 0), ((8, 1), (16392, 3)), 'efPosition_AID', None, AID
                                 , MSGXML)

    def efQueryAll(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809391, 1, (3, 0), ((8, 1), (16392, 3)), 'efQueryAll', None, MsgKey_
                                 , MSGXML)

    def efQueryAll_AID(self, AID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809392, 1, (3, 0), ((8, 1), (16392, 3)), 'efQueryAll_AID', None, AID
                                 , MSGXML)

    def efQueryAll_ID(self, ID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809390, 1, (3, 0), ((8, 1), (16392, 3)), 'efQueryAll_ID', None, ID
                                 , MSGXML)

    def efTrans(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809403, 1, (3, 0), ((8, 1), (16392, 3)), 'efTrans', None, MsgKey_
                                 , MSGXML)

    def efTrans_AID(self, AID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809404, 1, (3, 0), ((8, 1), (16392, 3)), 'efTrans_AID', None, AID
                                 , MSGXML)

    _prop_map_get_ = {
    }
    _prop_map_put_ = {
    }

    def __iter__(self):
        "Return a Python iterator for this object"
        try:
            ob = self._oleobj_.InvokeTypes(-4, LCID, 3, (13, 10), ())
        except pythoncom.error:
            raise TypeError("This object does not support enumeration")
        return win32com.client.util.Iterator(ob, None)


class _Fubon_Mananger_MsgServer_2(DispatchBaseClass):
    CLSID = IID('{E9188558-F1F6-4A06-A293-5A0F00093D3D}')
    coclass_clsid = IID('{47C406EC-DDD0-48B3-B8B2-7529580C54DD}')

    def CASign(self, strContent=defaultNamedNotOptArg, IDNO=defaultNamedNotOptArg, CAID=defaultNamedNotOptArg,
               CLSID=defaultNamedNotOptArg
               , DataSignature=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809355, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'CASign', None,
                                 strContent
                                 , IDNO, CAID, CLSID, DataSignature)

    def Ekey_AddPreSignData(self, PID=defaultNamedNotOptArg, PWD=defaultNamedNotOptArg, File=defaultNamedNotOptArg,
                            MessageStr=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809379, 1, (11, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'Ekey_AddPreSignData',
                                 None, PID
                                 , PWD, File, MessageStr)

    def Find_AID_by_ID(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809359, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def Find_MsgKey_by_ID(self, ID=defaultNamedNotOptArg, count=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809360, LCID, 1, (8, 0), ((8, 1), (2, 1)), ID
                                         , count)

    def GetServerTime(self, ServerTime=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809378, 1, (3, 0), ((16392, 3), (16392, 3)), 'GetServerTime', None, ServerTime
                                 , MSGXML)

    def MsgServer_AddMsg(self, bsMsgKey=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809351, LCID, 1, (24, 0), ((8, 1),), bsMsgKey
                                         )

    def MsgServer_RemoveMsg(self, bsMsgKey=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809352, LCID, 1, (24, 0), ((8, 1),), bsMsgKey
                                         )

    def Set_Trans_Position(self, enable=defaultNamedNotOptArg):
        return self._oleobj_.InvokeTypes(1610809380, LCID, 1, (3, 0), ((11, 1),), enable
                                         )

    def eBill(self, MsgKey_=defaultNamedNotOptArg, stockid=defaultNamedNotOptArg, FromDate=defaultNamedNotOptArg,
              ToDate=defaultNamedNotOptArg
              , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809388, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'eBill', None,
                                 MsgKey_
                                 , stockid, FromDate, ToDate, MSGXML)

    def eDayTrade(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809389, 1, (3, 0), ((8, 1), (16392, 3)), 'eDayTrade', None, MsgKey_
                                 , MSGXML)

    def eLogin(self, login_id=defaultNamedNotOptArg, login_pass=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809354, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eLogin', None, login_id
                                 , login_pass, MSGXML)

    def eLogin_CID(self, CID=defaultNamedNotOptArg, login_id=defaultNamedNotOptArg, login_pass=defaultNamedNotOptArg,
                   MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809353, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'eLogin_CID', None, CID
                                 , login_id, login_pass, MSGXML)

    def eLogout(self):
        return self._oleobj_.InvokeTypes(1610809358, LCID, 1, (3, 0), (), )

    def eMatch(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809386, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eMatch', None, MsgKey_
                                 , TT, MSGXML)

    def eMatchOne(self, MsgKey_=defaultNamedNotOptArg, OrderNo=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809387, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eMatchOne', None, MsgKey_
                                 , OrderNo, MSGXML)

    def eModifyOrder(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg,
                     TT=defaultNamedNotOptArg
                     , OT=defaultNamedNotOptArg, OID=defaultNamedNotOptArg, OrderNo=defaultNamedNotOptArg,
                     stockid=defaultNamedNotOptArg, BS=defaultNamedNotOptArg
                     , Qty=defaultNamedNotOptArg, Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg,
                     PreOrder=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809393, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (16392, 3)), 'eModifyOrder', None, MsgKey_
                                 , TDate, Type_, TT, OT, OID
                                 , OrderNo, stockid, BS, Qty, Qcurrent
                                 , Qmatch, PreOrder, MSGXML)

    def eOrder(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, TT=defaultNamedNotOptArg,
               OT=defaultNamedNotOptArg
               , BS=defaultNamedNotOptArg, stockid=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg,
               PriceType=defaultNamedNotOptArg, Price=defaultNamedNotOptArg
               , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809391, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'eOrder', None, MsgKey_
                                 , TDate, TT, OT, BS, stockid
                                 , Qty, PriceType, Price, MSGXML)

    def eOrder2(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, TT=defaultNamedNotOptArg,
                BS=defaultNamedNotOptArg
                , stockid=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Price=defaultNamedNotOptArg,
                P10=defaultNamedNotOptArg, PayType=defaultNamedNotOptArg
                , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809392, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'eOrder2', None, MsgKey_
                                 , TDate, TT, BS, stockid, Qty
                                 , Price, P10, PayType, MSGXML)

    def eQueryAll(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809384, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eQueryAll', None, MsgKey_
                                 , TT, MSGXML)

    def eQueryOne(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID_OrderNo=defaultNamedNotOptArg,
                  MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809383, 1, (3, 0), ((8, 1), (8, 1), (8, 1), (16392, 3)), 'eQueryOne', None, MsgKey_
                                 , Type_, OID_OrderNo, MSGXML)

    def eQueryOrder(self, MsgKey_=defaultNamedNotOptArg, TT=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809385, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'eQueryOrder', None, MsgKey_
                                 , TT, MSGXML)

    def eRtPosition(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809390, 1, (3, 0), ((8, 1), (16392, 3)), 'eRtPosition', None, MsgKey_
                                 , MSGXML)

    def eShowReg_Server_IP(self, Kind=defaultNamedNotOptArg):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809357, LCID, 1, (8, 0), ((8, 1),), Kind
                                         )

    def eShowVersion(self):
        # Result is a Unicode object
        return self._oleobj_.InvokeTypes(1610809356, LCID, 1, (8, 0), (), )

    def eTDate(self, Type_Kind=defaultNamedNotOptArg, TradeDate=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809361, 1, (3, 0), ((8, 1), (16392, 3), (16392, 3)), 'eTDate', None, Type_Kind
                                 , TradeDate, MSGXML)

    def efEquity(self, MsgKey_=defaultNamedNotOptArg, Currency_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809382, 1, (3, 0), ((8, 1), (8, 1), (16392, 3)), 'efEquity', None, MsgKey_
                                 , Currency_, MSGXML)

    def efMatch(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809362, 1, (3, 0), ((8, 1), (16392, 3)), 'efMatch', None, MsgKey_
                                 , MSGXML)

    def efModifyOrder(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                      OrderNo=defaultNamedNotOptArg
                      , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg, Qcurrent=defaultNamedNotOptArg,
                      Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                      , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809372, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder', None, MsgKey_
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, MSGXML)

    def efModifyOrder1(self, MsgKey_=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                       OrderNo=defaultNamedNotOptArg
                       , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg, Qcurrent=defaultNamedNotOptArg,
                       Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                       , Session=defaultNamedNotOptArg, Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809408, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder1', None, MsgKey_
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, Session, Cond
                                 , MSGXML)

    def efModifyOrder2(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg,
                       OID=defaultNamedNotOptArg
                       , OrderNo=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                       Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg
                       , PreOrder=defaultNamedNotOptArg, Session=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809424, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder2', None, MsgKey_
                                 , TDate, Type_, OID, OrderNo, Qty
                                 , ProductType, Qcurrent, Qmatch, PreOrder, Session
                                 , MSGXML)

    def efModifyOrder_AID(self, AID=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                          OrderNo=defaultNamedNotOptArg
                          , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                          Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                          , MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809423, 1, (3, 0),
                                 ((8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder_AID', None, AID
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, MSGXML)

    def efModifyOrder_AID1(self, AID=defaultNamedNotOptArg, Type_=defaultNamedNotOptArg, OID=defaultNamedNotOptArg,
                           OrderNo=defaultNamedNotOptArg
                           , Qty=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                           Qcurrent=defaultNamedNotOptArg, Qmatch=defaultNamedNotOptArg, PreOrder=defaultNamedNotOptArg
                           , Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809409, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)),
                                 'efModifyOrder_AID1', None, AID
                                 , Type_, OID, OrderNo, Qty, ProductType
                                 , Qcurrent, Qmatch, PreOrder, Cond, MSGXML
                                 )

    def efOrder(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                CommID=defaultNamedNotOptArg
                , CommID_EP=defaultNamedNotOptArg, CommID_YM=defaultNamedNotOptArg, CommID_CP=defaultNamedNotOptArg,
                BS=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg
                , Price=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg,
                Cond=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809368, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (16392, 3)), 'efOrder', None, MsgKey_
                                 , TDate, ProductType, CommID, CommID_EP, CommID_YM
                                 , CommID_CP, BS, PriceType, Price, Qty
                                 , Offset, Cond, MSGXML)

    def efOrder_2(self, MsgKey_=defaultNamedNotOptArg, TDate=defaultNamedNotOptArg, ProductType=defaultNamedNotOptArg,
                  CommID=defaultNamedNotOptArg
                  , CommID_EP=defaultNamedNotOptArg, CommID_YM=defaultNamedNotOptArg, CommID_CP=defaultNamedNotOptArg,
                  BS=defaultNamedNotOptArg, PriceType=defaultNamedNotOptArg
                  , Price=defaultNamedNotOptArg, Qty=defaultNamedNotOptArg, Offset=defaultNamedNotOptArg,
                  Cond=defaultNamedNotOptArg, CommID2=defaultNamedNotOptArg
                  , CommID_EP2=defaultNamedNotOptArg, CommID_YM2=defaultNamedNotOptArg,
                  CommID_CP2=defaultNamedNotOptArg, BS2=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809370, 1, (3, 0), (
        (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1), (8, 1),
        (8, 1), (8, 1), (8, 1), (8, 1), (16392, 3)), 'efOrder_2', None, MsgKey_
                                 , TDate, ProductType, CommID, CommID_EP, CommID_YM
                                 , CommID_CP, BS, PriceType, Price, Qty
                                 , Offset, Cond, CommID2, CommID_EP2, CommID_YM2
                                 , CommID_CP2, BS2, MSGXML)

    def efPosition(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809374, 1, (3, 0), ((8, 1), (16392, 3)), 'efPosition', None, MsgKey_
                                 , MSGXML)

    def efQueryAll(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809366, 1, (3, 0), ((8, 1), (16392, 3)), 'efQueryAll', None, MsgKey_
                                 , MSGXML)

    def efQueryAll_ID(self, ID=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809365, 1, (3, 0), ((8, 1), (16392, 3)), 'efQueryAll_ID', None, ID
                                 , MSGXML)

    def efTrans(self, MsgKey_=defaultNamedNotOptArg, MSGXML=defaultNamedNotOptArg):
        return self._ApplyTypes_(1610809376, 1, (3, 0), ((8, 1), (16392, 3)), 'efTrans', None, MsgKey_
                                 , MSGXML)

    _prop_map_get_ = {
    }
    _prop_map_put_ = {
    }

    def __iter__(self):
        "Return a Python iterator for this object"
        try:
            ob = self._oleobj_.InvokeTypes(-4, LCID, 3, (13, 10), ())
        except pythoncom.error:
            raise TypeError("This object does not support enumeration")
        return win32com.client.util.Iterator(ob, None)


class _FutureTradeCOM_Test(DispatchBaseClass):
    CLSID = IID('{0DEF5AE9-A386-4792-8111-B95E5F2E4306}')
    coclass_clsid = IID('{4B661E2A-9874-4534-B353-06F9C8E29B8C}')

    _prop_map_get_ = {
    }
    _prop_map_put_ = {
    }

    def __iter__(self):
        "Return a Python iterator for this object"
        try:
            ob = self._oleobj_.InvokeTypes(-4, LCID, 3, (13, 10), ())
        except pythoncom.error:
            raise TypeError("This object does not support enumeration")
        return win32com.client.util.Iterator(ob, None)


class _Fbs_MsgServ2_:
    CLSID = CLSID_Sink = IID('{A893A5A3-6619-4A7A-A7F4-50C02842F88F}')
    coclass_clsid = IID('{1A2CEB38-FAB7-434C-B797-D2978FD6908D}')
    _public_methods_ = []  # For COM Server support
    _dispid_to_func_ = {
        1: "OnInstantData",
        2: "OnStatus",
    }

    def __init__(self, oobj=None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc = oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp = cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie = cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp, self._olecp_cookie = cp, cookie

    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass

    def close(self):
        if self._olecp is not None:
            cp, cookie, self._olecp, self._olecp_cookie = self._olecp, self._olecp_cookie, None, None
            cp.Unadvise(cookie)

    def _query_interface_(self, iid):
        import win32com.server.util
        if iid == self.CLSID_Sink: return win32com.server.util.wrap(self)

# Event Handlers
# If you create handlers, they should have the following prototypes:


#	def OnInstantData(self, bsMsgID=defaultNamedNotOptArg, bsMsgKey=defaultNamedNotOptArg, bsData=defaultNamedNotOptArg):
#	def OnStatus(self, bsMsgID=defaultNamedNotOptArg, bsMsgKey=defaultNamedNotOptArg, nStatus=defaultNamedNotOptArg):


class _Fubon_Mananger_MsgServer_2_:
    CLSID = CLSID_Sink = IID('{D659B2A5-DC32-48E8-BBF1-A3884AD208E4}')
    coclass_clsid = IID('{47C406EC-DDD0-48B3-B8B2-7529580C54DD}')
    _public_methods_ = []  # For COM Server support
    _dispid_to_func_ = {
        1: "OnInstantData",
        2: "OnStatus",
    }

    def __init__(self, oobj=None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc = oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp = cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie = cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp, self._olecp_cookie = cp, cookie

    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass

    def close(self):
        if self._olecp is not None:
            cp, cookie, self._olecp, self._olecp_cookie = self._olecp, self._olecp_cookie, None, None
            cp.Unadvise(cookie)

    def _query_interface_(self, iid):
        import win32com.server.util
        if iid == self.CLSID_Sink: return win32com.server.util.wrap(self)

# Event Handlers
# If you create handlers, they should have the following prototypes:


#	def OnInstantData(self, bsMsgID=defaultNamedNotOptArg, bsMsgKey=defaultNamedNotOptArg, bsData=defaultNamedNotOptArg):
#	def OnStatus(self, bsMsgID=defaultNamedNotOptArg, bsMsgKey=defaultNamedNotOptArg, nStatus=defaultNamedNotOptArg):


class _FutureTradeCOM_Test_:
    CLSID = CLSID_Sink = IID('{C26AE6E3-7772-48F6-9527-9B1613A33B03}')
    coclass_clsid = IID('{4B661E2A-9874-4534-B353-06F9C8E29B8C}')
    _public_methods_ = []  # For COM Server support
    _dispid_to_func_ = {
    }

    def __init__(self, oobj=None):
        if oobj is None:
            self._olecp = None
        else:
            import win32com.server.util
            from win32com.server.policy import EventHandlerPolicy
            cpc = oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
            cp = cpc.FindConnectionPoint(self.CLSID_Sink)
            cookie = cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
            self._olecp, self._olecp_cookie = cp, cookie

    def __del__(self):
        try:
            self.close()
        except pythoncom.com_error:
            pass

    def close(self):
        if self._olecp is not None:
            cp, cookie, self._olecp, self._olecp_cookie = self._olecp, self._olecp_cookie, None, None
            cp.Unadvise(cookie)

    def _query_interface_(self, iid):
        import win32com.server.util
        if iid == self.CLSID_Sink: return win32com.server.util.wrap(self)

# Event Handlers
# If you create handlers, they should have the following prototypes:


from win32com.client import CoClassBaseClass


# This CoClass is known by the name 'FubonE01API.Fbs_MsgServ2'
class Fbs_MsgServ2(CoClassBaseClass):  # A CoClass
    CLSID = IID('{1A2CEB38-FAB7-434C-B797-D2978FD6908D}')
    coclass_sources = [
        _Fbs_MsgServ2_,
    ]
    default_source = _Fbs_MsgServ2_
    coclass_interfaces = [
        _Fbs_MsgServ2,
    ]
    default_interface = _Fbs_MsgServ2


# This CoClass is known by the name 'FubonE01API.Fubon_Mananger_API_2'
class Fubon_Mananger_API_2(CoClassBaseClass):  # A CoClass
    CLSID = IID('{60F749A4-6180-42BA-B9A3-5F2F657809DC}')
    coclass_sources = [
    ]
    coclass_interfaces = [
        _Fubon_Mananger_API_2,
    ]
    default_interface = _Fubon_Mananger_API_2


# This CoClass is known by the name 'FubonE01API.Fubon_Mananger_MsgServer_2'
class Fubon_Mananger_MsgServer_2(CoClassBaseClass):  # A CoClass
    CLSID = IID('{47C406EC-DDD0-48B3-B8B2-7529580C54DD}')
    coclass_sources = [
        _Fubon_Mananger_MsgServer_2_,
    ]
    default_source = _Fubon_Mananger_MsgServer_2_
    coclass_interfaces = [
        _Fubon_Mananger_MsgServer_2,
    ]
    default_interface = _Fubon_Mananger_MsgServer_2


# This CoClass is known by the name 'FubonE01API.FutureTradeCOM_Test'
class FutureTradeCOM_Test(CoClassBaseClass):  # A CoClass
    CLSID = IID('{4B661E2A-9874-4534-B353-06F9C8E29B8C}')
    coclass_sources = [
        _FutureTradeCOM_Test_,
    ]
    default_source = _FutureTradeCOM_Test_
    coclass_interfaces = [
        _FutureTradeCOM_Test,
    ]
    default_interface = _FutureTradeCOM_Test


_Fbs_MsgServ2_vtables_dispatch_ = 1
_Fbs_MsgServ2_vtables_ = [
    (('MsgServer_Connect', 'Fubon_Mananger',), 1610809347, (
    1610809347, (), [(9, 1, None, "IID('{EF592E6F-0455-4D83-B168-C7D40EA4B899}')"), ], 1, 1, 4, 0, 56,
    (3, 0, None, None), 0,)),
    (('MsgServer_Disconnect',), 1610809348, (1610809348, (), [], 1, 1, 4, 0, 64, (3, 0, None, None), 0,)),
    (('MsgServer_AddMsg', 'bsMsgKey', 'Fubon_Mananger',), 1610809349, (1610809349, (), [(8, 1, None, None),
                                                                                        (9, 1, None,
                                                                                         "IID('{EF592E6F-0455-4D83-B168-C7D40EA4B899}')"), ],
                                                                       1, 1, 4, 0, 72, (3, 0, None, None), 0,)),
    (('MsgServer_RemoveMsg', 'bsMsgKey',), 1610809350,
     (1610809350, (), [(8, 1, None, None), ], 1, 1, 4, 0, 80, (3, 0, None, None), 0,)),
]

_Fubon_Mananger_API_2_vtables_dispatch_ = 1
_Fubon_Mananger_API_2_vtables_ = [
    (('Get_Check_TSE_OPEN', None,), 1610809344,
     (1610809344, (), [(16395, 10, None, None), ], 1, 1, 4, 0, 56, (3, 0, None, None), 0,)),
    (('Get_Check_FUTURE_OPEN', None,), 1610809345,
     (1610809345, (), [(16395, 10, None, None), ], 1, 1, 4, 0, 64, (3, 0, None, None), 0,)),
    (('Get_Check_Session', None,), 1610809346,
     (1610809346, (), [(16395, 10, None, None), ], 1, 1, 4, 0, 72, (3, 0, None, None), 0,)),
    (('Set_Trans_Position', 'enable', None,), 1610809347, (1610809347, (), [(11, 1, None, None),
                                                                            (16387, 10, None, None), ], 1, 1, 4, 0, 80,
                                                           (3, 0, None, None), 0,)),
    (('AddPreSignData', 'PID', 'PWD', 'File_', 'MessageStr',
      None,), 1610809356, (1610809356, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16395, 10, None, None), ], 1, 1, 4, 0, 88,
                           (3, 0, None, None), 0,)),
    (('Ekey_AddPreSignData', 'PID', 'PWD', 'File_', 'MessageStr',
      None,), 1610809357, (1610809357, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16395, 10, None, None), ], 1, 1, 4, 0, 96,
                           (3, 0, None, None), 0,)),
    (('CASign', 'strContent', 'IDNO', 'CAID', 'CLSID',
      'DataSignature', None,), 1610809361, (1610809361, (), [(8, 1, None, None), (8, 1, None, None),
                                                             (8, 1, None, None), (8, 1, None, None),
                                                             (16392, 3, None, None), (16395, 10, None, None), ], 1, 1,
                                            4, 0, 104, (3, 0, None, None), 0,)),
    (('Check_Login', 'MSGXML', None,), 1610809362, (1610809362, (), [(16392, 3, None, None),
                                                                     (16387, 10, None, None), ], 1, 1, 4, 0, 112,
                                                    (3, 0, None, None), 0,)),
    (('Check_GROUP', 'AID', 'MSGXML', None,), 1610809363, (1610809363, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 120, (3, 0, None, None),
                                                           0,)),
    (('Check_ID_ACC', 'MsgKey', None,), 1610809364, (1610809364, (), [(8, 1, None, None),
                                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 128,
                                                     (3, 0, None, None), 0,)),
    (('eShowVersion', None,), 1610809365,
     (1610809365, (), [(16392, 10, None, None), ], 1, 1, 4, 0, 136, (3, 0, None, None), 0,)),
    (('eShowReg_Server_IP', 'Kind', None,), 1610809366, (1610809366, (), [(8, 1, None, None),
                                                                          (16392, 10, None, None), ], 1, 1, 4, 0, 144,
                                                         (3, 0, None, None), 0,)),
    (('Find_AID_by_ID', 'ID', 'count', None,), 1610809372, (1610809372, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 152, (3, 0, None, None), 0,)),
    (('Find_AID_by_ID_S', 'ID', 'count', None,), 1610809373, (1610809373, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 160, (3, 0, None, None), 0,)),
    (('Find_AID_by_ID_F', 'ID', 'count', None,), 1610809374, (1610809374, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 168, (3, 0, None, None), 0,)),
    (('Find_MsgKey_by_ID', 'ID', 'count', None,), 1610809375, (1610809375, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 176, (3, 0, None, None), 0,)),
    (('Find_MsgKey_by_ID_S', 'ID', 'count', None,), 1610809376, (1610809376, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 184, (3, 0, None, None), 0,)),
    (('Find_MsgKey_by_ID_F', 'ID', 'count', None,), 1610809377, (1610809377, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 192, (3, 0, None, None), 0,)),
    (('eLogout', None,), 1610809378,
     (1610809378, (), [(16387, 10, None, None), ], 1, 1, 4, 0, 200, (3, 0, None, None), 0,)),
    (('eLogout_MsgServ', 'ObjMsgServ', None,), 1610809379, (1610809379, (), [(9, 1, None, None),
                                                                             (16387, 10, None, None), ], 1, 1, 4, 0,
                                                            208, (3, 0, None, None), 0,)),
    (('eLogin_MsgServ_CID', 'CID', 'login_id', 'login_pass', 'ObjMsgServ',
      'MSGXML', None,), 1610809382, (1610809382, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (9, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 216, (3, 0, None, None),
                                     0,)),
    (('eLogin_CID', 'CID', 'login_id', 'login_pass', 'MSGXML',
      None,), 1610809383, (1610809383, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 224,
                           (3, 0, None, None), 0,)),
    (('eLogin_MsgServ', 'login_id', 'login_pass', 'ObjMsgServ', 'MSGXML',
      None,), 1610809384, (1610809384, (), [(8, 1, None, None), (8, 1, None, None), (9, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 232,
                           (3, 0, None, None), 0,)),
    (('eLogin', 'login_id', 'login_pass', 'MSGXML', None,
      ), 1610809385, (
     1610809385, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 240, (3, 0, None, None), 0,)),
    (('eTDate', 'Type_Kind', 'TradeDate', 'MSGXML', None,
      ), 1610809386, (
     1610809386, (), [(8, 1, None, None), (16392, 3, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1,
     1, 4, 0, 248, (3, 0, None, None), 0,)),
    (('efMatch', 'MsgKey_', 'MSGXML', None,), 1610809387, (1610809387, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 256, (3, 0, None, None),
                                                           0,)),
    (('efMatch_ID', 'ID', 'MSGXML', None,), 1610809388, (1610809388, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 264, (3, 0, None, None),
                                                         0,)),
    (('efMatch_AID', 'AID', 'MSGXML', None,), 1610809389, (1610809389, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 272, (3, 0, None, None),
                                                           0,)),
    (('efQueryAll_ID', 'ID', 'MSGXML', None,), 1610809390, (1610809390, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 280, (3, 0, None, None),
                                                            0,)),
    (('efQueryAll', 'MsgKey_', 'MSGXML', None,), 1610809391, (1610809391, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 288, (3, 0, None, None),
                                                              0,)),
    (('efQueryAll_AID', 'AID', 'MSGXML', None,), 1610809392, (1610809392, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 296, (3, 0, None, None),
                                                              0,)),
    (('efOrder', 'MsgKey_', 'TDate', 'ProductType', 'CommID',
      'CommID_EP', 'CommID_YM', 'CommID_CP', 'BS', 'PriceType',
      'Price', 'Qty', 'Offset', 'Cond', 'MSGXML',
      None,), 1610809393, (1610809393, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 304,
                           (3, 0, None, None), 0,)),
    (('efOrder_AID', 'AID', 'TDate', 'ProductType', 'CommID',
      'CommID_EP_', 'CommID_YM', 'CommID_CP_', 'BS', 'PriceType',
      'Price', 'Qty', 'Offset', 'Cond', 'MSGXML',
      None,), 1610809394, (1610809394, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 312,
                           (3, 0, None, None), 0,)),
    (('efOrder_2', 'MsgKey_', 'TDate', 'ProductType', 'CommID',
      'CommID_EP', 'CommID_YM', 'CommID_CP', 'BS', 'PriceType',
      'Price', 'Qty', 'Offset', 'Cond', 'CommID2',
      'CommID_EP2', 'CommID_YM2', 'CommID_CP2', 'BS2', 'MSGXML',
      None,), 1610809395, (1610809395, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 320,
                           (3, 0, None, None), 0,)),
    (('efOrder_AID_2', 'AID', 'TDate', 'ProductType', 'CommID',
      'CommID_EP_', 'CommID_YM', 'CommID_CP_', 'BS', 'PriceType',
      'Price', 'Qty', 'Offset', 'Cond', 'CommID2',
      'CommID_EP2_', 'CommID_YM2', 'CommID_CP2_', 'BS2', 'MSGXML',
      None,), 1610809396, (1610809396, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 328,
                           (3, 0, None, None), 0,)),
    (('efModifyOrder', 'MsgKey_', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'MSGXML', None,), 1610809398, (1610809398, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 336, (3, 0, None, None),
                                     0,)),
    (('efModifyOrder_AID', 'AID', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'MSGXML', None,), 1610809399, (1610809399, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 344, (3, 0, None, None),
                                     0,)),
    (('efPosition', 'MsgKey_', 'MSGXML', None,), 1610809401, (1610809401, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 352, (3, 0, None, None),
                                                              0,)),
    (('efPosition_AID', 'AID', 'MSGXML', None,), 1610809402, (1610809402, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 360, (3, 0, None, None),
                                                              0,)),
    (('efTrans', 'MsgKey_', 'MSGXML', None,), 1610809403, (1610809403, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 368, (3, 0, None, None),
                                                           0,)),
    (('efTrans_AID', 'AID', 'MSGXML', None,), 1610809404, (1610809404, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 376, (3, 0, None, None),
                                                           0,)),
    (('GetServerTime', 'ServerTime', 'MSGXML', None,), 1610809410, (1610809410, (), [
        (16392, 3, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 384, (3, 0, None, None),
                                                                    0,)),
    (('efEquity_AID', 'AID', 'Currency_', 'MSGXML', None,
      ), 1610809412, (
     1610809412, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 392, (3, 0, None, None), 0,)),
    (('efEquity', 'MsgKey_', 'Currency_', 'MSGXML', None,
      ), 1610809413, (
     1610809413, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 400, (3, 0, None, None), 0,)),
    (('eQueryOne', 'MsgKey_', 'Type_', 'OID_OrderNo', 'MSGXML',
      None,), 1610809421, (1610809421, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 408,
                           (3, 0, None, None), 0,)),
    (('eQueryAll', 'MsgKey_', 'TT', 'MSGXML', None,
      ), 1610809422, (
     1610809422, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 416, (3, 0, None, None), 0,)),
    (('eQueryOrder', 'MsgKey_', 'TT', 'MSGXML', None,
      ), 1610809424, (
     1610809424, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 424, (3, 0, None, None), 0,)),
    (('eMatch', 'MsgKey_', 'TT', 'MSGXML', None,
      ), 1610809426, (
     1610809426, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 432, (3, 0, None, None), 0,)),
    (('eMatchOne', 'MsgKey_', 'OrderNo', 'MSGXML', None,
      ), 1610809427, (
     1610809427, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 440, (3, 0, None, None), 0,)),
    (('eBill', 'MsgKey_', 'stockid', 'FromDate', 'ToDate',
      'MSGXML', None,), 1610809429, (1610809429, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 448, (3, 0, None, None),
                                     0,)),
    (('eDayTrade', 'MsgKey_', 'MSGXML', None,), 1610809430, (1610809430, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 456, (3, 0, None, None),
                                                             0,)),
    (('eRtPosition', 'MsgKey_', 'MSGXML', None,), 1610809432, (1610809432, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 464, (3, 0, None, None),
                                                               0,)),
    (('Find_AID_Count_F', None,), 1610809434,
     (1610809434, (), [(16386, 10, None, None), ], 1, 1, 4, 0, 472, (3, 0, None, None), 0,)),
    (('Find_AID_Count_S', None,), 1610809435,
     (1610809435, (), [(16386, 10, None, None), ], 1, 1, 4, 0, 480, (3, 0, None, None), 0,)),
    (('eOrder', 'MsgKey_', 'TT', 'OT', 'BS',
      'stockid', 'Qty', 'PriceType', 'Price', 'MSGXML',
      None,), 1610809436, (1610809436, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 488,
                           (3, 0, None, None), 0,)),
    (('eOrder2', 'MsgKey_', 'TT', 'BS', 'stockid',
      'Qty', 'Price', 'P10', 'PayType', 'MSGXML',
      None,), 1610809437, (1610809437, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 496,
                           (3, 0, None, None), 0,)),
    (('eModifyOrder', 'MsgKey_', 'Type_', 'TT', 'OT',
      'OID', 'OrderNo', 'stockid', 'BS', 'Qty',
      'Qcurrent', 'Qmatch', 'PreOrder', 'MSGXML', None,
      ), 1610809439, (1610809439, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                       (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                       (8, 1, None, None),
                                       (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                       (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 504,
                      (3, 0, None, None), 0,)),
    (('SetTopMostWindow', 'hWnd', 'Topmost', None,), 1610809458, (1610809458, (), [
        (16387, 3, None, None), (16395, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 512, (3, 0, None, None),
                                                                  0,)),
    (('ShowForm',), 1610809459, (1610809459, (), [], 1, 1, 4, 0, 520, (3, 0, None, None), 0,)),
    (('efModifyOrder1', 'MsgKey_', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'Session', 'Cond', 'MSGXML', None,), 1610809462, (1610809462, (), [
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 528, (3, 0, None, None),
                                                        0,)),
    (('efModifyOrder_AID1', 'AID', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'Session', 'Cond', 'MSGXML', None,), 1610809463, (1610809463, (), [
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 536, (3, 0, None, None),
                                                        0,)),
    (('Get_Check_TAIEMG_OPEN', None,), 1610809464,
     (1610809464, (), [(16395, 10, None, None), ], 1, 1, 4, 0, 544, (3, 0, None, None), 0,)),
    (('efModifyOrder2', 'MsgKey_', 'TDate', 'Type_', 'OID',
      'OrderNo', 'Qty', 'ProductType', 'Qcurrent', 'Qmatch',
      'PreOrder', 'Session', 'MSGXML', None,), 1610809484, (1610809484, (), [
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 552, (3, 0, None, None),
                                                            0,)),
    (('efModifyOrder_AID2', 'AID', 'TDate', 'Type_', 'OID',
      'OrderNo', 'Qty', 'ProductType', 'Qcurrent', 'Qmatch',
      'PreOrder', 'Session', 'MSGXML', None,), 1610809485, (1610809485, (), [
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 560, (3, 0, None, None),
                                                            0,)),
]

_Fubon_Mananger_MsgServer_2_vtables_dispatch_ = 1
_Fubon_Mananger_MsgServer_2_vtables_ = [
    (('MsgServer_AddMsg', 'bsMsgKey',), 1610809351,
     (1610809351, (), [(8, 1, None, None), ], 1, 1, 4, 0, 3912, (3, 0, None, None), 0,)),
    (('MsgServer_RemoveMsg', 'bsMsgKey',), 1610809352,
     (1610809352, (), [(8, 1, None, None), ], 1, 1, 4, 0, 3920, (3, 0, None, None), 0,)),
    (('eLogin_CID', 'CID', 'login_id', 'login_pass', 'MSGXML',
      None,), 1610809353, (1610809353, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 3928,
                           (3, 0, None, None), 0,)),
    (('eLogin', 'login_id', 'login_pass', 'MSGXML', None,
      ), 1610809354, (
     1610809354, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 3936, (3, 0, None, None), 0,)),
    (('CASign', 'strContent', 'IDNO', 'CAID', 'CLSID',
      'DataSignature', None,), 1610809355, (1610809355, (), [(8, 1, None, None), (8, 1, None, None),
                                                             (8, 1, None, None), (8, 1, None, None),
                                                             (16392, 3, None, None), (16395, 10, None, None), ], 1, 1,
                                            4, 0, 3944, (3, 0, None, None), 0,)),
    (('eShowVersion', None,), 1610809356,
     (1610809356, (), [(16392, 10, None, None), ], 1, 1, 4, 0, 3952, (3, 0, None, None), 0,)),
    (('eShowReg_Server_IP', 'Kind', None,), 1610809357, (1610809357, (), [(8, 1, None, None),
                                                                          (16392, 10, None, None), ], 1, 1, 4, 0, 3960,
                                                         (3, 0, None, None), 0,)),
    (('eLogout', None,), 1610809358,
     (1610809358, (), [(16387, 10, None, None), ], 1, 1, 4, 0, 3968, (3, 0, None, None), 0,)),
    (('Find_AID_by_ID', 'ID', 'count', None,), 1610809359, (1610809359, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 3976, (3, 0, None, None), 0,)),
    (('Find_MsgKey_by_ID', 'ID', 'count', None,), 1610809360, (1610809360, (), [
        (8, 1, None, None), (2, 1, None, None), (16392, 10, None, None), ], 1, 1, 4, 0, 3984, (3, 0, None, None), 0,)),
    (('eTDate', 'Type_Kind', 'TradeDate', 'MSGXML', None,
      ), 1610809361, (
     1610809361, (), [(8, 1, None, None), (16392, 3, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1,
     1, 4, 0, 3992, (3, 0, None, None), 0,)),
    (('efMatch', 'MsgKey_', 'MSGXML', None,), 1610809362, (1610809362, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4000, (3, 0, None, None),
                                                           0,)),
    (('efQueryAll_ID', 'ID', 'MSGXML', None,), 1610809365, (1610809365, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4008, (3, 0, None, None),
                                                            0,)),
    (('efQueryAll', 'MsgKey_', 'MSGXML', None,), 1610809366, (1610809366, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4016, (3, 0, None, None),
                                                              0,)),
    (('efOrder', 'MsgKey_', 'TDate', 'ProductType', 'CommID',
      'CommID_EP', 'CommID_YM', 'CommID_CP', 'BS', 'PriceType',
      'Price', 'Qty', 'Offset', 'Cond', 'MSGXML',
      None,), 1610809368, (1610809368, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4024,
                           (3, 0, None, None), 0,)),
    (('efOrder_2', 'MsgKey_', 'TDate', 'ProductType', 'CommID',
      'CommID_EP', 'CommID_YM', 'CommID_CP', 'BS', 'PriceType',
      'Price', 'Qty', 'Offset', 'Cond', 'CommID2',
      'CommID_EP2', 'CommID_YM2', 'CommID_CP2', 'BS2', 'MSGXML',
      None,), 1610809370, (1610809370, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4032,
                           (3, 0, None, None), 0,)),
    (('efModifyOrder', 'MsgKey_', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'MSGXML', None,), 1610809372, (1610809372, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 4040, (3, 0, None, None),
                                     0,)),
    (('efPosition', 'MsgKey_', 'MSGXML', None,), 1610809374, (1610809374, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4048, (3, 0, None, None),
                                                              0,)),
    (('efTrans', 'MsgKey_', 'MSGXML', None,), 1610809376, (1610809376, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4056, (3, 0, None, None),
                                                           0,)),
    (('GetServerTime', 'ServerTime', 'MSGXML', None,), 1610809378, (1610809378, (), [
        (16392, 3, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4064,
                                                                    (3, 0, None, None), 0,)),
    (('Ekey_AddPreSignData', 'PID', 'PWD', 'File', 'MessageStr',
      None,), 1610809379, (1610809379, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16395, 10, None, None), ], 1, 1, 4, 0, 4072,
                           (3, 0, None, None), 0,)),
    (('Set_Trans_Position', 'enable', None,), 1610809380, (1610809380, (), [(11, 1, None, None),
                                                                            (16387, 10, None, None), ], 1, 1, 4, 0,
                                                           4080, (3, 0, None, None), 0,)),
    (('efEquity', 'MsgKey_', 'Currency_', 'MSGXML', None,
      ), 1610809382, (
     1610809382, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 4088, (3, 0, None, None), 0,)),
    (('eQueryOne', 'MsgKey_', 'Type_', 'OID_OrderNo', 'MSGXML',
      None,), 1610809383, (1610809383, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4096,
                           (3, 0, None, None), 0,)),
    (('eQueryAll', 'MsgKey_', 'TT', 'MSGXML', None,
      ), 1610809384, (
     1610809384, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 4104, (3, 0, None, None), 0,)),
    (('eQueryOrder', 'MsgKey_', 'TT', 'MSGXML', None,
      ), 1610809385, (
     1610809385, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 4112, (3, 0, None, None), 0,)),
    (('eMatch', 'MsgKey_', 'TT', 'MSGXML', None,
      ), 1610809386, (
     1610809386, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 4120, (3, 0, None, None), 0,)),
    (('eMatchOne', 'MsgKey_', 'OrderNo', 'MSGXML', None,
      ), 1610809387, (
     1610809387, (), [(8, 1, None, None), (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1,
     4, 0, 4128, (3, 0, None, None), 0,)),
    (('eBill', 'MsgKey_', 'stockid', 'FromDate', 'ToDate',
      'MSGXML', None,), 1610809388, (1610809388, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 4136, (3, 0, None, None),
                                     0,)),
    (('eDayTrade', 'MsgKey_', 'MSGXML', None,), 1610809389, (1610809389, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4144, (3, 0, None, None),
                                                             0,)),
    (('eRtPosition', 'MsgKey_', 'MSGXML', None,), 1610809390, (1610809390, (), [
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4152, (3, 0, None, None),
                                                               0,)),
    (('eOrder', 'MsgKey_', 'TDate', 'TT', 'OT',
      'BS', 'stockid', 'Qty', 'PriceType', 'Price',
      'MSGXML', None,), 1610809391, (1610809391, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 4160, (3, 0, None, None),
                                     0,)),
    (('eOrder2', 'MsgKey_', 'TDate', 'TT', 'BS',
      'stockid', 'Qty', 'Price', 'P10', 'PayType',
      'MSGXML', None,), 1610809392, (1610809392, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 4168, (3, 0, None, None),
                                     0,)),
    (('eModifyOrder', 'MsgKey_', 'TDate', 'Type_', 'TT',
      'OT', 'OID', 'OrderNo', 'stockid', 'BS',
      'Qty', 'Qcurrent', 'Qmatch', 'PreOrder', 'MSGXML',
      None,), 1610809393, (1610809393, (), [(8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                            (8, 1, None, None), (8, 1, None, None),
                                            (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4176,
                           (3, 0, None, None), 0,)),
    (('efModifyOrder1', 'MsgKey_', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'Session', 'Cond', 'MSGXML', None,), 1610809408, (1610809408, (), [
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4184, (3, 0, None, None),
                                                        0,)),
    (('efModifyOrder_AID1', 'AID', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'Cond', 'MSGXML', None,), 1610809409, (1610809409, (), [(8, 1, None, None),
                                                              (8, 1, None, None), (8, 1, None, None),
                                                              (8, 1, None, None), (8, 1, None, None),
                                                              (8, 1, None, None),
                                                              (8, 1, None, None), (8, 1, None, None),
                                                              (8, 1, None, None), (8, 1, None, None),
                                                              (16392, 3, None, None),
                                                              (16387, 10, None, None), ], 1, 1, 4, 0, 4192,
                                             (3, 0, None, None), 0,)),
    (('efModifyOrder_AID', 'AID', 'Type_', 'OID', 'OrderNo',
      'Qty', 'ProductType', 'Qcurrent', 'Qmatch', 'PreOrder',
      'MSGXML', None,), 1610809423, (1610809423, (), [(8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None),
                                                      (8, 1, None, None), (8, 1, None, None), (16392, 3, None, None),
                                                      (16387, 10, None, None), ], 1, 1, 4, 0, 4200, (3, 0, None, None),
                                     0,)),
    (('efModifyOrder2', 'MsgKey_', 'TDate', 'Type_', 'OID',
      'OrderNo', 'Qty', 'ProductType', 'Qcurrent', 'Qmatch',
      'PreOrder', 'Session', 'MSGXML', None,), 1610809424, (1610809424, (), [
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None), (8, 1, None, None),
        (8, 1, None, None), (16392, 3, None, None), (16387, 10, None, None), ], 1, 1, 4, 0, 4208, (3, 0, None, None),
                                                            0,)),
]

_FutureTradeCOM_Test_vtables_dispatch_ = 1
_FutureTradeCOM_Test_vtables_ = [
]

RecordMap = {
}

CLSIDToClassMap = {
    '{0DEF5AE9-A386-4792-8111-B95E5F2E4306}': _FutureTradeCOM_Test,
    '{C26AE6E3-7772-48F6-9527-9B1613A33B03}': _FutureTradeCOM_Test_,
    '{4B661E2A-9874-4534-B353-06F9C8E29B8C}': FutureTradeCOM_Test,
    '{EF592E6F-0455-4D83-B168-C7D40EA4B899}': _Fubon_Mananger_API_2,
    '{60F749A4-6180-42BA-B9A3-5F2F657809DC}': Fubon_Mananger_API_2,
    '{ABB84942-39DD-40CB-A176-8C508EE59CAD}': _Fbs_MsgServ2,
    '{A893A5A3-6619-4A7A-A7F4-50C02842F88F}': _Fbs_MsgServ2_,
    '{1A2CEB38-FAB7-434C-B797-D2978FD6908D}': Fbs_MsgServ2,
    '{E9188558-F1F6-4A06-A293-5A0F00093D3D}': _Fubon_Mananger_MsgServer_2,
    '{D659B2A5-DC32-48E8-BBF1-A3884AD208E4}': _Fubon_Mananger_MsgServer_2_,
    '{47C406EC-DDD0-48B3-B8B2-7529580C54DD}': Fubon_Mananger_MsgServer_2,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict(CLSIDToClassMap)
VTablesToPackageMap = {}
VTablesToClassMap = {
    '{0DEF5AE9-A386-4792-8111-B95E5F2E4306}': '_FutureTradeCOM_Test',
    '{EF592E6F-0455-4D83-B168-C7D40EA4B899}': '_Fubon_Mananger_API_2',
    '{ABB84942-39DD-40CB-A176-8C508EE59CAD}': '_Fbs_MsgServ2',
    '{E9188558-F1F6-4A06-A293-5A0F00093D3D}': '_Fubon_Mananger_MsgServer_2',
}

NamesToIIDMap = {
    '_FutureTradeCOM_Test': '{0DEF5AE9-A386-4792-8111-B95E5F2E4306}',
    '_FutureTradeCOM_Test_': '{C26AE6E3-7772-48F6-9527-9B1613A33B03}',
    '_Fubon_Mananger_API_2': '{EF592E6F-0455-4D83-B168-C7D40EA4B899}',
    '_Fbs_MsgServ2': '{ABB84942-39DD-40CB-A176-8C508EE59CAD}',
    '_Fbs_MsgServ2_': '{A893A5A3-6619-4A7A-A7F4-50C02842F88F}',
    '_Fubon_Mananger_MsgServer_2': '{E9188558-F1F6-4A06-A293-5A0F00093D3D}',
    '_Fubon_Mananger_MsgServer_2_': '{D659B2A5-DC32-48E8-BBF1-A3884AD208E4}',
}
