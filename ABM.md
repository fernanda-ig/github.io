---
layout: default 
title: Agent-Based Model
---
**Agent-Based Model**
======

Hereinafter I will explain an Agent-Based Model, which is based on the Programming for Social Scientists course (University of Leeds, 2019).

An Agent-Based Model is a technique used to analyse individuals’ behaviours and interactions of entities, usually called as agents, inside a specific area, usually called environment, between the repetition of these interrelations they emulate a specific system. These kinds of modelling techniques are commonly used to understand complex phenomenon of real-life situations (Bonabeau, 2002).

In the next lines, I will explain an Agent-Based Model that emulated the dynamics of a hypothetical population. It is important to highlight that the script I will show has a neutral codification of the variables but in order to do a better explanation of the dynamics of this theoretical population I will adequate the names of my variables.

I built this Agent-Based Model to emulate an imaginary city which was formed by two kinds of agents which their main difference was their diet, which could be vegetarian or omnivore. Regarding the city dynamics, both kinds of individuals were able to move and interact with each other, although they had slight variations on their behaviours.

On one hand, omnivorous people were able to move around their environment and ate their environment, this last behaviour was a metaphor among the link of food production, global warm and environment exploitation (Salonen and Helne, 2012). Also, they were able to get close to their neighbours and to share resources with them. On the other hand, vegetarian people were able to move faster than their counterparts and had a main purpose of influencing omnivorous individuals to adopt vegetarianism. Nevertheless, they were able to achieve this goal only when they reached omnivorous individuals. Also, their influence objective was finite, because they stopped that behaviour when they at least duplicate their population.

In order to build this model, firstly I defined the variables which were the input to run my model. In this sense, I established that this city had a population of 15 persons. Then I determined that 10 of them had an omnivore diet and 5 of them had a vegetarian diet. Then, I defined that the total omnivorous individuals were open to change their dietary pattern to vegetarianism, therefore I set 10 available positions to be converted *-coded as num_of_chased-* as a new vegetarian. Even though, the complete population of omnivorous were able to adopt vegetarianism I set a condition that protected them to be influenced, which was a safety area of 20 *-coded as ep_area-*. In other words, this area was the maximum distance in which vegetarian individuals were not able to influence omnivorous individuals.

![fig_1](/assets/fig_1.jpg)

In the second place, I defined the behaviours for each group of the population. As I have stated the omnivorous people *-coded as agents-* were able to move, eat their environment and share resources with their neighbours. Nevertheless, their moving behaviour was slow therefore it was set in two steps as it is showed in the next piece of code.

![fig_2](/assets/fig_2.jpg)

Meanwhile, vegetarian people *-coded as agents2-* were able to move faster than their counterparts therefore they were able to move in ten steps, this is also showed in the next code. 

![fig_3](/assets/fig_3.jpg)

Besides, vegetarian people were able to persuade *-coded as chase-* omnivorous people to modify their dietary patterns. Nevertheless, the latter behaviour happened when they get close to omnivorous people, in a distance *-coded as dist2-* which had to be below or equal to the safety area. 

![fig_4](/assets/fig_4.jpg)

In the third place, I established the stopping condition to the model when vegetarian individuals achieved their influenced goal. This was accomplished when the number omnivorous individuals who adopted a vegetarian diet was equal or higher than the vegetarian total population.

![fig_5](/assets/fig_5.jpg)

The next graphic depicts one trial of the city dynamics. In order to interpret the graphic, it is necessary to note that the plus marker in red represents omnivorous individuals which are four, then the diamonds marker in green represents vegetarian individuals which remain at the same level as it was defined at the beginning of the script, five, and finally the thin diamonds marker in blue describes the 6 omnivorous individuals that were pursued to transit towards a vegetarian diet.

![fig_6](/assets/fig_6.jpg)

Finally, if you want to run my code or based on it to build another Agent-Based Model you can access to my repository. There are two script files regarding the model, one of them called *agent framework*, in which I established the behaviours for each agent and another file that is called *model* in which I defined the rest of the model.

**Note:** It is important to highlight that the Agent-Based Model that I presented here, was a hypothetical example which is not supported by scientific evidence regarding dietarian consumptions behaviours. 

**References.**
1. Bonabeau, E., 2002. Agent-based modeling: Methods and techniques for simulating human systems. Proc. Natl. Acad. Sci. 99, 7280–7287. https://doi.org/10.1073/pnas.082080899
2. Salonen, A.O., Helne, T.T., 2012. Vegetarian Diets: A Way towards a Sustainable Society. J. Sustain. Dev. 5, p10. https://doi.org/10.5539/jsd.v5n6p10
3. University of Leeds, 2019. Programming for Social Science: Core Skills. URL https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/


