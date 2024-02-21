./deposit.sh install  


mkdir -p validator_keys_10


./deposit.sh \
  --language=English \
  --non_interactive \
  existing-mnemonic \
  --validator_start_index=27000 \
  --num_validators=29999 \
  --chain=holesky \
  --folder=./validator_keys_10 \
  --execution_address=0x350279fC8648f5d5B3aCCEFe166Bf4b1b096F04B




