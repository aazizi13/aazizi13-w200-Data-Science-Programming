#! /bin/bash
mkdir -p s1/s2
mkdir -p s1/s3
echo "Virtual (conda) environments are my favorite technology" >> s1/s3/conf.txt
mkdir -p s1/s2/Advanced
echo "Virtual environments are good for learning new technology" >> s1/s2/text_chunk1.txt
cp s1/s2/text_chunk1.txt s1/s2/Advanced
echo "I like them because they are fun" >> s1/s2/Advanced
cat s1/s2/Advanced/text_chunk2.txt > s1/s2/Advanced/text_chunk2.txt
