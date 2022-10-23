Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\soumy\Desktop\BITS Pilani ME\Semester III\Blockchain Technologies (BT)\Assignment 1\A1_Group_No_19\main.py
CREATING GENESIS BLOCK
[{'block_number': 1,
  'merkleroot': None,
  'merkletree': OrderedDict(),
  'prev_hsh': '0',
  'timestamp': '2022-10-17 18:19:38.636095',
  'transactions': None}]

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 1234567890123456
NAME : Zubair
DOES USER HAVE LAND? (1/0) : 1
LAND ID : 100
LAND TOKEN CREATED, ASSGINED TO :  1234567890123456
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}]}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 1234567890123456
DOES USER HAVE LAND? (1/0) : 1
LAND ID : 200
LAND TOKEN CREATED, ASSGINED TO :  1234567890123456
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}]}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 2345678901234567
NAME : Soumya
DOES USER HAVE LAND? (1/0) : 0
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: []}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

2
FROM AADHAR : 1234567890123456
TO AADHAR : 2345678901234567
LAND ID : 200
LAND TOKEN CREATED, ASSGINED TO :  2345678901234567
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1}]}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

2
FROM AADHAR : 1234567890123456
TO AADHAR : 2345678901234567
LAND ID : 200
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1}]}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 3456789012345678
NAME : Archana
DOES USER HAVE LAND? (1/0) : 0
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1}],
 3456789012345678: []}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 4567890123456789
NAME : Sagarika
DOES USER HAVE LAND? (1/0) : 0
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1}],
 3456789012345678: [],
 4567890123456789: []}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

2
FROM AADHAR : 1234567890123456
TO AADHAR : 2345678901234567
LAND ID : 100
LAND TOKEN CREATED, ASSGINED TO :  2345678901234567
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1},
                    {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                     'out': {'land_id': 100,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                     'type': 1}],
 3456789012345678: [],
 4567890123456789: []}

ADDING BLOCK .... PoET ....

SLEEP :  24

[{'block_number': 1,
  'merkleroot': None,
  'merkletree': OrderedDict(),
  'prev_hsh': '0',
  'timestamp': '2022-10-17 18:19:38.636095',
  'transactions': None},
 {'block_number': 2,
  'merkleroot': 'daa5398f3c0c26bcfd93c67d18fc0afd4f2734829ceba57d1d899f60d4b8a9de',
  'merkletree': OrderedDict([('28b02d07f0af73feaa469f27baf031b6712af87c3be728e440f81627917f0800',
                              <merkle.MerkleNode object at 0x000001C1F20A1040>),
                             ('ec5da670f654a0ce7063683bbb96e4f2827ce6e3fcf772ca24bf879d44712010',
                              <merkle.MerkleNode object at 0x000001C1F20A1B30>)]),
  'prev_hsh': '806a62e70b0d6a8e846ac8864115572088e7f1e7ee966fe44e5020edec222ea2',
  'timestamp': '2022-10-17 18:22:42.472234',
  'transactions': [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                    'out': {'land_id': 200,
                            'owner': 2345678901234567,
                            'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                    'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                    'type': 1},
                   {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                    'out': {'land_id': 100,
                            'owner': 2345678901234567,
                            'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                    'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                    'type': 1}]}]

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

2
FROM AADHAR : 1234567890123456
TO AADHAR : 3456789012345678
LAND ID : 100
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1},
                    {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                     'out': {'land_id': 100,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                     'type': 1}],
 3456789012345678: [],
 4567890123456789: []}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

2
FROM AADHAR : 2345678901234567
TO AADHAR : 1234567890123456
LAND ID : 100
LAND TOKEN CREATED, ASSGINED TO :  1234567890123456
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'in': 'ec5da670f654a0ce7063683bbb96e4f2827ce6e3fcf772ca24bf879d44712010',
                     'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'sign': '07dfdcab8b23d61f90f9e04b4aad599d6c1cc1c92ce72a0accd6b4e0a5c52afa53369be8822128f3bdd1af23e17c51f8236f1a458b21c35d32839b0f291443a8',
                     'type': 1}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1},
                    {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                     'out': {'land_id': 100,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                     'type': 1}],
 3456789012345678: [],
 4567890123456789: []}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

2
FROM AADHAR : 1234567890123456
TO AADHAR : 3456789012345678
LAND ID : 100
LAND TOKEN CREATED, ASSGINED TO :  3456789012345678
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'in': 'ec5da670f654a0ce7063683bbb96e4f2827ce6e3fcf772ca24bf879d44712010',
                     'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'sign': '07dfdcab8b23d61f90f9e04b4aad599d6c1cc1c92ce72a0accd6b4e0a5c52afa53369be8822128f3bdd1af23e17c51f8236f1a458b21c35d32839b0f291443a8',
                     'type': 1}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1},
                    {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                     'out': {'land_id': 100,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                     'type': 1}],
 3456789012345678: [{'in': 'ea762030ee9ea30988506ee478c670bb002c668502ac262e0d1372999283e7fb',
                     'out': {'land_id': 100,
                             'owner': 3456789012345678,
                             'pk': 'ba104ecc00e526e011cc3e8db438ffb521212f64cee33c7b4ef24f1f4b949b425492eb737559aca49a3e3cdad660189079281d93e97f0770f437da5515ec54cd'},
                     'sign': '27b14fcbe99ba2acd98df385b287bec84e0e19f4d235667ac99e6399a8bed93c4d1c824b7898596f30fffc403fcaf419a3248f6c6022595b4582d0dcb4a8fd66',
                     'type': 1}],
 4567890123456789: []}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

3
ENTER LAND ID FOR HISTORY OF OWNERS: 100
	 Zubair
	 Soumya
	 Zubair
	 Archana

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

3
ENTER LAND ID FOR HISTORY OF OWNERS: 200
	 Zubair
	 Soumya

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 4567890123456789
DOES USER HAVE LAND? (1/0) : 1
LAND ID : 300
LAND TOKEN CREATED, ASSGINED TO :  4567890123456789
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'in': 'ec5da670f654a0ce7063683bbb96e4f2827ce6e3fcf772ca24bf879d44712010',
                     'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'sign': '07dfdcab8b23d61f90f9e04b4aad599d6c1cc1c92ce72a0accd6b4e0a5c52afa53369be8822128f3bdd1af23e17c51f8236f1a458b21c35d32839b0f291443a8',
                     'type': 1}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1},
                    {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                     'out': {'land_id': 100,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                     'type': 1}],
 3456789012345678: [{'in': 'ea762030ee9ea30988506ee478c670bb002c668502ac262e0d1372999283e7fb',
                     'out': {'land_id': 100,
                             'owner': 3456789012345678,
                             'pk': 'ba104ecc00e526e011cc3e8db438ffb521212f64cee33c7b4ef24f1f4b949b425492eb737559aca49a3e3cdad660189079281d93e97f0770f437da5515ec54cd'},
                     'sign': '27b14fcbe99ba2acd98df385b287bec84e0e19f4d235667ac99e6399a8bed93c4d1c824b7898596f30fffc403fcaf419a3248f6c6022595b4582d0dcb4a8fd66',
                     'type': 1}],
 4567890123456789: [{'out': {'land_id': 300,
                             'owner': 4567890123456789,
                             'pk': 'b78d389fe3e70737f60c7e868133c2515b5b56b0b00a52d7b5a843a015a81dadfefd13875ed49e66509865286e49e6b5638af03672400688194b5f877d4ec8e2'},
                     'type': 0}]}

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

3
ENTER LAND ID FOR HISTORY OF OWNERS: 300
	 Sagarika

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

1
AADHAR : 5678901234567890
NAME : John
DOES USER HAVE LAND? (1/0) : 1
LAND ID : 400
LAND TOKEN CREATED, ASSGINED TO :  5678901234567890
{1234567890123456: [{'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'out': {'land_id': 200,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'type': 0},
                    {'in': 'ec5da670f654a0ce7063683bbb96e4f2827ce6e3fcf772ca24bf879d44712010',
                     'out': {'land_id': 100,
                             'owner': 1234567890123456,
                             'pk': '877bbfed7077bd9eb4f9d887d87c5e9d3f310553331414bb720aa6a754a00c161af7c7dc97bb9c4fb22b185f34865b74f254bf8a57466c3c9a21b90ab511988e'},
                     'sign': '07dfdcab8b23d61f90f9e04b4aad599d6c1cc1c92ce72a0accd6b4e0a5c52afa53369be8822128f3bdd1af23e17c51f8236f1a458b21c35d32839b0f291443a8',
                     'type': 1}],
 2345678901234567: [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                     'out': {'land_id': 200,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                     'type': 1},
                    {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                     'out': {'land_id': 100,
                             'owner': 2345678901234567,
                             'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                     'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                     'type': 1}],
 3456789012345678: [{'in': 'ea762030ee9ea30988506ee478c670bb002c668502ac262e0d1372999283e7fb',
                     'out': {'land_id': 100,
                             'owner': 3456789012345678,
                             'pk': 'ba104ecc00e526e011cc3e8db438ffb521212f64cee33c7b4ef24f1f4b949b425492eb737559aca49a3e3cdad660189079281d93e97f0770f437da5515ec54cd'},
                     'sign': '27b14fcbe99ba2acd98df385b287bec84e0e19f4d235667ac99e6399a8bed93c4d1c824b7898596f30fffc403fcaf419a3248f6c6022595b4582d0dcb4a8fd66',
                     'type': 1}],
 4567890123456789: [{'out': {'land_id': 300,
                             'owner': 4567890123456789,
                             'pk': 'b78d389fe3e70737f60c7e868133c2515b5b56b0b00a52d7b5a843a015a81dadfefd13875ed49e66509865286e49e6b5638af03672400688194b5f877d4ec8e2'},
                     'type': 0}],
 5678901234567890: [{'out': {'land_id': 400,
                             'owner': 5678901234567890,
                             'pk': '69273acf448ed76dd0e46a2fdafbe2e962627cc61e53754579270b6e424b3df5e41dfc7a836ee8bcb02b60cbc0a40cb3efd8a377c5d498223454484565c9cfc4'},
                     'type': 0}]}

ADDING BLOCK .... PoET ....

SLEEP :  11

[{'block_number': 1,
  'merkleroot': None,
  'merkletree': OrderedDict(),
  'prev_hsh': '0',
  'timestamp': '2022-10-17 18:19:38.636095',
  'transactions': None},
 {'block_number': 2,
  'merkleroot': 'daa5398f3c0c26bcfd93c67d18fc0afd4f2734829ceba57d1d899f60d4b8a9de',
  'merkletree': OrderedDict([('28b02d07f0af73feaa469f27baf031b6712af87c3be728e440f81627917f0800',
                              <merkle.MerkleNode object at 0x000001C1F20A1040>),
                             ('ec5da670f654a0ce7063683bbb96e4f2827ce6e3fcf772ca24bf879d44712010',
                              <merkle.MerkleNode object at 0x000001C1F20A1B30>)]),
  'prev_hsh': '806a62e70b0d6a8e846ac8864115572088e7f1e7ee966fe44e5020edec222ea2',
  'timestamp': '2022-10-17 18:22:42.472234',
  'transactions': [{'in': 'f7a622f9a298841f58b0ff6c3b77072de9386ad0db7ab890da3c67053ffdb5b4',
                    'out': {'land_id': 200,
                            'owner': 2345678901234567,
                            'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                    'sign': 'f3c5bcb07fa406a297a15297ca68a3e606fc9a47c5806e1ebbc3b11ca9a883b2cfebeaef317693f60badef9b094b0291216403eabbf2a44f6a08a23ebb90dc46',
                    'type': 1},
                   {'in': '63d63bf47b76528137785c6c011ddb6d8d1fd4965e68aa99c475be6aac3b0026',
                    'out': {'land_id': 100,
                            'owner': 2345678901234567,
                            'pk': 'a425362f6a66fb038d6b7bda3172a5beb3b54366e793b04f9db73d6688480c81b075c2d4dc8c0727810ee627f28d60139920e0d7d634e15c023ff0e5465c22c6'},
                    'sign': 'b4d57d3fc545ebff688f59049ac5d5b3bcc80b028a7f5b4c947402469ee555deab3404e44d619f44011df3fc14d6fcea253f62536356186a5d0142d7e4543646',
                    'type': 1}]},
 {'block_number': 3,
  'merkleroot': '2520ebd4ddcaf426b33ad00a78a55c433129448133654f2dfcb8272b404df12a',
  'merkletree': OrderedDict([('ce5ffb18f4b7321baba26a9363d5f5f9255c66d56f2ea4444bc9546f1e25a17f',
                              <merkle.MerkleNode object at 0x000001C1F20A7B30>),
                             ('b52502603a6e9d0b2a3ad8fa02ccca9869bcac73bf4ee959dc864fb239d09d40',
                              <merkle.MerkleNode object at 0x000001C1F20A7F40>),
                             ('8b2e83e99430b1fc0c8a940d4e967ac0d3c4f639de1c2d82da0fe2b9cd70c354',
                              <merkle.MerkleNode object at 0x000001C1F20A7EA0>)]),
  'prev_hsh': '7cf0b8a0daef1988701427b4284877c16371682481df819c900d45c7a9a68404',
  'timestamp': '2022-10-17 18:26:04.661676',
  'transactions': [{'in': 'ea762030ee9ea30988506ee478c670bb002c668502ac262e0d1372999283e7fb',
                    'out': {'land_id': 100,
                            'owner': 3456789012345678,
                            'pk': 'ba104ecc00e526e011cc3e8db438ffb521212f64cee33c7b4ef24f1f4b949b425492eb737559aca49a3e3cdad660189079281d93e97f0770f437da5515ec54cd'},
                    'sign': '27b14fcbe99ba2acd98df385b287bec84e0e19f4d235667ac99e6399a8bed93c4d1c824b7898596f30fffc403fcaf419a3248f6c6022595b4582d0dcb4a8fd66',
                    'type': 1},
                   {'out': {'land_id': 300,
                            'owner': 4567890123456789,
                            'pk': 'b78d389fe3e70737f60c7e868133c2515b5b56b0b00a52d7b5a843a015a81dadfefd13875ed49e66509865286e49e6b5638af03672400688194b5f877d4ec8e2'},
                    'type': 0},
                   {'out': {'land_id': 400,
                            'owner': 5678901234567890,
                            'pk': '69273acf448ed76dd0e46a2fdafbe2e962627cc61e53754579270b6e424b3df5e41dfc7a836ee8bcb02b60cbc0a40cb3efd8a377c5d498223454484565c9cfc4'},
                    'type': 0}]}]

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

3
ENTER LAND ID FOR HISTORY OF OWNERS: 400
	 John

1. REGISTER USER WITH LAND
2. TRANSFER PROPERTY
3. LAND HISTORY
4. EXIT

4
>>> 