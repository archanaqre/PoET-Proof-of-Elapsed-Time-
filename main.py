import sgx
import user
import pickle
import pprint
import hashlib
import sqlite3
import blockchain
import collections
import transaction

'''
t_count - Number of pending transactions to be included on the blockchain
user_tokens - Land tokens held by each user
The following three dicts are used to duplicate the functionality of LevelDB in the bitcoin network
pending_transactions - OrderedDict containing list of valid (unspent) pending transaction and their hash
complete_transactions - OrderedDict containing list of valid (unspent) complete transaction and their hash
transaction_hist - OrderedDict containing all the spent and unspent transactions known to the node
'''
t_count = 0
user_tokens = {}
pending_transactions = collections.OrderedDict()
complete_transactions = collections.OrderedDict()
transaction_hist = collections.OrderedDict()

#Creates a token for a given land_id and owner_idn provided it does not exist previously
def create_land_token(idn, land_id):
    global complete_transactions
    global pending_transactions
    global t_count
    l = [x for x in complete_transactions.values()]
    l.extend([x for x in pending_transactions.values()])
    for t in l:
        if t['out']['land_id'] == land_id:
            print('LAND ALREADY OWNED by ', t['out']['owner'])
            return None
    new_token = transaction.coinbase(idn, land_id)
    pending_transactions[hashlib.sha256(pickle.dumps(new_token)).hexdigest()] = new_token
    transaction_hist[hashlib.sha256(pickle.dumps(new_token)).hexdigest()] = new_token
    t_count += 1
    return new_token

#Verfies if a transaction is valid as explained in the README
def verify_transaction(t):
    global complete_transactions
    global pending_transactions
    token = t['in']
    prev = complete_transactions.get(token) or pending_transactions.get(token)
    if prev is None:
        return False
    idn = prev['out']['owner']
    return user.verify_sign(t['sign'], token, user.get_user_pk(idn))

#Get user token for given owner idn and land_id
def get_token(idn, land_id):
    global user_tokens
    t = None
    for token in user_tokens[idn]:
        if token['out']['land_id'] == land_id:
            t = token
    return t

#Transfers a land token to a new owner idn using prev owner idn and land token (if token is unspent)
def transfer_land_token(curr_idn, idn, land_id, token):
    global complete_transactions
    global pending_transactions
    global t_count
    token = hashlib.sha256(pickle.dumps(token)).hexdigest()
    new_token = transaction.transfer(curr_idn, idn, land_id, token)
    if(verify_transaction(new_token)):
        pending_transactions[hashlib.sha256(pickle.dumps(new_token)).hexdigest()] = new_token
        transaction_hist[hashlib.sha256(pickle.dumps(new_token)).hexdigest()] = new_token
        t_count += 1
        if complete_transactions.get(token) is not None:
            complete_transactions.pop(token)
        else:
            pending_transactions.pop(token)
        return new_token
    else:
        return None

#Driver code for running the blockchain and providing given functionality
if __name__ == '__main__':
    #global complete_transactions
    #global pending_transactions
    #global user_tokens
    #global t_count
    print("CREATING GENESIS BLOCK")
    chain = blockchain.Blockchain()
    pprint.pprint(chain.chain)
    print()
    while(1):
        print("1. REGISTER USER WITH LAND\n2. TRANSFER PROPERTY\n3. LAND HISTORY\n4. EXIT\n")
        option = int(input())
        if option == 1:
            idn = int(input('AADHAR : '))
            if user_tokens.get(idn) is None:
                user_tokens[idn] = []
                user.insert_user(idn)
            option = int(input('DOES USER HAVE LAND? (1/0) : '))
            if(option):
                land_no = int(input('LAND ID : '))
                token = create_land_token(idn, land_no)
                if token is not None:
                    user_tokens[idn].append(token)
                    print('LAND TOKEN CREATED, ASSIGNED TO : ', idn)
            pprint.pprint(user_tokens)
            print()
            if t_count >= 4:
                print('ADDING BLOCK .... PoET ....\n')
                tl = [x for x in pending_transactions.values()]
                new_block, certificate = chain.poet(tl)
                if sgx.verify_certificate(certificate):
                    chain.add_block(new_block)
                    complete_transactions.update(pending_transactions)
                    pending_transactions.clear()
                    t_count = 0
                pprint.pprint(chain.chain)
                print()
        elif option == 2:
            curr_idn = int(input('FROM AADHAR : '))
            idn = int(input('TO AADHAR : '))
            land_id = int(input('LAND ID : '))
            token = transfer_land_token(curr_idn, idn, land_id, get_token(curr_idn, land_id))
            if token is not None:
                user_tokens[idn].append(token)
                print('LAND TOKEN CREATED, ASSGINED TO : ', idn)
            pprint.pprint(user_tokens)
            print()
            if t_count >= 4:
                print('ADDING BLOCK .... PoET ....\n')
                tl = [x for x in pending_transactions.values()]
                new_block, certificate = chain.poet(tl)
                if sgx.verify_certificate(certificate):
                    chain.add_block(new_block)
                    complete_transactions.update(pending_transactions)
                    pending_transactions.clear()
                    t_count = 0
                pprint.pprint(chain.chain)
                print()
        elif option == 3:
            land_id = int(input('ENTER LAND ID FOR HISTORY OF OWNERS: '))
            transaction_hist.update(pending_transactions)
            tl = [x for x in transaction_hist.values()]
            for t in tl:
                if t['out']['land_id'] == land_id:
                    owner_idn = t['out']['owner']
                    connection = sqlite3.connect('user.db')
                    cursor = connection.cursor()
                    query = '''
                                SELECT NAME FROM USER WHERE ID = (?)
                            '''
                    cursor.execute(query, (owner_idn, ))
                    result = cursor.fetchall()[0][0]
                    cursor.close()
                    connection.close()
                    print('\t', result)
            print()
        else:
            break
