./deposit.sh install  


mkdir -p validator_keys_2


./deposit.sh \
  --language=English \
  --non_interactive \
  existing-mnemonic \
  --validator_start_index=3000 \
  --num_validators=5999 \
  --chain=holesky \
  --folder=./validator_keys_2 \
  --execution_address=0x350279fC8648f5d5B3aCCEFe166Bf4b1b096F04B




