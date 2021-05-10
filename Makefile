FC := gfortran
FFLAGS := -g

LFLAGS := -fopenmp

OBJ1 := leapfrog.f90
TARGET1 := test



$(TARGET1): $(OBJ1)
	$(FC) $(FFLAGS) $(LFLAGS) $^ -o $@



TARGETS := $(TARGET1)

.PHONY: clean

clean:
	\rm -f *.o *.mod $(TARGETS) *.lst


%.o: %.f90 Makefile
	$(FC) $(FFLAGS) -c $< 


