from mfrc522 import MFRC522
import utime
import machine
import time
              
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
btn = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
first_sector_key = []
next_sector_key = []

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

def brute_force_key():
    keys = [
        [0xff, 0xff, 0xff, 0xff, 0xff, 0xff], # FF FF FF FF FF FF
        [0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5], # A0 A1 A2 A3 A4 A5
        [0xb0, 0xb1, 0xb2, 0xb3, 0xb4, 0xb5], # B0 B1 B2 B3 B4 B5
        [0x4d, 0x3a, 0x99, 0xc3, 0x51, 0xdd], # 4D 3A 99 C3 51 DD
        [0x1a, 0x98, 0x2c, 0x7e, 0x45, 0x9a], # 1A 98 2C 7E 45 9A
        [0xd3, 0xf7, 0xd3, 0xf7, 0xd3, 0xf7], # D3 F7 D3 F7 D3 F7
        [0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff], # AA BB CC DD EE FF
        [0x00, 0x00, 0x00, 0x00, 0x00, 0x00], # 00 00 00 00 00 00
        [0xa0, 0xb0, 0xc0, 0xd0, 0xe0, 0xf0], # a0 b0 c0 d0 e0 f0
        [0xa1, 0xb1, 0xc1, 0xd1, 0xe1, 0xf1], # a1 b1 c1 d1 e1 f1
        [0x71, 0x4c, 0x5c, 0x88, 0x6e, 0x97], # 71 4c 5c 88 6e 97
        [0x58, 0x7e, 0xe5, 0xf9, 0x35, 0x0f], # 58 7e e5 f9 35 0f
        [0xa0, 0x47, 0x8c, 0xc3, 0x90, 0x91], # a0 47 8c c3 90 91
        [0x53, 0x3c, 0xb6, 0xc7, 0x23, 0xf6], # 53 3c b6 c7 23 f6
        [0x8f, 0xd0, 0xa4, 0xf2, 0x56, 0xe9], # 8f d0 a4 f2 56 e9
    ]
    
    global first_sector_key
    global next_sector_key
    
    print("\n")
    print(100*"_")
    print("*****BRUTE FORCING KEY*****")
    print("")
    print("Place card into reader")
    print("")
    
    print("Starting in 3")
    time.sleep(1)
    print("Starting in 2")
    time.sleep(1)
    print("Starting in 1")
    time.sleep(1)
    
    (stat, tag_type) = reader.request(reader.REQIDL)
    
    if stat == reader.OK:
        for key in keys:
            (stat, tag_type) = reader.request(reader.REQIDL)
            if stat == reader.OK:
                (stat, uid) = reader.SelectTagSN()
                if stat == reader.OK:
                    print("Trying: ")
                    print("KEY_A: " + str(key))

                    #read MAD sector  (first sector)
                    if len(first_sector_key) == 0 and reader.MFRC522_DumpClassic1K(uid, Start=0, End=4, keyA=key) == reader.OK:
                        first_sector_key = key
                        
                    if len(next_sector_key) == 0 and reader.MFRC522_DumpClassic1K(uid, Start=4, End=64, keyA=key) == reader.OK:
                        next_sector_key = key
                        
                    if len(first_sector_key) != 0 and len(next_sector_key) != 0:
                        break
                            
    print("First sector key:")
    print(first_sector_key)
    print("Next sector key:")
    print(next_sector_key)
    
    print("\n")
    print("Press button to change mode or press button to change mode")
    
    while True:
        if btn.value():
            write_data()
            return 0
    
def write_data():
    print("\n")
    print(100*"_")
    print("*****WRITING*****")
    print("")
    
    global first_sector_key
    global next_sector_key
    
    sector = int(input("Enter first sector (1) or next sectors (2): "))
    block_number = int(input("Enter absolote block number: "))
    data = input("Enter data to write seperate by space: ").split(" ")
    
    for i in range(len(data)):
        data[i] = int(data[i])
        
    if sector == 1:
        key = first_sector_key
    else:
        key = next_sector_key
    
    print("")
    print("Place card into reader")
    print("")
    
    try:
        while True:

            (stat, tag_type) = reader.request(reader.REQIDL)

            if stat == reader.OK:
                (stat, uid) = reader.SelectTagSN()
                if stat == reader.OK:
                    print("Card detected 0x%s" % uidToString(uid))
                    absoluteBlock=block_number
                    value=data
                    for i in range(16):
                        value.append(i)
                    status = reader.auth(reader.AUTHENT1A, absoluteBlock, key, uid)
                    if status == reader.OK:
                        status = reader.write(absoluteBlock,value)
                        if status == reader.OK:
                            print("Data written successfully")
                        else:
                            print("Unable to write")
                    else:
                        print("Authentication error for writing")
                    break
                    
            if btn.value():
                read_data()
                break
                return 0
            
    except KeyboardInterrupt:
        print('Bye')
    
def read_data():
    print("\n")
    print(100*"_")
    print("*****READING*****")
    print("")
    print("Place card into reader or press button to change mode")
    print("")

    PreviousCard = [0]

    try:
        while True:

            reader.init()
            (stat, tag_type) = reader.request(reader.REQIDL)
            if stat == reader.OK:
                (stat, uid) = reader.SelectTagSN()
                if uid == PreviousCard:
                    continue

                if stat == reader.OK:
                    print(uid)
                    print("Card detected []  uid=[]".format(hex(int.from_bytes(bytes(uid),"little",False)).upper(),reader.tohexstring(uid)))
                    firstSectorKey = [0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5]
                    nextSectorKey = [0xD3, 0xF7, 0xD3, 0xF7, 0xD3, 0xF7]
                    #defaultKey = [255,255,255,255,255,255]

                    #read MAD sector  (first sector)
                    if reader.MFRC522_DumpClassic1K(uid, Start=0, End=4, keyA=firstSectorKey)== reader.OK:
                        #read the rest of the card
                        reader.MFRC522_DumpClassic1K(uid, Start=4, End=64, keyA=nextSectorKey)
                    print("Done")
                    PreviousCard = uid
            else:
                PreviousCard=[0]
            utime.sleep_ms(50)                

            if btn.value():
                brute_force_key()
                break
                return 0
                
    except KeyboardInterrupt:
        print('Bye')
    
brute_force_key()
