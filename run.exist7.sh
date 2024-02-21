./deposit.sh install  


mkdir -p validator_keys_7


./deposit.sh \
  --language=English \
  --non_interactive \
  existing-mnemonic \
  --validator_start_index=18000 \
  --num_validators=20999 \
  --chain=holesky \
  --folder=./validator_keys_7 \
  --execution_address=0x350279fC8648f5d5B3aCCEFe166Bf4b1b096F04B




