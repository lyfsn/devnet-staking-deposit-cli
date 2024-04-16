./deposit.sh install  

mkdir -p validator_keys_new

./deposit.sh \
  --language=English \
  --non_interactive \
  new-mnemonic \
  --num_validators=1 \
  --mnemonic_language=english \
  --chain=holesky \
  --folder=./validator_keys_new \

