class accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_statement(self):
        print('the exception says ',self.msg)


try:
    raise accident('There is a terrible accident')
except accident as a:
    print('caught exception: ',a.print_statement())
    # pass
