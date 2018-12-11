#a
seqfile = open('sprot_prot.fasta', 'r')
for line in seqfile:
print line

#b
seqs = open('seqs.txt', 'w')
for line in seqfile:
	if line[0] == '>':
		if 'Homo sapiens' not in line:
			seqs.write(line)
			
seqs.close()
