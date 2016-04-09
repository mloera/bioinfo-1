from Bio import Entrez
import sys
import time
Entrez.email = "email" # No olvides poner tu email

## Este código te servirá para bajar información en batches usando el historial

search_handle = Entrez.esearch(db="nucleotide",term="Opuntia[orgn] and rpl16",
                                   usehistory="y")


search_results = Entrez.read(search_handle)
search_handle.close()
gi_list = search_results["IdList"]
count = int(search_results["Count"])
assert count == len(gi_list)
webenv = search_results["WebEnv"]
query_key = search_results["QueryKey"]
print(webenv,query_key)

start = 0
batch_size = 3
out_handle = open("orchid_fasta.txt", "w")
for start in range(0,len(gi_list),batch_size):
    time.sleep(5)
    fetch_handle = Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text",
                                         retstart=start, retmax=batch_size,
                                         webenv=webenv, query_key=query_key)
        
    data = fetch_handle.read()
    fetch_handle.close()
    out_handle.write(data)
out_handle.close()
