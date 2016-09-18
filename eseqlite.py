import sqlite3

''' Make a string query from a list'''
def make_query(components):
	query = '('
	for component in components:
		query += component + ','
	query[len(query)-1] = ')'
	return query# str(query)

def make_values(vals):
	values = '('
	for i in range(len(vals)-1):
		values += '?, '
	values += '?)'
	return values

def make_inputs(fields):
	query = '('
	i = 0
	for field in fields:
		query = query + field + '=?'
		if (i < len(fields) -1):
			query = query + ', '
		else :
			query = query + ') '
		i = i + 1
	#print query
	return query

def createTable(ddbb, table, fields):
	query = 'Create table if not exists ' + str(table) + make_query(fields)
	print 'createTable()\n', query
	# ddbb
	conn = sqlite3.connect(ddbb)
	c = conn.cursor()
	c.execute(query)
	conn.commit()
	conn.close()

def insert(ddbb, table, values):
	query = 'INSERT INTO ' + str(table) + ' VALUES '
	query += make_values(values)
	valuesTuple = tuple(values)
	vals = [valuesTuple]
	# ddbb
	conn = sqlite3.connect(ddbb)
	c = conn.cursor()
	c.executemany(query, vals)
	conn.commit()
	conn.close()
'''
def insert(ddbb, table, fields, values):
	query = 'INSERT OR IGNORE INTO ' + table + make_query(fields) + ' VALUES '
	query = query + make_values(len(fields))
	print query
	# ddbb
	conn = sqlite3.connect(ddbb)
	c = conn.cursor()
	c.executemany(query, values)
	conn.commit()
	conn.close()

def selectFields(ddbb, table, fields, values):
	query = 'SELECT '  + make_fields(fields) + 'FROM ' + table  + ' WHERE '
	query = query + make_inputs(fields)
	print query
	# ddbb
	conn = sqlite3.connect(ddbb)
	c = conn.cursor()
	c.execute(query, (values, ) )
	result = c.fetchall()
	conn.commit()
	conn.close()
	#return result
'''