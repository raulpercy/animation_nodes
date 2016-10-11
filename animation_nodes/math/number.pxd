from libc.math cimport M_PI as PI
from libc.math cimport (sin, cos, tan, asin, acos, atan, atan2, hypot,
                        pow)

cdef double PI_HALF, PI_QUARTER

cdef double add(double x, double y)
cdef double subtract(double x, double y)
cdef double multiply(double x, double y)
cdef double divide_Save(double x, double y)

cdef double asin_Save(double x)
cdef double acos_Save(double x)

cdef double power_Save(double base, double exponent)