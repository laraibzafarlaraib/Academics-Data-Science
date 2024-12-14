import struct

with open('LaraibBinary.txt', 'wb') as file:
    # Write the string '123' to the file
    a = '123'
    a_bytes = a.encode()
    file.write(a_bytes)
    print(a_bytes)

    # Write the list of strings and integers using struct.pack
    s = ['Larib', 'laiba', 'aima']
    r = [12, 13, 14]

    for string_value, int_value in zip(s, r):
        # Adjust the format string based on your specific requirements
        fmt = '10s I'
        packed_data = struct.pack(fmt, string_value.encode(), int_value)
        file.write(packed_data)

    # Write additional packed data
    fmt_additional = '1s 40s f'
    h = b's'
    larab = b'r'
    br1 = struct.pack(fmt_additional, h, larab, 3.000)
    file.write(br1)

  

  
