from pexpect import pxssh

server = 'magalhaes01.grid.fe.up.pt'
user = 'ei11051'
password = 'sporting2018'

def sendCommand(command):
    var = pxssh.pxssh()
    if not var.login(server, user, password):
        print("SSH session failed on login.")
        print(str(var))
    else:
        print("SSH session login successful")
        var.sendline(command)
        var.prompt()
        print(var.before)
        var.logout()
    return;

