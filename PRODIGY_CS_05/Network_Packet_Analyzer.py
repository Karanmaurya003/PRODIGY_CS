#IMPORT all the neccesarry methods and protocols
from scapy.all import sniff, IP, ICMP, TCP, UDP, get_if_addr, get_if_list
#List the availabe interfaces
def List_Available_Interface():
    print(f"\nAvailable Interfaces")
    interfaces = get_if_list()
    active_interfaces = []
    active_descriptions = []
    for iface in interfaces:
        try:
            ip_address = get_if_addr(iface)
            #filter invalid IP's and only store logical IP's which are useful
            if ip_address and ip_address != "0.0.0.0" and not ip_address.startswith("169.254"):
                description = f"\n{iface}- IP: {ip_address} (Active)"
            else:
                continue
            active_interfaces.append(iface)
            active_descriptions.append(description)
        except:
            continue
    if active_interfaces:
        for i,description in enumerate(active_descriptions):
            print(f"\n{i+1}. {description}")
    else:
        print(f"\nNo active interface found for sniffing")      
    return active_interfaces, active_descriptions
#Select interface
def select_interface(interfaces):
    while True:
        try:
            option = int(input("\nEnter the number to choose the Interface"))
            if 1 <= option <= len(interfaces):
                return interfaces[option - 1]
            else:
                print("\nOption out of Range. Please select the Appearing Options")
                return
        except ValueError:
            print(f"\nPlease enter a valid number")
    

#define the callback function for the network analyzing
def analyze_network(packet):
    
    #check for the ip layer
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        #protocol = ip_layer.proto
        
        #Display the source and the destination IP's
        print(f"\nPackets Captured")
        print(f"\nSource IP: {src}")
        print(f"\nDestination IP: {dst}")

        #check for the specific protocols
        if TCP in packet:                          #for TCP protocols
            tcp_layer = packet[TCP]
            print(f"\nSource Port: {tcp_layer.sport}")
            print(f"\nDestination Port: {tcp_layer.dport}")
        elif UDP in packet:                        #for UDP protocols
            udp_layer = packet[UDP]
            print(f"\nSource UDP: {udp_layer.sport}")
            print(f"\nDestination UDP: {udp_layer.dport}")
        elif ICMP in packet:                       #for ICMP protocols
            print(f"\nProtocol: ICMP")
        else:
            print(f"\nOther Protocol")             #for other protocols
        #check if packet payload is present the display the payload data (only first 50 characters)
        if packet.payload:
            print(f"\nPayload Data: {bytes(packet.payload)[:50]}") 

#define the working of snipper when called 
def start_sniffer(interface):
    
    print(f"\nStarting the sniffer on the given {interface} interface")
    print(f"\nPress Ctrl+C to exit")
    #defining the main work of the sniffer and callback funtion
    sniff(iface = interface, prn = analyze_network, store = 0) #not storing the payload in the memory

#program execution starts here
if __name__ == "__main__":
    print(f"\nPacket Sniffer Tool -(Only For Education Purpose)")           #Reminding the Ethical Use for safety purpose
    print(f"\n(Only use for Ethical Use)")
    active_interface, active_description = List_Available_Interface()
    selected_interface  = select_interface(active_interface)

    #Handling the case effectively
    if active_interface:
        try: 
            #starting the sniffer  
            start_sniffer(selected_interface)
        #Handling the error    
        except PermissionError:
            print(f"\nPermission Denied: You need administrative privileges to sniff packets")
        except KeyboardInterrupt:
            print(f"\nSniffer stopped by the user")
        except Exception as e:
            print(f"\nError occured while sniffing : \n\t{e}")
    else:
                #incase no interfaces are found
                print("\nNo active interfaces available for sniffing.")

    

    


        
        

        



