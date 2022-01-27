adjectives = ["icky", "sick", "dizzy"]

#enumerating my_list
'''
[ (0, "icky"), (1, "sick"), (2,"dizzy")]
'''

for index, adjective in enumerate(adjectives):
    adjectives[index] = adjective + " :("

print(adjectives)
    
