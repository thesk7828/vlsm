class calc:
    nHost = list() # grabs the hosts from user input
    # ip=list() # Splits IP octate's and stores in list with type 'int'
    #ip_addr=list() # Splits IP octate's and stores in list with type 'String'
    networks=0 # intiating network with NULL value
    total_host=0 # Specifies sum of all hosts from all the network
    cidr=list() # Holds CIDR value for a particlar Host
    val=int(0) # Used for general calculation

    # Holding and Sorting the HOSTS in Decreasing manner 
    def host(self,networks):
        self.networks=networks
        print("\nEnter the number of host for all ",self.networks," networks-")
        for i in range(0, int(self.networks)):
            print("NETWORK ",i+1,": ")
            temp = input()
            self.nHost.append(int(temp))
        self.nHost.sort(reverse=True)
        tHost=0
        print("\nArranging Host in sequence -")
        for i in range(0, len(self.nHost)):
            print("NETWORK ",i+1,": ",self.nHost[i])
            tHost=self.nHost[i]+tHost
        self.total_host=int(tHost)
        print("\nTotal Hosts are ",self.total_host,"\n")

        # Here all the calculation related to Subnetting finding CIDR value for specific host and converting
        # CIDR value to Subnet Mask takes place
    def subnet(self):

        # // The following code is to get the IP from the user -
        #print('''\nNow enter the favorable IP with respect to number of host mentioned above!
        #where last octate should be '0' (zero)
        #Example: 10.23.124.0 or 128.232.2.0 or 192.168.1.0\n''')
        #sam=input("enter IP : ")
        #ip_addr=sam.split(".")
        #ip=list()
        #for x in range(0, len(ip_addr)):
        #    temp=ip_addr[x]
        #    ip.append(int(temp))
        #if ((ip[0]<1 or ip[0]>255 or ip[0]==127) or (ip[1]<0 or ip[1]>255) or (ip[2]<0 or ip[2]>255) or (ip[3]<0 or ip[3]>255)):
        #    print("Illegel parameter!")
        #    raise SystemExit
        
        # Finding CIDR Values
        for x in range(0, len(self.nHost)):
            temp=self.nHost[x]
            cidr=32
            host_bit=1
            flag=2
            for x in range(1, 32):
                if flag > temp:
                    cidr=cidr-host_bit
                    self.cidr.append(int(cidr))
                    break
                else:
                    flag=flag*2
                    host_bit=host_bit+1
        
        # CIDR Value to Subnet Mask Conversion
        for x in range(0, len(self.cidr)):
            print("CIDR for ",self.nHost[x]," host is /",self.cidr[x])
            temp=self.cidr[x]
            if ((temp > 24) and (temp <= 32)):
                remain = 8 - (32-temp)
                self.calci(remain)
                print("Subnet Mask: 255 . 255 . 255 .",self.val,"\n")
                self.val=0
            elif ((temp > 16) and (temp <= 24)):
                remain = 8 - (24-temp)
                self.calci(remain)
                print("Subnet Mask: 255 . 255 .",self.val,". 0\n")
                self.val=0
            elif ((temp > 8) and (temp <=16)):
                remain = 8 - (16-temp)
                self.calci(remain)
                print("Subnet Mask: 255 .",self.val,". 0 . 0\n")
                self.val=0
            else:
                remain = 8 - temp
                self.calci(remain)
                print("Subnet Mask:",self.val,". 0 . 0 . 0\n")
                self.val=0
    
    # Function call for Subnet Mask Calculation
    def calci(self,bit):
        remain=bit
        sub=int(128)
        x=0
        while x<remain:
            self.val=int(self.val+sub)
            sub=sub/2
            x+=1

# // Initiating code from here -
if __name__ == "__main__":
    execute=calc()
    networks=input("Enter number of network (atleast 1 or more):")
    execute.host(networks)
    execute.subnet()
