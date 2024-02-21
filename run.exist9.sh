./deposit.sh install  


mkdir -p validator_keys_9


./deposit.sh \
  --language=English \
  --non_interactive \
  existing-mnemonic \
  --validator_start_index=24000 \
  --num_validators=26999 \
  --chain=holesky \
  --folder=./validator_keys_9 \
  --execution_address=0x350279fC8648f5d5B3aCCEFe166Bf4b1b096F04B




