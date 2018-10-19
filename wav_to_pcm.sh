#/bin/bash

if [ $# -lt 1 ];then
    echo "usage: sh $0 indir "
fi

indir=$1
# outdir=$2

for file in `ls ${indir}/*.wav`
do
    echo ${file}
    sox ${file} ${file}.raw
    mv ${file}.raw ${file}.pcm
done
