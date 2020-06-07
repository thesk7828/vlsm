import math
import os


class calc:
    nHost = list()  # grabs the hosts from user input
    ip = list()  # Splits IP octate's and stores in list with type 'int'
    ip_addr = list()  # Splits IP octate's and stores in list with type 'String'
    networks = 0  # intiating network with NULL value
    total_host = 0  # Specifies sum of all hosts from all the network
    cidr = list()  # Holds CIDR value for a particlar Host
    val = int(0)  # Used for general calculation
    netid = list()
    fid = list()
    lid = list()
    bid = list()
    chk = 0

    # Holding and Sorting the HOSTS in Decreasing manner
    def host(self, networks):
        self.networks = networks
        print("\n\n\n\u001b[38;5;135mEnter the number of host for all ",self.networks, " networks (4294967296 max.)-\n")
        for i in range(0, int(self.networks)):
            def ip():
                try:
                    print("\u001b[38;5;3mNETWORK ", i+1, ":\u001b[38;5;196m ")
                    temp = input()
                    self.nHost.append(int(temp))
                except ValueError:
                    print("hmm! Value seems to be numerical or not NULL.")
                    ip()
            ip()
        self.nHost.sort(reverse=True)
        tHost = 0
        print("\n\n\u001b[38;5;135mArranging Host in sequence -\n")
        for i in range(0, len(self.nHost)):
            print("\u001b[38;5;3mNETWORK ", i+1,
                  ":\u001b[38;5;51m ", self.nHost[i])
            tHost = self.nHost[i]+tHost
        self.total_host = int(tHost)
        tempx = int(self.networks)
        self.chk = int(tempx*2)
        print(
            "\n\n\u001b[38;5;135mTotal Hosts are :\u001b[38;5;51m ", self.total_host, "\n\n")

    # Here all the calculation related to Subnetting finding CIDR value for specific host and converting
    # CIDR value to Subnet Mask takes place
    def subnet(self):
        # // The following code is to get the IP from the user -
        #print("chk: ",self.chk)
        #print("Total Host + chk: ",self.total_host+self.chk)
        #print("\nNow enter the favorable IP with respect to number of host mentioned above!")
        # if ((self.total_host+self.chk)>0 and (self.total_host+self.chk)<=256):
        #    print("Note: It seems to be like you are recomended to use 'Class-C' PRIVATE_IP as the number Total Hosts are",self.total_host)
        # elif ((self.total_host+self.chk)>256 and (self.total_host+self.chk)<=65536):
        #   print("Note: It seems to be like you are recomended to use 'Class-B' PRIVATE_IP as the number Total Hosts are",self.total_host)
        # elif ((self.total_host+self.chk)>65536 and (self.total_host+self.chk)<=4294967296):
        #   print("Note :It seems to be like you are recomended to use 'Class-A' PRIVATE_IP as the number Total Hosts are",self.total_host)
        # else:
        #   pass
        #sam=input("enter IP : ")
        #print("\nu entered IP as :",sam)
        # self.ip_addr=sam.split(".")
        # self.ip=list()
        for x in range(0, len(self.ip_addr)):
            temp = self.ip_addr[x]
            self.ip.append(int(temp))

        # var=self.ip_addr[0]+"."+self.ip_addr[1]+"."+self.ip_addr[2]+"."+self.ip_addr[3]
        #print("merged_ip :",var)

        # for i in range(0, len(self.networks)):
        #   if i is 0:
        #       tmp=self.ip[3]+1

        #   temp=networks
        #  flag=0
        #  if (temp>256):
        #        while (temp<=256):
        #            temp=temp-256
        #            flag+=1

        # Finding CIDR Values
        for x in range(0, len(self.nHost)):
            temp = self.nHost[x]
            cidr = 32
            host_bit = 1
            flag = 2
            for x in range(1, 32):
                if flag > temp:
                    cidr = cidr-host_bit
                    self.cidr.append(int(cidr))
                    break
                else:
                    flag = flag*2
                    host_bit = host_bit+1

        # CIDR Value to Subnet Mask Conversion
        for x in range(0, len(self.cidr)):
            print(
                "\u001b[38;5;228m******************************************************************************************")
            print("\u001b[38;5;135mCIDR for ", self.nHost[x],
                  " host is \u001b[38;5;208m/", self.cidr[x])
            temp = self.cidr[x]
            if ((temp > 24) and (temp <= 32)):
                remain = 8 - (32-temp)
                self.calci(remain)
                print(
                    "\u001b[38;5;83mSubnet Mask:\u001b[38;5;51m 255 . 255 . 255 .", self.val, "\n")
                self.val = 0
            elif ((temp > 16) and (temp <= 24)):
                remain = 8 - (24-temp)
                self.calci(remain)
                print(
                    "\u001b[38;5;83mSubnet Mask:\u001b[38;5;51m 255 . 255 .", self.val, ". 0\n")
                self.val = 0
            elif ((temp > 8) and (temp <= 16)):
                remain = 8 - (16-temp)
                self.calci(remain)
                print(
                    "\u001b[38;5;83mSubnet Mask:\u001b[38;5;51m 255 .", self.val, ". 0 . 0\n")
                self.val = 0
            else:
                remain = 8 - temp
                self.calci(remain)
                print("\u001b[38;5;83mSubnet Mask:", self.val, ". 0 . 0 . 0\n")
                self.val = 0
        print(
            "\u001b[38;5;228m******************************************************************************************")

    # Function call for Subnet Mask Calculation
    def calci(self, bit):
        remain = bit
        sub = int(128)
        x = 0
        while x < remain:
            self.val = int(self.val+sub)
            sub = sub/2
            x += 1


# // Initiating code from here -
if __name__ == "__main__":
    os.system('cls')
    execute = calc()
    print('''
\u001b[38;5;210m..........................................................................................
\u001b[38;5;210m:'\u001b[38;5;67m##\u001b[38;5;210m::::'\u001b[38;5;67m##\u001b[38;5;210m:'\u001b[38;5;67m##\u001b[38;5;210m::::::::'\u001b[38;5;67m######\u001b[38;5;210m::'\u001b[38;5;67m##\u001b[38;5;210m::::'\u001b[38;5;67m##\u001b[38;5;210m:::::::::::'\u001b[38;5;67m######\u001b[38;5;210m::'\u001b[38;5;67m####\u001b[38;5;210m:'\u001b[38;5;67m########\u001b[38;5;210m::'\u001b[38;5;67m########\u001b[38;5;210m::
\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::::::'\u001b[38;5;67m##\u001b[38;5;210m... \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m###\u001b[38;5;210m::'\u001b[38;5;67m###\u001b[38;5;210m::::::::::'\u001b[38;5;67m##\u001b[38;5;210m... \u001b[38;5;67m##\u001b[38;5;210m:. \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m.... \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m.... \u001b[38;5;67m##\u001b[38;5;210m:
\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m::::::: \u001b[38;5;67m##\u001b[38;5;210m:::..:: \u001b[38;5;67m####'\u001b[38;5;67m####\u001b[38;5;210m:::::::::: \u001b[38;5;67m##\u001b[38;5;210m:::..::: \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m:
\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::::::. \u001b[38;5;67m######\u001b[38;5;210m:: \u001b[38;5;67m## ### ##\u001b[38;5;210m:::::::::: \u001b[38;5;67m##\u001b[38;5;210m:::::::: \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m########\u001b[38;5;210m::
\u001b[38;5;210m:. \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m::::::::..... \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m. \u001b[38;5;67m#\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:::::::::: \u001b[38;5;67m##\u001b[38;5;210m:::::::: \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m.. \u001b[38;5;67m##\u001b[38;5;210m:::
\u001b[38;5;210m::. \u001b[38;5;67m## ##\u001b[38;5;210m::: \u001b[38;5;67m##\u001b[38;5;210m:::::::'\u001b[38;5;67m##\u001b[38;5;210m::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m:.:: \u001b[38;5;67m##\u001b[38;5;210m:::::::::: \u001b[38;5;67m##\u001b[38;5;210m::: \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m: \u001b[38;5;67m##\u001b[38;5;210m::. \u001b[38;5;67m##\u001b[38;5;210m::
\u001b[38;5;210m:::. \u001b[38;5;67m###\u001b[38;5;210m:::: \u001b[38;5;67m########\u001b[38;5;210m:. \u001b[38;5;67m######\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:::: \u001b[38;5;67m##\u001b[38;5;210m:'\u001b[38;5;67m#######\u001b[38;5;210m:. \u001b[38;5;67m######\u001b[38;5;210m::'\u001b[38;5;67m####\u001b[38;5;210m: \u001b[38;5;67m########\u001b[38;5;210m:: \u001b[38;5;67m##\u001b[38;5;210m:::. \u001b[38;5;67m##\u001b[38;5;210m:
\u001b[38;5;210m::::...:::::........:::......:::..:::::..::.......:::......:::....::........:::..:::::..::

                                                                     \u001b[38;5;228m*********************
                                                                     \u001b[38;5;228m*\u001b[38;5;219mRanztech Pvt. Ltd.©\u001b[38;5;228m*
                                                                     \u001b[38;5;228m*********************


''')
    temp = ""

    def run():
        global temp
        try:
            temp = int(input(
                "\u001b[38;5;135mEnter number of network (atleast 1 or more):\u001b[38;5;196m"))
        except ValueError:
            print("hmm! Value seems to be numerical or not NULL.")
            run()
    run()
    execute.host(temp)
    execute.subnet()

    # net = 0
    # try:
    #     net = int(input(temp))
