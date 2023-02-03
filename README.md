# Atom-s-trajectories
The repository consist numberical methods do describe "random" trajectories and forces of points(molecules) in cubic 20x20 units
file: “task1a.py”Pseudo-random number generator

The program generates random numbers. To achieve it, I used the
linear consequential generator, what is based on formula:

Where X is the sequence of pseudo-random values. I tested different variants
of the coefficients: a, c, and m, to observe how “randomness” is conditioned (in the equation).
Some coefficients were creating short repeated period.

m coefficient conditioned the maximum value of generated number. The generator produces a
uniform distribution of integers from 0 to m-1.
The diversity of the period conditioned by m value were dependent on a and c coeficients. The most
various numbers were generated for a and c coef., which were high, prime numbers.
To resolve the issue of repeated period, what made the collection of numbers more monotonous, we
decided to extract only the first period form the generated sequence.

The code generate the random numbers by upper formula, extract period (to avoid repeatable
sequences of numbers). Variety of generated numbers is visualized by generated plot, which shows
each value of generated values.

 Randomness checker - distribution
To check the randomness of the numbers, I used the determination distribution tool, what showed
us the graph of abundance of the numbers. This method uses numpy.histogram to bin the data
in x and count the number of values in each bin, then draws the distribution.

file: , “task1b.py” 

The code is another, more manual way to visualize the randomness of the numbers. The code
randoms the numbers, part the period onto 4 parts, by 3”division border values”.
Code generate the matrix 20x20 filled by zeros – what is an area consisted of 4000 places. Each
place can be describes by x and y coordinated with values from 0 to 19 (python’ description of list).
The code generate the initial position at place 9,9.
Generated earlier 3 “division borders” by division of max value (what is determined by m value)
into 4 parts. Division borders allow to create 4 bins.
If the generated value is less than first division border, the initial position value has been changed at
1 value higher (10,9), and the new position gets upper value (every 1). If the value is bigger than
first border, but less then second the position goes down. For value between second and third
border, position goes left, and for last condition goes right.
The code generate matrix which describes the randomness of the period, the matrix is translated into
graph(below).

File: "task2.py" Line trend generator

The code calculates linear coefficients from sets of x and y data. Code is based on below equation:

Calculated coefficients are used to generate the trend line. There are graphs for gives set of data.

The generated trend-lines have similar equations. The second graph shows polynomial set of data,
what makes generated linear trend line ridiculous. The third graph shows linear data, but last record
has not adequate big value, what changes curve, and does not make it fitted.
The last graph is the same set of data, but have been removed third data, what makes line perfectly
fitted.

files: “interpolation_left.py”, interpolation_right.py Lagrange Polynomial Interpolation Program

The code uses Lagrange polynomial interpolation to finds a single polynomial that goes through all
the data points. Lagrange interpolation polynomials are defined outside the area of interpolation,
that is outside of the interval , will grow very fast and unbounded outside this region. This is not a
desirable feature because in general, this is not the behavior of the underlying data. Thus, a
Lagrange interpolation should never be used to interpolate outside this region.

For another, simplified code, prediction is exact, but after deep analysis, I still don’t
have any idea why these codes works different.
The second code gives exact interpolation. file "interpolation_rigth.py"

file: “integral.py”  Integral calculation – trapezoidal rule:

The code calculate the integral by trapezoidal rule:
where a and b determines the boundary values (start and end) for integral calculations. N is number
of steps.
The code calculates relative error, for decreasing value of del xk,and generates the graph of the
dependency of the relative error and step value (del xk).
Graph for function sin(x) from 0 to
pi/2:

We can observe that for smaller
values of step the relative error is
equal 0.

Program also calculates the time of calculations, and draw the plot of dependency of the time and
number of step:

We can observe that time of
the calculation rise with
number of steps.

File: vine.py Creation of kinetic model for nitrogen-limited Wine Fermentations

The code creates the graph what describes the concentration of sugar[g/l](yellow), nitrogen [mg/l]
(green), ethanol [g/l](red), and biomass [g/l](blue) in dependency of time.
Model uses the equation and constants from publication.
Kinetic Model for Nitrogen-Limited Wine Fermentation

“trajectory.py Trajectory generation



Trajectory generation (file: “trajectory.py”)
The code write down the trajectory file for point-like objects. The trajectory file describes position
of point per frame. Position of point is described by spatial coordinates (x,y,z). The trajectory of the
points is determined by initial velocities, which are determined randomly in range from 0 to 2 in all
3 – dimensions. The point changes position by addition initial velocity per frame to previous(initial)
position.
The way of acting of points is determined by Newton’s Laws of motion:
F=m*a
where Force is proportional to mass and acceleration.
Second law of motion describes that Fore is derivative of mass and velocity by time.
We also know that venosity(v) is derivative of distance(s) and time(t).
So displacement will be proportional to derivative of time times velocity. In our case dt=frame=1.
So for every frame distance will be:
s=frame*velocity
Program creates trajectory file for arbitrary number of points (in code described by nop,and
generates random number form 1 to 10), and save every movement (frame) for all molecules.
The output file (trajfile) can be an input file for visualization program, like VMD.
The output file stands out the input file, additionally the user have to switch on readable for points
representation, and set up the box boundaries for all molecules by below commands:
vmd > pbc set {20 20 20} -all
vmd > pbc box_draw


More over second code take accond L-J potential and gives ability to estimate forces between particles. 






