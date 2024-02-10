__author__ = "Swarup Maity"
__copyright__ = "Copyright (c) 2023 Swarup Maity"
__version__ = "1.1"


import pyubx2

def process_ubx_file(file_path):
    with open(file_path, 'rb') as ubx_file:
        ubxreader = pyubx2.UBXReader(ubx_file, protfilter=3)

        msg_count = 0
        delta_count_msg = 1
        prev_count = -999
        count1 = 0
        delta_count = []

        for raw_data, parse_data in ubxreader:
        
            if raw_data[0] ==0xb5 and raw_data[1] == 0x62 and raw_data[2] == 0x0d and raw_data[3] ==0x03:  # Check UBX message header
                count = parse_data.get("count", -999)  # Extract count property
                if prev_count != -999:
                    diff = count - prev_count
                    print("Difference:", diff)
                    if diff >= 1:
                        delta_count.append(diff)
                        delta_count_msg += 1
                    else:
                        count1 += 1
                        print("Count1 =", count1)
                prev_count = count
                print(parse_data)
                msg_count += 1

        print("Total number of TIM-TM2 messages:", msg_count)
        print("After deleting similar rising edges:", delta_count_msg)
        print("Delta count:", delta_count)

# Example usage:
process_ubx_file("AARAV-ENX6M_raw_20240207111548.ubx")
