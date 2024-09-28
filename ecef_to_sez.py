# ecef_to_sez.py

# Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km
# Converting from ecef to sez origin positions

# Parameters:
#  o_x_km : int | float | str
#   sez x origin position in kn
#  o_y_km : int | float | str
#   sez y origin position in kn
#  o_z_km : int | float | str
#   sez z origin position in kn
#  x_km : int | float | str
#   ECEF X position in km
#  y_km : int | float | str
#   ECEF Y position in km
#  z_km : int | float | str
#   ECEF Z position in km

# Output:
#  r_s : float
#   s position of 3D position vector
#  r_e : float
#   e position of 3D position vector
#  r_z_
#   z position of 3D position vector

# Written by Riley Parsons

import sys

# "constants"

# helper functions  

# main function
def ecef_to_sez(o_x_km, o_y_km, o_z_km, x_km, y_km, z_km):
  r_s = o_x_km + x_km
  r_e = o_y_km + y_km
  r_z = o_z_km + z_km

  print(round(r_s,3))
  print(round(r_e, 3))
  print(round(r_z, 3))

  return [r_s, r_e, r_z]
  
# initialize script arguments
o_x_km = None
o_y_km = None
o_z_km = None
x_km = None
y_km = None
z_km = None

# parse script arguments
if len(sys.argv)==7:
  o_x_km = float(sys.argv[1])
  o_y_km = float(sys.argv[2])
  o_z_km = float(sys.argv[3])
  x_km = float(sys.argv[4])
  y_km = float(sys.argv[5])
  z_km = float(sys.argv[6])
else:
  print('Usage: python3 ecef_to_sez.py o_x_km o_y_km o_z_km x_km y_km z_km')
  exit()

# write script below this line
if __name__ == '__main__':
  ecef_to_sez(o_x_km, o_y_km, o_z_km, x_km, y_km, z_km)
else:
  ecef_to_sez(o_x_km, o_y_km, o_z_km, x_km, y_km, z_km)