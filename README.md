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
2) Deploy a tool that users can use to toggle through different types of analaysis on crypto twitter in some automated way
-> ie. "Show me from whom the most reliable sources of information comes from", "Show me who the thought leaders on transaction cost analysis are", "Show me what new trends unseen in both DeFi and traditional finance are", "Show me what paradigms from TradFi are latching on to DeFi", etc...

3) Allow embedding of variety of NLP analytics techniques that can be plugged in to start building adjancecy matrices for variety of scores

### Steps: 
1) Map out the entirity of crypto twitter as a network represented in adjacency lists

#### Deliverable: Store the IDs in a adjacency list (where user i -> user j means user i follows user j)

#### Approaches:
1) Root Node User Approach
       Identify "root node" users who follow a ton of interesting ppl ("I'll show who to follow types")
       For each node, iterate through each child user and their children until termination - reached a user already seen, no more to traverse, or other            programmer defined termination condition is met



2) Iterate through the adjacency list to generate

#### OPEN QUESTIONS:
1) HOW OFTEN TO UPDATE NETWORK STATUS? - at some cadence/real-time? (=update network graph functions needed)
2) 

get accounts a particular user follows: 
1) 
