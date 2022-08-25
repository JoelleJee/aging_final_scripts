#!/bin/sh

data=$1
out=$2

for case in $(ls $data)
do

  # convert none
  if [ ! -e $out/$case/$case-none.nii ]; then
    /project/bbl_projects/apps/melliott/scripts/dicom2nifti.sh -u -F \
      $out/$case/$case-none.nii \
      $data/$case/S*none*/*dcm

    fi
done

