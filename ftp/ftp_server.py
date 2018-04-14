from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("admin", "admin", "/data1/nelson/data", perm="elradfmw")
authorizer.add_anonymous("/data1/nelson/data", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.147.128", 9000), handler)
server.serve_forever()
