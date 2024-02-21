./deposit.sh install  


mkdir -p validator_keys_1


./deposit.sh \
  --language=English \
  --non_interactive \
  existing-mnemonic \
  --validator_start_index=0 \
  --num_validators=2999 \
  --chain=holesky \
  --folder=./validator_keys_1 \
  --execution_address=0x350279fC8648f5d5B3aCCEFe166Bf4b1b096F04B




