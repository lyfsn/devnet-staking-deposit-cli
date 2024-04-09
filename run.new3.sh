./deposit.sh install  

mkdir -p validator_keys_3

./deposit.sh \
  --language=English \
  --non_interactive \
  new-mnemonic \
  --num_validators=4000 \
  --mnemonic_language=english \
  --chain=holesky \
  --folder=./validator_keys_3 \
  --execution_address=0x8943545177806ED17B9F23F0a21ee5948eCaa776

