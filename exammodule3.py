##RNA sequence
def dna2rna(dna_seq):
	for base in seq:
        rna_seq = dna_seq.replace('T', 'U')
        return(rna_seq)

##protein sequence
def translate(rna_seq):  
	start_codon = rna_seq.find('ATG')
        seq_start = sequence[int(start_codon):]
        for n in (0, len(seq_start), 3):
        	if seq_start[n:n+3] in genetic_code:
        	    protein_seq += genetic_code[seq_start[n:n+3]]
    	return protein_seq
