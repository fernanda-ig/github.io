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

In order to build this model, firstly I defined the variables which were the input to run my model. In this sense, I established that this city had a population of 15 persons. Then I determined that 10 of them had an omnivore diet and 5 of them had a vegetarian diet. Then, I defined that the total omnivorous individuals were open to change their dietary pattern to vegetarianism, therefore I set 10 available positions to be converted -coded as num_of_chased- as a new vegetarian. Even though, the complete population of omnivorous were able to adopt vegetarianism I set a condition that protected them to be influenced, which was a safety area of 20 -coded as ep_area-. In other words, this area was the maximum distance in which vegetarian individuals were not able to influence omnivorous individuals.



