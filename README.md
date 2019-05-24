# bloom_filtering

The following project aims to build a further understanding on bloom filters.

Objectives of this project: 

- Build a simple Bloom filter in Python, Scala and Java.
- Built (or select) an appropriate hash function 
- Understand how bit vectors are designed.
- Design different data stores and iterate through using the bloom filter, much like how LSM-Tables use bloom filters for fast access to SSTables.


### In Lehmann's terms, what is a Bloom filters? 

- Bloom Filters are a data structure which can act as an medium to some storage of information to find out whether a piece of information exists. It uses probability. This are particular useful for quickly retreiving data from databases. 

### A simple analogy (WITH TOYS!)

- A kid is looking for his favourite toy, but only knows its in one of 5 different toy boxes.
- Each toybox has 30 toys. 
- The way the toys go into these boxes are by the order in which they were bought. Newer toys go into new boxes
- If the person didn't know which toy box it was in.. then the worst case scenario is that he'll may have to search through all 150 toys (firstly by going through each box one at a time).
- The problem would be EVEN WORSE if each toy box had 100 toys in.
- Now .... if the person did know that the toy was in a box, it would be a lot quick to search. 

**Let's solve this with a bloom filter!**

- We can have an intermediate (aka a bloom filter) for each box. 
- Each box will have a paper with a blank list that can be filled in. 
- Whenever we place a new toy into the box, we write down the name of the toy into that empty list. 
- This piece of magic will allow us to quickly identify which box the toy is in USING PROBABILITY.
- The next time the kid tries to find his toy, knowing the name of the toy, he'll look at the chart to see the name of the toy is there. 
- If it isn't, then the kid will move onto the next box until he find it. 

## How does this translate?

- The boxes represent different storage types (database, table, data structure, etc.)
- The blank list on each box is a bit vector. 
- The toy is an object within the storage type, which has a name (key)
- The bloom filter is the process of adding names to the list for insertions and checking the names on the list for getting the information using the key.

## What if two toys have the same name? 

- This is actually expected, but also expected to be extremely unlikely. The worse case is that the box will be searched and there is no toy in there. But at least 150 toys won't be searched. Given a good hash function design (which is our paper with names on), we can reduce this probability as low as 1%. 

## References 

1. https://llimllib.github.io/bloomfilter-tutorial/ 
2. https://www.youtube.com/watch?v=x2sLjRK56YU 
3. https://en.wikipedia.org/wiki/Bloom_filter
4. http://hadoopmag.com/cassandra-internal-storage/ 
