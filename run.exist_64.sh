./deposit.sh install  


mkdir -p validator_keys_64


./deposit.sh \
  --language=English \
  --non_interactive \
  existing-mnemonic \
  --validator_start_index=0 \
  --num_validators=64 \
  --chain=holesky \
  --folder=./validator_keys_64 \
  --execution_address=0x6D39C4E60dEf1DfC6d09A8FdB5D075e85F0e5F8d




