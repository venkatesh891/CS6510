from py2neo import Graph
from py2neo import Node, Relationship
from neo4jrestclient.client import GraphDatabase
graph = Graph()
def connectToDB():
	db = GraphDatabase("http://localhost:7474/db/data", username="neo4j", password="admin")
	user = db.labels.create("User")
	u1 = db.nodes.create(name="Marco")
	user.add(u1)
	Connection = "helloooo"
	return Connection