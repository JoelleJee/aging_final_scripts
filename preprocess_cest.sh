#!/bin/sh

data=$1
out=$2

for sub in $(ls $data)
do
  
  if ! [ -d $out/$sub ]
  then
    bsub python /project/bbl_roalf_3dcest/sandbox/test_pyGluCEST_2.0/pyGluCEST_2.0/scripts/process_GluCEST.py \
      -i $data \
      -o $out \
      -t hippocampus -d 2 -s $data -c $sub
  fi
done
