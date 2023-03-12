import socket
from datetime import datetime as dt

# print(ascii_banner)
operation = "port scanning"
ip = ""
op_ports = []
ports = range(1, 65536)
file_name = ""

def probe(ip, port):
    result =1
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(5)
        r = sock.connect_ex((ip, port))
        if (r==0):
            # print("port open",port)
            result = 0
        sock.close()
    except Exception as e:
        pass
    # print("result", result)
    return result


def launchAttack():
    filw = open(file_name, 'w')
    filw.write("Port scan summary for host: "+ip+"\n")
    filw.write("========================================\n")
    for port in ports:
        # sys.stdout.flush()
        response = probe(ip, port)
        if (response == 0):
            op_ports.append(port)
    
    if op_ports:
        filw.write("Open ports:\n")
        for port in sorted(op_ports):
            filw.write(str(port)+"\n")
    else:
        filw.write("No ports are open.")

def setStage():
    global ip
    ip = input("Enter IP address: ")
    name = dt.isoformat(dt.now())
    global file_name
    file_name = "outputs/PortScan/"+name+".txt"
    print("Results will be written to file: ",file_name)