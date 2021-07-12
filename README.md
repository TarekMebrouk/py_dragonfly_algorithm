<H1> DragonFly algorithm </h1>
  <H6> University of Science and Technology USTHB </H6>
  <H6> IT department </H6>
  <H6> End-of-study project in license year (2020/2021) </H6>
  
<H3> Source of inspiration </H3>
<br>
The main inspiration of the Dragonfly Algorithm (DA) proposed in
2015 comes from the teeming behaviors of a dragonfly. The reason for their swarming
is either migration or hunting (dynamic swarm or static swarm respectively). In a static swarm, small groups of dragonflies move on a small
area to hunt other insects. The behaviors of this type of swarming include
local movements and sudden changes. In dynamic swarming,
however, a massive number of dragonflies create a single group and move to a
direction over a long distance.
According to Reynolds, the behavior of swarms follows three primitive principles:
✓ Separation, which refers to the static avoidance of collisions between
individuals and other individuals in the neighborhood.
✓ Alignment, which indicates the pairing of the speed of individuals to that of others
individuals from the neighborhood.
✓ Cohesion, which refers to the tendency of individuals towards the center of mass of the
district.
<br>

<H3> Fonctionnement </H3>
<br>
The basis of this algorithm is based on the spatial approximation of the
dragonflies to food sources and escape from danger (enemy) while exploiting
aspects of displacement which are separation, cohesion and alignment.
In order to benefit from the strong points of this algorithm, we made a projection on it on
our problem investigated and we decided to proceed as follows:
- The notion of position in space of dragonflies will be replaced by our function
objective (PSNR).
- The best and the worst solution found in a population will be defined as
source of food and danger.
- To keep the actions of moving towards the food source, we have
implemented:
▪ A method of inheriting the good characteristics of the best solution
neighbor in order to get closer.
▪ A history of all bad solutions is maintained in order to
move away from enemies.
- The diversification aspect managed by the Lévy flight results in reconstruction
random of the solution.
<br>

<H3> Intensification / diversification aspect </H3>
<br>
To move from intensification to diversification, dragonflies must change their weight from
adaptively. This ensures the convergence of dragonfly individuals during the
optimization process. As the optimization process progresses, to
adjust the flight path, the neighborhood area is enlarged, so at the final stage of
optimization, the swarm becomes a group to converge towards a global optimum. The
best and worst solutions found so far respectively become the source
food and the enemy. This encourages convergence and divergence towards the area
promising and the non-promising outward area of the research space
respectively.
<br>

<H3> Advantages and disadvantages : </H3>
DA is one of the most recently developed algorithms, it has been used to optimize
various problems in different fields. One of the reasons why this algorithm could contribute to different applications is that it is very simple, easy to implement and suitable for applications in different fields. In addition, having few parameters for tuning is another advantage of DA. The convergence time of the algorithm is reasonable. 
Compared to other optimization algorithms, it is faster and can easily be merged with other algorithms.
On the other hand, it does not have any internal memory which could lead to convergence premature towards the local optimum. This drawback has been overcome by proposing a New Memory-Based Dragonfly Hybrid Algorithm (MHDA). In addition, DA is easily stuck in the local optima because it has a high exploitation rate. The mechanism Levy flight was used to model the random flight behavior of dragonflies in nature. 
The disadvantages of the Levy flight are the overflow of the search area and the interruption of random flights due to its major research steps.


