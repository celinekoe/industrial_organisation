rename_path="../../data/crunchbase/country"
files=$(find "$rename_path/$1" -type f -name "*.csv")

OIFS="$IFS"
IFS=$'\n'
num=0
for f in $files; do
  newf="$rename_path/$1/$1_$num.csv"
  echo "file: $f"
  echo "new file: $newf"
  ((num++))
  mv -- "$f" "${newf}"
done
IFS="$OIFS"