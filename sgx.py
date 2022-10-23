import ecdsa
import pickle
import sqlite3

# Code to generate sgx keys - public key and private key
def _generate_sgx_keys():
    s = ecdsa.SigningKey.generate(curve = ecdsa.SECP256k1)
    #print('Secret Key : ', s.to_string().hex())
    p = s.verifying_key.to_string().hex()
    #print('Public Key : ', p)
    #print()
    return (s.to_string().hex(), p)

# Code to create the database for keys
def _create_db_sgx():
    connection = sqlite3.connect('sgx.db')
    cursor = connection.cursor()
    query = '''
                CREATE TABLE IF NOT EXISTS SGX
                (
                    ID BIGINT PRIMARY KEY,
                    SK VARCHAR(70) NOT NULL,
                    VK VARCHAR(130) NOT NULL
                )
            '''
    cursor.execute(query)
    cursor.close()
    connection.commit()
    connection.close()

# Code to add user keys to the database
def insert_user_sgx(idn):
    _create_db_sgx()
    sk, vk = _generate_sgx_keys()
    connection = sqlite3.connect('sgx.db')
    cursor = connection.cursor()
    query = '''
                INSERT INTO SGX VALUES (?, ?, ?)
            '''
    cursor.execute(query, (idn, sk, vk))
    cursor.close()
    connection.commit()
    connection.close()

# Code to get a user's secret key
def _get_user_sk(idn):
    connection = sqlite3.connect('sgx.db')
    cursor = connection.cursor()
    query = '''
                SELECT * FROM SGX U WHERE U.ID = (?)
            '''
    cursor.execute(query, (idn, ))
    result = cursor.fetchall()[0]
    cursor.close()
    connection.commit()
    connection.close()
    return result[1]

# Code to get user's public key
def _get_user_pk(idn):
    connection = sqlite3.connect('sgx.db')
    cursor = connection.cursor()
    query = '''
                SELECT * FROM SGX U WHERE U.ID = (?)
            '''
    cursor.execute(query, (idn, ))
    result = cursor.fetchall()[0]
    cursor.close()
    connection.commit()
    connection.close()
    return result[2]

# Code to get certificate signed by secret key
def get_certificate(time, idn):
    certificate = {}
    certificate['idn'] = idn
    certificate['time'] = time
    sk = _get_user_sk(idn)
    s = ecdsa.SigningKey.from_string(bytes.fromhex(sk), curve = ecdsa.SECP256k1)
    certificate['sign'] = s.sign(pickle.dumps(str(time))).hex()
    return certificate

# Code for certificate verification
def verify_certificate(certificate):
    idn = certificate['idn']
    time = certificate['time']
    sign = certificate['sign']
    pk = _get_user_pk(idn)
    p = ecdsa.VerifyingKey.from_string(bytes.fromhex(pk), curve = ecdsa.SECP256k1)
    return p.verify(bytes.fromhex(sign), pickle.dumps(str(time)))

# Code for deleting a user from database
def del_user(idn):
    connection = sqlite3.connect('sgx.db')
    cursor = connection.cursor()
    query = '''
                DELETE FROM SGX WHERE ID = (?)
            '''
    cursor.execute(query, (idn, ))
    cursor.close()
    connection.commit()
    connection.close()
