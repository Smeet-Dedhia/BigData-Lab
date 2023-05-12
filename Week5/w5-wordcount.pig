records = LOAD '/p3/l3.txt';
terms = FOREACH records GENERATE FLATTEN(TOKENIZE((chararray) $0)) AS word;
grouped_terms = GROUP term BY word;
word_counts = FOREACH grouped_terms GENERATE COUNT(terms), group;
STORE word_counts INTO '/p3/out6';

/*
path of hdfs files and folders
create txt file with paragraph on local
create pig file on local
transfer only text file onto hdfs
no need to transfer pig file to hadoop
run pig in mapreduce mode
on grunt use:
run filename.pig
*/
