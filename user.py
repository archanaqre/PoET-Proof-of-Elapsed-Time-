import sgx
import ecdsa
import pickle
import sqlite3


# This function creates a private public key pair.
def generate_keys():
    # s is signing key, we'll use it to sign data (private key)
    s = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    # print('Secret Key : ', s.to_string().hex())
    # p is the corresponding public key to s , we'll use it to verify digital signature.
    # basically (s,p) is private public key pair.
    p = s.verifying_key.to_string().hex()
    # print('Public Key : ', p)
    # print()
    return (s.to_string().hex(), p)


# Creates a USER Table : Schema (ID,NAME,SK,VK)
def _create_db():
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                CREATE TABLE IF NOT EXISTS USER
                (
                    ID BIGINT PRIMARY KEY,
                    NAME VARCHAR(50) NOT NULL,
                    SK VARCHAR(70) NOT NULL,
                    VK VARCHAR(130) NOT NULL
                )
            '''
    cursor.execute(query)
    cursor.close()
    connection.commit()
    connection.close()


# The moment you enter a username, your identification number , public key and private key is created and inserted
# into database
def insert_user(idn):
    _create_db()
    name = input('NAME : ')
    sk, vk = generate_keys()
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                INSERT INTO USER VALUES (?, ?, ?, ?)
            '''
    cursor.execute(query, (idn, name, sk, vk))
    cursor.close()
    connection.commit()
    connection.close()
    sgx.insert_user_sgx(idn)


# This function takes user identification number as input and returns a tuple corresponding to that user
def get_user(idn):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                SELECT * FROM USER U WHERE U.ID = (?)
            '''
    cursor.execute(query, (idn,))
    result = cursor.fetchall()[0]
    cursor.close()
    connection.commit()
    connection.close()
    return result


# This function fetches rows of all users from the database
def get_all_userids():
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                SELECT ID FROM USER
            '''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return result


# This function takes a user idn and returns secret key corresponding to that user.
def _get_user_sk(idn):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                SELECT * FROM USER U WHERE U.ID = (?)
            '''
    cursor.execute(query, (idn,))
    result = cursor.fetchall()[0]
    cursor.close()
    connection.commit()
    connection.close()
    return result[2]


# This function takes a user idn and returns public key corresponding to that user.
def get_user_pk(idn):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                SELECT * FROM USER U WHERE U.ID = (?)
            '''
    cursor.execute(query, (idn,))
    result = cursor.fetchall()[0]
    cursor.close()
    connection.commit()
    connection.close()
    return result[3]


# This function takes user identification number and deletes user from the database.
def del_user(idn):
    connection = sqlite3.connect('user.db')
    cursor = connection.cursor()
    query = '''
                DELETE FROM USER WHERE ID = (?)
            '''
    cursor.execute(query, (idn,))
    cursor.close()
    connection.commit()
    connection.close()
    sgx.del_user(idn)


# This function takes user identification number and the message as input,
# it fetches the secret key corresponding to the idn from the database , signs the message with
# secret key of user and returns the signature.
def generate_sign(idn, message):
    sk = _get_user_sk(idn)
    s = ecdsa.SigningKey.from_string(bytes.fromhex(sk), curve=ecdsa.SECP256k1)
    return s.sign(pickle.dumps(message)).hex()


# This function takes sign, message and public key as input and verifies whether the signature
# is genuine and was produced by user who holds private key corresponding to the public key
# provided as input.
def verify_sign(sign, message, vk):
    p = ecdsa.VerifyingKey.from_string(bytes.fromhex(vk), curve=ecdsa.SECP256k1)
    return p.verify(bytes.fromhex(sign), pickle.dumps(message))
