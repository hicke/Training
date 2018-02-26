from twilio.rest import Client

account = "ACc30d0b06d4eaa8ce4d6fdae4eb63d1d7"
token = "aafd925f596b78aaf228d1660764f59a"
client = Client(account, token)


client.messages.create(to="+460705397949", from_="+46705397949", body="Hej")
