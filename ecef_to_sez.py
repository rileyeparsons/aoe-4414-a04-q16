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
import math

# "constants"
R_E_KM = 6378.137
E_E    = 0.081819221456

# helper functions  
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-(ecc**2)*(math.sin(lat_rad)**2))

def ecef_to_llh(r_x_km, r_y_km, r_z_km):
 # calculate longitude
 lon_rad = math.atan2(r_y_km,r_x_km)
 lon_deg = lon_rad*180.0/math.pi
 
 # initialize lat_rad, r_lon_km, r_z_km
 lat_rad = math.asin(r_z_km/math.sqrt(r_x_km**2+r_y_km**2+r_z_km**2))
 r_lon_km = math.sqrt(r_x_km**2+r_y_km**2)
 prev_lat_rad = float('nan')
 
 # iteratively find latitude
 c_E = float('nan')
 count = 0
 while (math.isnan(prev_lat_rad) or abs(lat_rad-prev_lat_rad)>10e-7) and count<5:
   denom = calc_denom(E_E,lat_rad)
   c_E = R_E_KM/denom
   prev_lat_rad = lat_rad
   lat_rad = math.atan((r_z_km+c_E*(E_E**2)*math.sin(lat_rad))/r_lon_km)
   count = count+1
   
 # calculate hae
 hae_km = r_lon_km/math.cos(lat_rad)-c_E

 return [lon_deg, lat_rad*180.0/math.pi, hae_km]

def simple_rot(three_three_mat, three_one_mat):
  """
  no numpy :(
  """
  r1 = three_three_mat[0][0]*three_one_mat[0] + three_three_mat[0][1]*three_one_mat[1] + three_three_mat[0][2]*three_one_mat[2]
  r2 = three_three_mat[1][0]*three_one_mat[0] + three_three_mat[1][1]*three_one_mat[1] + three_three_mat[1][2]*three_one_mat[2]
  r3 = three_three_mat[2][0]*three_one_mat[0] + three_three_mat[2][1]*three_one_mat[1] + three_three_mat[2][2]*three_one_mat[2]
  return [r1, r2, r3]

# main function
def ecef_to_sez(o_x_km, o_y_km, o_z_km, x_km, y_km, z_km):
  ecef_x_km = x_km - o_x_km
  ecef_y_km = y_km - o_y_km 
  ecef_z_km = z_km - o_z_km

  llh = ecef_to_llh(o_x_km, o_y_km, o_z_km)
  
  # not putting this part in a function dont feel like it
  Rz_inv = [
    [math.sin(llh[1]*(math.pi/180)), 0, -math.cos(llh[1]*(math.pi/180))], 
    [0, 1, 0], 
    [math.cos(llh[1]*(math.pi/180)), 0, math.sin(llh[1]*(math.pi/180))]
  ]

  Ry_inv = [
    [math.cos((llh[0])*(math.pi/180)), math.sin((llh[0])*(math.pi/180)), 0], 
    [-math.sin((llh[0])*(math.pi/180)), math.cos((llh[0])*(math.pi/180)), 0],
    [0, 0, 1]
  ]

  sez = simple_rot(Rz_inv, simple_rot(Ry_inv, [ecef_x_km, ecef_y_km, ecef_z_km]))
  print(sez[0])
  print(sez[1])
  print(sez[2])

  return sez
  
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