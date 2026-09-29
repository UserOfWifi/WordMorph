# Project 1: Word Morph - CSCI 325
Project 1 (Orange Group) for CSCI-325 Lake Forest College. In collaboration with Arianna, Princess, and Soham.

## What is our goal?
- Our goal is to use BFS and UCS to find the fastest and cheapest path respectively when morphing one word to another.

## How is this done?
- The rough idea is that we call the excel or csv file that has 74 thousand words and find same length neighbors for each word next in the queue / priority queue. BFS determines the shortest path to get to it's destination without worrying about cost, while UCS makes all it's decisions based on cost.

## Short Result Example
(This is a copy paste from the terminal)
    
    Word morph selected: [goat -> barn]
    BFS Initiated | Please wait!
    BFS:  (['goat', 'boat', 'boas', 'baas', 'bars', 'barn'], 28)
    Path Length: 6
    Finished in 70.86 seconds
    
    UCS Initiated | Please wait!
    UCS:  (['goat', 'boat', 'boot', 'boon', 'born', 'barn'], 24)
    Path Length: 6
    Finished in 59.04 seconds
    ---
