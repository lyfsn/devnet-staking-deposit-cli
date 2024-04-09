./deposit.sh install  


mkdir -p ./bls_to_execution_changes_2

./deposit.sh \
  --language=English \
  --non_interactive \
  generate-bls-to-execution-change \
  --bls_to_execution_changes_folder=./bls_to_execution_changes_2 \
  --chain=holesky \
  --mnemonic="ice sunny plastic surround unaware select decorate false pink uniform toward senior shed awesome visit" \
  --validator_start_index=0 \
  --validator_indices=0 \
  --bls_withdrawal_credentials_list=0015dd79b0170f51a5eb5ba35233183445d5eebac171330e603104f3267d17ef \
  --execution_address=0x95382F81598A3c9b4E8C5549B9Ea9ad24A734b13 \