#! /usr/bin/env python3

import sys
import six
import pronto

ont = pronto.Ontology('/Users/admin/problemsets/go.owl') #path to go.owl file in named directory

#term_obj = ont['GO:0006355'] #GO:0006355 is 'regulation of transcription, DNA template'
#term_name = term_obj.name	

#all_children = {}

#for child in ont['GO:0006355'].rchildren(): #this only returns the children term names of the provided GO annotation
#	all_children[child.id] = child.name

#all_children['GO:0006355'] = term_name #this is the parent term name

#print(all_children)
#print(term_name)


##repeating above script but to take arguments: gene ID or gene list

GO_GENES = sys.argv[1] # this is your gene list (gene_id\tgo_id\tgo_name)
MY_GO_ID = sys.argv[2] # this is the GO term you want to search for in your gene list

term_obj = ont[MY_GO_ID]
term_name = term_obj.name
print("These genes have all been annotated with" , MY_GO_ID + ', "' + term_name + '" or any of its child terms' )

all_children = {}
all_children[MY_GO_ID] = term_name #this is the parent term name

for child in ont[MY_GO_ID].rchildren(): #this only returns the children term names of the provided GO annota$
	all_children[child.id] = child.name

with open(GO_GENES, "r") as file:
	for line in file:
		

print(all_children)
#print(term_name)
