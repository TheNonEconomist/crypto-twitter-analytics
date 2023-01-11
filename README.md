# crypto-twitter-analytics


## Network Analysis
### Project Goal:
The Goal of this project is to build a basis for analyzing Crypto Twitter that can be used to d ovariety of tasks from - extracting investment signals, 
assessing health of the Crypto Twitter, identifying where quality sources of information are, and to understand how thougts are influenced. 

### Objectives:
1) To Map out the Entirity of Crypto Twitter to be further used for any type of network analyses
-> Network Analysis could be used for the following purposes - 
     i) Identify spheres of influence in Crypto Twitter (can be correlated with investment signals, industry shifts, etc...)
     ii) Detect echo chambers as indicators for reliabilities of certain source(s)
     iii) 
2) Deploy some kind of tool that users can use to toggle through different types of analaysis on crypto twitter in some automated way
-> ie. "Show me from whom the most reliable sources of information comes from", "Show me how people have "

3) Allow embedding of variety of NLP analytics techniques that can be plugged in to start building adjancecy matrices for variety of scores

### Steps: 
1) Map out the entirity of crypto twitter as a network represented in adjacency lists

2) Identify "spheres of influence", either through a clustering approach or using NLP techniques to understand level of influence amongst Crypto Twitter accounts (using as basis for edge values) 

3) Generate adjacency matrices for the graph per topic to measure the level of influence (NLP technique based scoring - Methodology to be developed)

4) Classify "centroids" (perhaps thought originators and those good at presenting info in a digestible way) in each cluster as being Reliable or Not Reliable (or measure level of reliability per topic) & Cross-reference with level of influence as provided by the adjacency matrix to determine which clusters are good sources of information/indicators on a particualr topic. 

5) Build UX that presents information either to - provide high elvel overview or dig deep into 1 topic - and develop an algo that traverses the graph built above - Rough idea for now but ie) high level overview could traverse through "centroids" rated to be reliable on each topic, deep dive into a topic starts at the "centroid" then traverses through next nodes that are closest to the centroids.

#### Deliverable: Store the IDs in a adjacency list (where user i -> user j means user i follows user j)

#### Approaches - Step 1:
1) Root Node User Approach
       Identify "root node" users who follow a ton of interesting ppl ("I'll show who to follow types")
       For each node, iterate through each child user and their children until termination - reached a user already seen, no more to traverse, or other            programmer defined termination condition is met



2) Iterate through the adjacency list to generate

#### OPEN QUESTIONS:
1) HOW OFTEN TO UPDATE NETWORK STATUS? - at some cadence/real-time? (=update network graph functions needed)
2) 

#### Potential Risks
1) This approach really associates reliability of information to each twitter account on a given topic. It doesn't take account of possibility of hacking and faltering or increasing reliability in a dynamic and real-time way. It is possible to "Regenerate the graph" given new data to update the level of reliability and influence that's modeled by the adjacency matrix and lists.
2) 
