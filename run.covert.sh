./deposit.sh install  


mkdir -p ./bls_to_execution_changes_2

./deposit.sh \
  --language=English \
  --non_interactive \
  generate-bls-to-execution-change \
  --bls_to_execution_changes_folder=./bls_to_execution_changes_2 \
  --chain=holesky \
  --mnemonic="agree patch reduce satoshi kitten illness predict tail truck abuse acoustic bean volume manual uncover tilt punch labor spend general denial village radar grow" \
  --validator_start_index=0 \
  --validator_indices=0 \
  --bls_withdrawal_credentials_list=004760a7ad03166031a52553f9789d56fcffd30ef2b6a91e13c199f19231d9f7 \
  --execution_address=0x95382F81598A3c9b4E8C5549B9Ea9ad24A734b13 \