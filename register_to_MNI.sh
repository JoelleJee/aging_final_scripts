case=$1
structural=$2
atlas=$3


if [ ! -d $structural/$case/MNI_transforms ]; then
  mkdir $structural/$case/MNI_transforms
fi

for str in UNI INV2; do
  
  if [ ! -e $structural/$case/$case-${str}-hdbet_masked.nii.gz ]; then
    fslmaths $structural/$case/$case-${str}_corrected.nii.gz \
      -mas $structural/$case/$case-INV2-hdbet_mask.nii.gz \
      $structural/$case/$case-${str}-hdbet_masked.nii.gz
  fi

  if [ ! -e $structural/$case/MNI_transforms/$case-${str}inMNI-Warped.nii.gz ]; then
    #register brain masked INV2 to upsampled MNI T1 template
    antsRegistrationSyN.sh -d 3 \
      -f $atlas/MNI/MNI152_T1_0.7mm_brain.nii.gz \
      -m $structural/$case/$case-${str}-hdbet_masked.nii.gz \
      -o $structural/$case/MNI_transforms/$case-${str}inMNI-
  fi
done
