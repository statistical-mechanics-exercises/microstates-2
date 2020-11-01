# Representing microstates using a single number

We have learned during the course that the central quantity in statistical mechanics is the partition function, which is calculated as:

![](https://render.githubusercontent.com/render/math?math=Z=\frac{j=1}^Me^{-\beta\H(\mathbf{x}_j)})

The sum in this expression runs over M of the microstates, ![](https://render.githubusercontent.com/render/math?math=x_j), that the system can adopt.  H is the Hamiltonian and ![](https://render.githubusercontent.com/render/math?math=\beta) is the inverse temperature.  In the next few exercises we are going to learn how to compute this quantity using a computer.  Before we get on that, however, we first need to learn how to write a single loop that will generate all the microstates that our system of spins can adopt.

With that in mind notice that if we compute b using the following equation:

![](https://render.githubusercontent.com/render/math?math=b=\sum_{j=1}^N2^{j-1}z(s_j)\qquad\textrm{where}\qquad\z(0)=-1\qquad\textrm{and}\qquad\z(1)=1)

it takes a different value for each of the microstates that our system can adopt.  Notice that the sum here runs over the N spin coordinates, ![](https://render.githubusercontent.com/render/math?math=s_j), in the list that defines our spin state.

Modify the code in the box on the upper right so that the function called `compute_b` calculates the the quantity, b, that is defined in the formula above.  Notice that this function takes a list called `spins`, which contains all the spin coordinates.  I have called this function with each of the 8 microstates that are possible for a system of three spins so that you can convince yourself that b takes a different value for each of these different states.
