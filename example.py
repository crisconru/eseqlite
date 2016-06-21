import eseqlite
# dbb
ddbb = 'example.db'
# table
table = 'table_example'
# fields
fields = []
id = 'id integer primary key autoincrement'
fields.append(id)
code = 'code str unique'
fields.append(code)
type = 'type str'
fields.append(type)
print 'Fields = ' + str(fields)
# create table
eseqlite.createTable(ddbb, table, fields)
# update fields
values = [('2006-03-28', 'BUY'),
             ('2006-04-05', 'MSFT'),
             ('2006-04-06', 'SELL'),
            ]
fields2 = []
fields2.append('code')
fields2.append('type')
'''print 'Fields2 = ' + str(fields2)
print 'Values = ' + str(values)
eseqlite.insertTable(ddbb, table, fields2, values)
print eseqlite.make_fields(fields2)
print eseqlite.make_inputs(fields2)'''
print eseqlite.selectFields(ddbb,table,'code', '2006-04-05')