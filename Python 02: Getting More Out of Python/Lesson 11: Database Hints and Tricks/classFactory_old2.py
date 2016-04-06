"""
classFactory: function to add records to a DB table and return the records as 
tailored classes.
"""

def build_row(curs, table):
    # Get column names for this table
    curs.execute("""
        SELECT column_name FROM information_schema.columns 
        WHERE table_name='{0}'""".format(table))
    cols = []
    [cols.append(colname[0]) for colname in curs.fetchall()]
    """ Build a class that creates instances of specific rows """
    class DataRow:
        """ Generic data row class, specialized by surrounding function """
        def __init__(self, data=None):
            if data:
                """ Uses data and column names to inject attributes
                and add record to the DB """
                assert len(data)==len(self.cols[1:])
                self.curs.execute("""
                    INSERT INTO {0} ({1})
                    VALUES ({2})""".format(self.table, ", ".join(
                            ["{0}".format(colname) for colname in self.cols[1:]]), ", ".join(
                            ["{0!r}".format(datum) for datum in data])))
                # Get id of just added animal
                self.curs.execute("SELECT LAST_INSERT_ID()")
                data.insert(0, curs.fetchone()[0])
                self.set_attributes(data)
                
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(
                        ["{0!r}".format(getattr(self, c)) for c in self.cols]))
            
        def retrieve(self, condition=None):
            self.curs.execute("""
                SELECT * FROM {0} {1}
            """.format(self.table, condition))
            records = curs.fetchall()
            for record in records:
                self.set_attributes(record)
                yield record
                
        def set_attributes(self, datarow):
            for colname, row in zip(self.cols, datarow):
                setattr(self, colname, row)
            
    DataRow.curs = curs
    DataRow.table = table
    DataRow.cols = cols
    return DataRow