import os

os.environ['TESTDB'] = 'postgresql+psycopg2://username:password@localhost:5432/testbucketlist'
os.environ['PRODUCTIONDB'] = 'postgresql+psycopg2://username:password@localhost:5432/bucketlist'
os.environ['DEVELOPMENTDB'] = 'postgresql+psycopg2://username:password@localhost:5432/bucketlist'
