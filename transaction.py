import user
import hashlib

# This function creates a coinbase transaction, it fetches public key of the owner via the get_user_pk() function
# and embeds it in the transaction dictionary.
def coinbase(idn, land_id):
    transaction = {
                    'type' : 0,
                    'out' : {
                                'owner' : idn,
                                'land_id' : land_id,
                                'pk' : user.get_user_pk(idn)
                            }
                  }
    return transaction


# This function creates a buy/sell transaction, it fetches public key of the owner via the get_user_pk() function
# and embeds it in the transaction dictionary.
def transfer(curr_idn, idn, land_id, token):
    transaction = {
                    'type' : 1,
                    'in' : token,
                    'sign' : user.generate_sign(curr_idn, token),
                    'out' : {
                                'owner' : idn,
                                'land_id' : land_id,
                                'pk' : user.get_user_pk(idn)
                            }
                  }
    return transaction
