# ./deposit.sh install  


mkdir -p ./bls_to_execution_changes

./deposit.sh \
  --language=English \
  --non_interactive \
  generate-bls-to-execution-change \
  --bls_to_execution_changes_folder=./bls_to_execution_changes \
  --chain=holesky \
  --mnemonic="marine fox season boat flee bid execute involve tree agree sick fault kind during quit monitor guard impulse half dawn drill drastic salon faith" \
  --validator_start_index=1 \
  --validator_indices=79 \
  --bls_withdrawal_credentials_list=00898becf9f2e2476794d2af3871c0d1409e0d556bbbfc64413e9f0537d303d2 \
  --execution_address=0x95382F81598A3c9b4E8C5549B9Ea9ad24A734b13 \





