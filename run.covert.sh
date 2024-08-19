./deposit.sh install  


mkdir -p ./bls_to_execution_changes_2

./deposit.sh \
  --language=English \
  --non_interactive \
  generate-bls-to-execution-change \
  --bls_to_execution_changes_folder=./bls_to_execution_changes_2 \
  --chain=holesky \
  --mnemonic="expand chimney soldier increase degree chief throw hammer escape abandon light begin beauty fancy guess romance crunch behind game media piece fire velvet room" \
  --validator_start_index=0 \
  --validator_indices=65 \
  --bls_withdrawal_credentials_list=007fdb2abf35287a336830f6ae42cfa1dadd48afd1b3606025ab29fa9e7361f4 \
  --execution_address=0x95382F81598A3c9b4E8C5549B9Ea9ad24A734b13 \