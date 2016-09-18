import eseqlite
import datetime

''' DDBB '''
ddbb = 'example.db'

''' Table 1 '''
table1 = 'table_1'
# Columns - Fields of the Table 1
pos  = 'pos integer primary key autoincrement'
code = 'codigo str unique'
type = 'tipo str'
used = 'usado int'
when = 'cuando numeric'
fields = []
fields.append(pos)
fields.append(code)
fields.append(type)
fields.append(used)
fields.append(when)

''' Create Table 1'''
eseqlite.createTable(ddbb, table1, fields)

''' Insert data into Table 1 '''
values = [1234, 'peq', 0, datetime.datetime.now()]
#eseqlite.insert(ddbb, table1, values)

'''
fields2 = []
fields2.append('code')
fields2.append('type')'''
'''print 'Fields2 = ' + str(fields2)
print 'Values = ' + str(values)
eseqlite.insertTable(ddbb, table, fields2, values)
print eseqlite.make_fields(fields2)
print eseqlite.make_inputs(fields2)'''
#print eseqlite.selectFields(ddbb,table,'code', '2006-04-05')