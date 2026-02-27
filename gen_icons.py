#!/usr/bin/env python3
"""Generate MathUp PWA icons as PNG files."""

import struct, zlib, math, os

def png_chunk(chunk_type, data):
    c = chunk_type + data
    crc = zlib.crc32(c) & 0xffffffff
    return struct.pack('>I', len(data)) + c + struct.pack('>I', crc)

def make_png(size):
    w = h = size
    pixels = []
    cx, cy = w/2, h/2
    r_outer = w * 0.46
    r_inner = w * 0.28
    
    for y in range(h):
        row = []
        for x in range(w):
            dx, dy = x - cx, y - cy
            dist = math.sqrt(dx*dx + dy*dy)
            
            # Background circle
            if dist <= r_outer:
                # Gradient: orange top-left to dark orange bottom-right
                t = (x/w * 0.5 + y/h * 0.5)
                r_col = int(255 - t * 40)
                g_col = int(107 + t * 10)
                b_col = int(53 - t * 10)
                a = 255
                
                # Inner white circle
                if dist <= r_inner:
                    r_col, g_col, b_col = 255, 255, 255
                
                # Draw "M" shape in white (simplified as rects)
                # M letter bounds relative to center
                lw = w * 0.05  # line width
                mh = w * 0.22  # M height
                mw = w * 0.28  # M width
                
                mx1 = cx - mw/2
                mx2 = cx + mw/2
                my1 = cy - mh/2
                my2 = cy + mh/2
                
                in_m = False
                # Left vertical bar
                if mx1 <= x <= mx1 + lw and my1 <= y <= my2:
                    in_m = True
                # Right vertical bar  
                if mx2 - lw <= x <= mx2 and my1 <= y <= my2:
                    in_m = True
                # Left diagonal (from top-left going down-right to center)
                mid_x = cx
                mid_y = cy - mh * 0.05
                # Simplified: two diagonal bars
                slope_l = (mid_y - my1) / (mid_x - mx1)
                slope_r = (mid_y - my1) / (mid_x - mx2)
                
                # Left diagonal bar
                expected_y_l = my1 + slope_l * (x - mx1)
                if mx1 <= x <= mid_x and abs(y - expected_y_l) <= lw * 1.5:
                    in_m = True
                # Right diagonal bar
                expected_y_r = my1 + slope_r * (x - mx2)
                if mid_x <= x <= mx2 and abs(y - expected_y_r) <= lw * 1.5:
                    in_m = True
                
                if in_m and dist > r_inner * 0.3:
                    r_col, g_col, b_col = 255, 255, 255
                    
            else:
                r_col, g_col, b_col, a = 0, 0, 0, 0
                # Transparent
                row.extend([0, 0, 0, 0])
                continue
            
            row.extend([r_col, g_col, b_col, a])
        pixels.append(row)
    
    # Build PNG
    ihdr_data = struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)  # RGB no alpha
    # Use RGBA
    ihdr_data = struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0)
    
    raw_data = b''
    for row in pixels:
        raw_data += b'\x00' + bytes(row)
    
    compressed = zlib.compress(raw_data, 9)
    
    png = b'\x89PNG\r\n\x1a\n'
    png += png_chunk(b'IHDR', ihdr_data)
    png += png_chunk(b'IDAT', compressed)
    png += png_chunk(b'IEND', b'')
    return png

os.makedirs('icons', exist_ok=True)
for size in [72, 96, 128, 144, 152, 192, 384, 512]:
    data = make_png(size)
    with open(f'icons/icon-{size}.png', 'wb') as f:
        f.write(data)
    print(f'Generated icon-{size}.png')
print('Done!')
