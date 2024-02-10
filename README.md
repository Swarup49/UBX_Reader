# UBX_Reader

This script is designed to process UBX (u-blox binary) files and extract specific information from them. It utilizes the pyubx2 library for parsing UBX messages.

# Description

The script process_ubx_file reads a UBX file specified by the file_path parameter, parses it using pyubx2, and extracts specific information related to TIM-TM2 (time mark) messages.

The script iterates through each message in the UBX file.
It checks for messages with the UBX message header 0xb5 0x62 0x0d 0x03.
It extracts the "count" property from each message and calculates the difference between consecutive counts.
Messages with a count difference of at least 1 are considered as "rising edges" and are recorded.
The script prints the total number of TIM-TM2 messages, the number of distinct rising edges, and the list of delta counts.

# Example Usage
python
Copy code
process_ubx_file("m2_raw_2k03hr4.ubx")
Replace "m2_raw_2k03hr4.ubx" with the path to your UBX file.

# Dependencies
pyubx2 library is required. Install it using pip install pyubx2.

# License
This script is provided under the MIT License. See the LICENSE file

# References
https://content.u-blox.com/sites/default/files/NEO-M8-FW3_DataSheet_UBX-15031086.pdf

https://pypi.org/project/pyubx2/0.1.0/
