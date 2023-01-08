import tweepy
import concurrent.futures as parallel
import time
import json
import logging
import asyncio
import argparse


info_logger = logging.getLogger('info_logger')
logging.basicConfig(filename='/Users/keonshikkim/Documents/non-economist-dev/crypto-twitter-analytics/CryptoTwitterNetwork_AdjacencyListGeneration.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


# Objective of the Script
# 1) To Map out the Entirety of Crypto Twitter & Dump into adjacency list

# Deliverable: Store the IDs in a adjacency list (where user i -> user j means user i follows user j)

# Approaches:
# 1) Root Node User Approach:
#   Identify "root node" users who follow a ton of interesting ppl ("I'll show who to follow types") - manual work
#   For each node, iterate through each child user and their children until termination - reached a user already seen, no more to traverse, or other programmer defined termination condition is met
# 2)


# OPEN QUESTIONS:
# 1) HOW OFTEN TO UPDATE NETWORK STATUS? - at some cadence/real-time? (=update network graph functions needed)
# 2) 

# get accounts a particular user follows: 
# 1) 

# TODO: More features to add
# 1) Additional Termination Rules - TAKING TOO LONG
# -> How many children to traverse through before stopping?
# ->        


# 2) Asynchronous (Needed?)
# -> Approximation

def get_user_id_from_username(client, username: str) -> str:
    """
    :param client twitter api client obj
    :param username user name of twitter account to retrieve ID of
    """
    return client.get_user(username=username).data.id

def build_adjacency_list_from_id(client, to_search_ids: set, generation_limit: int) -> dict:
    """
    :param client twitter api client obj
    :param to_search_ids set of IDs to search for
    """
    # The following  Conditions have been implemented
    # 1) Don't search again an already searched ID
    # 2) Move on once all its children node have been searched
    # 3) Generation Limit: Given generation_limit=m, then once the m-th generation from one of the root nodes is reached, then stop adding children nodes


    # TODO: More conditions
    # 1) 

    adjacency_list = dict()
    searched_ids = set() # IDs that have been searched that no longer need to be traversed (termination condition for the network search)

    current_generation = 1
    generation_population = {
        current_generation: len(to_search_ids)
    }
    def calculate_cumulative_generation_population(gen, gen_pop):
        return sum( [gen_pop[g] for g in range(1, gen+1)] ) 

    while len(to_search_ids) > 0: # All the IDS to search have not yet been traversed
        start = time.time()
        print("To Be Searched:", len(to_search_ids), "| Already Searched:", len(searched_ids))
        info_logger.info('{} ids left to search'.format(len(to_search_ids)))
        info_logger.info('{} ids have been searched so far'.format(len(searched_ids)))

        id = to_search_ids.pop() # Search a particular ID
        info_logger.info('ID={} to be searched'.format(id))

        if id not in adjacency_list: # we haven't seen this ID before
            info_logger.info('ID={} is being seen for the first time'.format(id))
            adjacency_list[id] = []
            page_token = None
            page_token_repeated = False
        else: # In case we've reached a limit wrt number of API calls but haven;t fully traversed that particular ID
            info_logger.info('ID={} had to wait cuz we exceeded API call limits'.format(id))
            # still keep the same pg_token

        while page_token_repeated is False:
            # Retrieve the response - we want the (id, username, name) tuple
            try:
                response = client.get_users_following(id=id, max_results=1000, pagination_token=page_token)
            except Exception as e: # API call limit met - add it back again to search
                info_logger.error('Too many API calls made. Waiting for 15 minutes...')
                time.sleep(15*60) # If you run into an error then sleep for 15 minutes = limit reached so waiit
                to_search_ids.add(id) # add the id back to something that needs to be traversed because we haven't explored it yet
                
            # Once the data has been retrieved, store the users in adjacency list
            try:
                for user in response.data:
                    username = user.username
                    name = user.name
                    user_id = user.id
                    # print(username, name, user_id)
                    adjacency_list[id].append({
                        "id": user_id, "username": username, "name": name
                    })
                    # If a completely new ID has been found (condition 1) then add it to the ids to be searched + generation limit hasn't been reached
                    if user_id not in searched_ids and current_generation < generation_limit: 
                        to_search_ids.add(user_id)
            except TypeError: # No data has been found = no more following
                info_logger.info("ID = {} Took {} seconds to build adjacency list out of".format(id, time.time()-start))
                page_token_repeated = True # I guess this is moot actually then 
                searched_ids.add(id) # Add the ID to a set of searched IDs - termination condition

            # Grab Next Page Token | If last page then exit & move on to the next ID
            try:
                page_token = response.meta["next_token"]
            except KeyError: # Condition 2: We've searched the node fully
                info_logger.info("ID = {} Took {} seconds to build adjacency list out of".format(id, time.time()-start))
                page_token_repeated = True # I guess this is moot actually then 
                searched_ids.add(id) # Add the ID to a set of searched IDs - termination condition

                # every time we add, make sure we check the generation
                if len(searched_ids) == calculate_cumulative_generation_population(current_generation, generation_population): # generation has been searched
                    current_generation += 1 # update to new generation
                    generation_population[current_generation] = len(to_search_ids) # the next generation is number of ids lef to be searched on the next gen
                    print("Next Generation")

                break
    return adjacency_list


def main(args):
    # Initialize Logging
    info_logger = logging.getLogger('info_logger')
    logging.basicConfig(filename=args.log_file_path + 'CryptoTwitterNetwork_AdjacencyListGeneration.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    
    # Initialize Twitter API Client
    client = tweepy.Client(
        args.bearer_token, args.api_key, args.api_key_secret, args.access_token, args.access_token_secret
    )

    # Run the Adjacency List Creation
    # 1) Retrieve set of Twitter IDs to search for, which correspond to "root node" usernames provided in an external text file
    to_search_ids = set()
    with open(args.root_node_usernames_path, 'r') as f:
        for username in f.readlines():
            username = username.replace("\n", "")
            to_search_ids.add(get_user_id_from_username(client, username))

    # 2) Run the Adjacency list creation algorithm
    res = build_adjacency_list_from_id(client, to_search_ids, generation_limit=2)

    # 3) Store the Adjancency List as a JSON File
    with open(args.results_path + 'CryptoTwitterNetwork.json', 'w') as fp:
        json.dump(res, fp)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    api_args = parser.add_argument_group("api_args")
    api_args.add_argument("-k", "--api_key", type=str, help="")
    api_args.add_argument("-s", "--api_key_secret", type=str, help="")
    api_args.add_argument("-b", "--bearer_token", type=str, help="")
    api_args.add_argument("-a", "--access_token", type=str, help="")
    api_args.add_argument("-t", "--access_token_secret", type=str, help="")
    
    
    filepaths = parser.add_argument_group("filepaths")
    filepaths.add_argument(
        "-l", "--log_file_path", type=str, help="path under which to store the log file",
        default="/Users/keonshikkim/Documents/non-economist-dev/crypto-twitter-analysis/network_analysis/logs/"
    )
    filepaths.add_argument(
        "-u", "--root_node_usernames_path", type=str, help="path to text file containing root node usernames",
        default="/Users/keonshikkim/Documents/non-economist-dev/crypto-twitter-analysis/network_analysis/root_node_usernames.txt",
    )

    filepaths.add_argument(
        "-r", "--results_path", type=str, help="where to store crypto network adjacency list as JSON",
        default="/Users/keonshikkim/Documents/non-economist-dev/crypto-twitter-analysis/network_analysis/"
    )
    
    
    main(parser.parse_args())
