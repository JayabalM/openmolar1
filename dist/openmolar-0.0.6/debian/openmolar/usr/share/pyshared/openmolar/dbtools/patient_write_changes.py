# -*- coding: utf-8 -*-
# Copyright (c) 2009 Neil Wallace. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. See the GNU General Public License for more details.

import MySQLdb,sys,types
from openmolar.connect import connect
from openmolar.settings import localsettings
from openmolar.dbtools import patient_class

def write_changes(pt,changes):
    print "write_changes"
    if changes==[]:
        print "write changes called, but no changes for patient %d"%pt.serialno
        return True
    else:
        sqlcommands={}
        patchanges=""
        trtchanges=""
        for change in changes:
            
            if change in patient_class.patientTableAtts:
                value=pt.__dict__[change]
                print change,type(value)
                if change in patient_class.dateFields:
                    if value!=None and value!="":
                        patchanges+='%s="%s" ,'%(change,localsettings.uk_to_sqlDate(value))
                elif value==None:
                    patchanges+='%s=NULL ,'%(change)
                elif (type(value) is types.IntType) or  (type(value) is types.LongType):
                    patchanges+='%s=%s ,'%(change,value)
                else:
                    patchanges+='%s="%s" ,'%(change,value)
            if change == "bpe":
                sqlcommands['bpe']='insert into bpe set serialno=%d,bpedate="%s",bpe="%s"'%(pt.serialno,localsettings.uk_to_sqlDate(pt.bpe[-1][0]),pt.bpe[-1][1])
            if change == "estimates":
                sqlcommands["prvfees"]="update prvfees set data='%s' where serialno=%d and courseno=%d "%(pt.estimates[0][7],pt.serialno,pt.courseno)
                    
            if change in patient_class.currtrtmtTableAtts:
                value=pt.__dict__[change]
                if change in patient_class.dateFields:
                    if value!=None and value!="":
                        trtchanges+='%s="%s" ,'%(change,localsettings.uk_to_sqlDate(value))
                elif value==None:
                    trtchanges+='%s=NULL ,'%(change)
                elif (type(value) is types.IntType) or  (type(value) is types.LongType) :
                    trtchanges+='%s=%s ,'%(change,value)
                else:
                    trtchanges+='%s="%s" ,'%(change,value)
                
    result=True
    if patchanges != "":
        print "update patients SET %s where serialno=%s"%(patchanges.strip(","),pt.serialno)
        sqlcommands['patient'] = "update patients SET %s where serialno=%d"%(patchanges.strip(","),pt.serialno)
    if trtchanges != "":
        sqlcommands['currtrtmt'] = "update currtrtmt SET %s where serialno=%d and courseno=%d"%(trtchanges.strip(","),pt.serialno,pt.courseno0)
    if sqlcommands!={}:
        db=connect()
        cursor = db.cursor()
        for table in sqlcommands.keys():
            try:
                print sqlcommands[table]
                cursor.execute(sqlcommands[table])
                db.commit()
            except Exception,e:
                print "error saving %s for patient %d"%(table,pt.serialno)
                print e
                result = False
        cursor.close()
        #db.close()
    return result

def toNotes(serialno,newnotes):
    print "write changes - toNotes for patient %d"%serialno
    #print "writing to db",serialno,newnotes
    query="select max(lineno) from notes where serialno=%d"%serialno
    db=connect()
    cursor = db.cursor()
    cursor.execute(query)
    rows=cursor.fetchall()
    if rows!=((None,),):
        lineNo=rows[0][0]
    else:
        lineNo=0
    try:
        n=1
        t=localsettings.curTime()
        year,month,day,hour,min=t.year-1900,t.month,t.day,t.hour,t.minute                           #grrr - crap date implementation
        openstr="\x01"+"%s"%localsettings.operator+chr(day)+chr(month)+chr(year)+chr(day)+chr(month)+chr(year)+chr(hour)+chr(min)
        closestr="\x02"+"%s"%localsettings.operator+chr(day)+chr(month)+chr(year)+chr(hour)+chr(min)
        for note in [openstr]+newnotes+[closestr]:
            query='insert into notes (serialno,lineno,line) values (%d,%d,"%s")'%(serialno,lineNo+n,note)
            cursor.execute(query)
            n+=1
        result=lineNo
    except Exception,e:
        print e
        result=-1
    cursor.close()
    db.commit()
    #db.close()
    return result

def discreet_changes(pt_changed,changes):
    print "write changes - discreet changes"
    '''this updates only the selected atts - usually called by automated proc such as recalls... and accounts)
    only updates the patients table'''
    sqlcond=""
    for change in changes:
        value=pt_changed.__dict__[change]
        print change,type(value)
        if change in patient_class.dateFields:
            if value!="" and value!=None:
                sqlcond+='%s="%s" ,'%(change,localsettings.uk_to_sqlDate(value))
        elif value==None:
            sqlcond+='%s=NULL ,'%(change)
        elif (type(value) is types.IntType) or  (type(value) is types.LongType) :
            sqlcond+='%s=%s ,'%(change,value)
        else:
            sqlcond+='%s="%s" ,'%(change,value)
                   
    print "update patients SET %s where serialno=%s"%(sqlcond.strip(","),pt_changed.serialno)
    result=True
    if sqlcond!="":
        db=connect()
        cursor = db.cursor()
        #print cursor.execute(sqlcommand)
        try:
            sqlcommand= "update patients SET %s where serialno=%s"%(sqlcond.strip(","),pt_changed.serialno)
            cursor.execute(sqlcommand)
            db.commit()
        except Exception,e:
            print e
            result=False
        cursor.close()
        #db.close()
    return result