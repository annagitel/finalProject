"""
This test will preform a deniel of serveice attack by sending a big ammount of API request to the
clusters. types of tests:
1. DOS of the same query
2. different queries
3. spoofed IP with each query (DDOS)

the test will expect a block after some amount of time
in addition, response latancy will be recorded and analysed to determine the durability
of the API with such attacks

"""