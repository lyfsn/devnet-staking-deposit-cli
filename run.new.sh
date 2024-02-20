# ./deposit.sh install  

mkdir -p validator_keys_new

./deposit.sh \
  --language=English \
  --non_interactive \
  new-mnemonic \
  --num_validators=1 \
  --mnemonic_language=english \
  --chain=holesky \
  --folder=./validator_keys_new \
  --execution_address=0x6D39C4E60dEf1DfC6d09A8FdB5D075e85F0e5F8d

