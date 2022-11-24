import socket,traceback
import time,sys
from PySide6.QtCore import QTimer, Slot, QThread, Signal, QObject
from numpy import positive
sys.dont_write_bytecode = True
import serial
import serial.tools.list_ports
from serial import SerialException
class pmc(object):

    def __init__(self,ip:str="192.168.1.55",port=7777):
        socket.setdefaulttimeout(3) #TODO: make timeout to variable
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_status=False
        self.ip=ip
        self.port=port

    def connect(self):
        status=False
        try:
            self._socket.connect((self.ip,  self.port))
        except Exception as e:
            error_info = traceback.format_exc()
            print(error_info)
        else:
            status=True
            self.connect_status=True
        return status

    def ver(self):
        return self.send_recv(b'VER?')

    def send(self, data):
        if isinstance(data,(bytes,)):
            self._socket.send(data + b'\r\n')
        else:
            self._socket.send(bytes(data, "utf-8") + b'\r\n')

    def send_recv(self, data):
        if isinstance(data,(bytes,)):
            self._socket.send(data + b'\r\n')
        else:
            self._socket.send(bytes(data, "utf-8") + b'\r\n')

        r = self._socket.recv(1024)
        #print(f'resp:{r}')
        return r.decode('utf8')

    def estop(self, ch):
        self.send('ESTP' + ch)

    def get_pos16(self):
        p = self.send_recv(b'PS_16?')
        return [int(x) for x in p.split('/')]

    def get_pos(self,ch:str):
        p = self.send_recv("PS?"+ch)
        return int(p) if p else None

    def set_pos(self,ch:str,pos):
        #PS<ch><pos>
        self.send("PS" + ch + str(pos))
    
    def abs_move(self,ch:str,pos,backlash=True):
        b="S" if backlash else "B"
        self.send("ABS"+ch+b+str(pos))

    def set_SPD(self,ch:str,mode:str):
        """set the speed mode of ch
        send(SPD+<mode>+ch)
        mode=L/LSPD or M/MSPD or H/HSPD
        Args:
            ch (str): _description_
            mode (str): L/LSPD or M/MSPD or H/HSPD
        """
        self.send("SPD"+mode+ch)
    
    def get_SPD(self,ch:str):
        """get the speed mode of ch

        Args:
            ch (str): _description_
        """
        resp=self.send_recv("SPD?"+ch)
        return resp.split('\r\n')[0] if resp else None


    def get_status(self):
        p = self.send_recv(b'STS_16?')
        return p

    def __exit__(self, exc_type, exc_value, traceback):
        self._socket.close()
        self.exc_type = exc_type
        self.exc_value = exc_value
        self.traceback = traceback

class pmc_RS232(object):
    """provide COM PORT for connection

    serial_port=serial.Serial(Selected_port="COM4")
    pmc_motor=pmc_RS232(port=serial_port)

    Args:
        object (_type_): _description_
    """

    def __init__(self,port:str="COM4"):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect_status=False
        self.serial=serial.Serial()
        #self.open_port(port)
        self.port=port

    def open_port(self):
        """
        open port for data transmission
        :return:
        """
        status_txt='no info'
        try:
            self.serial.port = self.port
            self.serial.baudrate = 38400
            self.serial.stopbits = 1
            self.serial.bytesize = 8
            self.serial.parity = 'N'
            self.serial.write_timeout=3
            self.serial.open()
        except Exception as e:
            print(e)
            status_txt=str(e)  
        else:
            self.connect_status=True
            status_txt='OK'
        return status_txt

    def close_port(self):
        """
        close the port
        :return: 
        """
        status_txt=None
        if self.serial.isOpen():
            try:
                self.serial.close()
            except Exception as e:
                status_txt=e
            else:
                status_txt='OK'
                self.connect_status=False
        return status_txt

    def cmd_send(self, cmd, read_timeout=30,receive_flag=True,wait: int = 1000):
        """
        write cmd via serial port
        :param read_timeout:  read timeout default=5s
        :param cmd: CMD to be send
        :return:
        """
        #send_msg = (cmd + '\r\n').encode('utf-8')
        #send_msg = cmd + '\r\n'
        send_msg=bytes(cmd, "utf-8") + b'\r\n'
        if self.serial.isOpen():
            print(f"start send {cmd}")
            self.read_flag = True
            rec_data = b''
            try:
                self.serial.write(send_msg)
            except SerialException as e:
                print(e)
            else:
                time.sleep(0.1)
                t0 = time.time()
                while self.read_flag and receive_flag and time.time() - t0 < read_timeout:
                    wait_Num = self.serial.in_waiting
                    if wait_Num > 0:
                        rec_data += self.serial.read(wait_Num)
                        #print(wait_Num)
                        # end read when get the stop bit '\n'
                        if b'\n' in rec_data:
                            self.read_flag = False
                            print(f'data reciveied in {1000 * (time.time() - t0):.4f}ms')
                    # else:
                    #     time.sleep(0.1)
                    #     print("wait 100ms")
            finally:
                return rec_data.decode('utf-8')


    def ver(self):
        return self.cmd_send(cmd='VER?',receive_flag=True)

    def status(self):
        return self.cmd_send(cmd='STS?')


    def estop(self, ch):
        self.cmd_send('ESTP' + ch,receive_flag=False)

    def get_pos16(self):
        p = self.cmd_send('PS_16?',receive_flag=True)
        return [int(x) for x in p.split('/')]

    def get_pos(self,ch:str):
        p = self.cmd_send("PS?"+ch,receive_flag=True)
        pos=p.split('\r\n')
        print(f'get pos {pos}')
        return int(pos[0])
        #return int(p) if p else None

    def set_pos(self,ch:str,pos):
        #PS<ch><pos>
        self.cmd_send("PS" + ch + str(pos),receive_flag=False)
    
    def abs_move(self,ch:str,pos,backlash=True):
        b="S" if backlash else "B"
        self.cmd_send("ABS"+ch+b+str(pos),receive_flag=False)

    def set_SPD(self,ch:str,mode:str):
        """set the speed mode of ch
        send(SPD+<mode>+ch)
        mode=L/LSPD or M/MSPD or H/HSPD
        Args:
            ch (str): _description_
            mode (str): L/LSPD or M/MSPD or H/HSPD
        """
        self.send("SPD"+mode+ch,receive_flag=False)
    
    def get_SPD(self,ch:str):
        """get the speed mode of ch

        Args:
            ch (str): _description_
        """
        resp=self.cmd_send("SPD?"+ch,receive_flag=True)
        return resp.split('\r\n')[0] if resp else None


    def get_status(self):
        p = self.cmd_send('STS_16?',receive_flag=True)
        return p

    def __exit__(self, exc_type, exc_value, traceback):
        self.serial.close()
        self.exc_type = exc_type
        self.exc_value = exc_value
        self.traceback = traceback

        

class pmcSetThread(QThread):
    """
    Working QThread for setting position of pmc motor,
    emit done signal when set position is finished successfully.
    emit signal: info = [new_pos, self.target_pos, self.ch_num, self.set_info]
    """
    done_signal = Signal(list)

    def __init__(self, pmc:pmc, ch_num:int, pos:int, num: int = 0, wait=1000,parent=None):
        super(pmcSetThread,self).__init__(parent)
        self.pmc=pmc
        self.ch_num=ch_num
        self.target_pos=pos
        self.check_n=num
        self.set_flag=True
        self.wait=wait
    
    def __del__(self):
        self.set_flag = False

    def run(self):
        t0 = time.time()  # for time out
        print(f'start setting ch{self.ch_num} position:...')
        if self.pmc.connect_status:
            cur_pos=self.pmc.get_pos(str(self.ch_num))
            self.msleep(100)
            #self.pmc.set_pos(str(self.ch_num),self.target_pos)
            self.pmc.abs_move(str(self.ch_num),self.target_pos)
            self.msleep(1000)
            time_out = 3.0+abs(cur_pos-self.target_pos)*0.2
            self.set_info = f'done with time out:{time_out}'
            while self.set_flag and time.time() - t0 < time_out:
                new_pos=self.pmc.get_pos(str(self.ch_num))
                if abs(new_pos-self.target_pos)<1:
                    self.msleep(200)
                    self.set_flag=False
                    self.set_info = 'done'
                else:
                    self.msleep(100)
            # jump out time
            print(f'set ch position done after: {time.time() - t0:.2f}s with timeout of {time_out}s')
            info = [new_pos, self.target_pos, self.ch_num, self.set_info]
            print(info)
            self.msleep(self.wait)
            self.done_signal.emit(info)
    
    def __del__(self):
        self.set_flag = False


if __name__=="__main__":
    # pmc_host = '192.168.1.55'
    # pmc_port = 7777

    #制作控制器项目
    #c = pmc(pmc_host,pmc_port)

    #与控制器连接
    #connect(ip, port)
    #返回值：无
    #connect_status=c.connect()

    #控制器版本
    #ver()
    #返回值：版本的字节串
    # if connect_status:
    #     print(c.ver())
    #     print(c.get_pos16())
    #     print(c.get_status())
    #     ch5_value=c.get_pos('5')
    #     print(f'ch5_value:{ch5_value}')
    #     c.abs_move('5',pos=ch5_value-200,backlash=True)
    # else:
    #     print(f'connect to {pmc_host}:{pmc_port} failed')
    PMC=pmc_RS232(port="COM4")
    connect_txt=PMC.open_port()
    print(connect_txt)
    a=PMC.get_pos('5')
    PMC.get_pos('5')
    b=PMC.get_pos('4')
    print(a,b)
