import sqlite3

def make_query(components):
	query = ' ('
	i = 0
	for component in components:
		query = query + component
		if (i < len(components) -1):
			query = query + ', '
		else :
			query = query + ')'
		i = i + 1
	#print query
	return query

def make_fields(fields):
	query = ''
	i = 0
	for field in fields:
		query = query + field
		if (i < len(fields) -1):
			query = query + ', '
		else :
			query = query + ' '
		i = i + 1
	#print query
	return query

def make_values(num):
	values = '('
	for i in range(num-1):
		values = values + '?, '
	values = values + '?)'
	#print values
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
	print query
	# ddbb
	conn = sqlite3.connect(ddbb)
	c = conn.cursor()
	c.execute(query)
	conn.commit()
	conn.close()

def insertTable(ddbb, table, fields, values):
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
	