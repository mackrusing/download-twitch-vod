while getopts i: flag
do 
  case "${flag}" in
    i) id=${OPTARG};;
  esac
done
echo "$id";

twcli api get videos -q id=$id > metadata/$id.json
