

if [ "$#" -ne 8 ]; then
  echo "Usage: $0 EXPNUM NIF NLT NNUM NVAR NPLUS NMULT DEPTH" >&2
  exit 1
fi


rnum=$1

NIF=$2 #1
NLT=$3 #1
NNUM=$4 #0
NVAR=$5 #6
NPLUS=$6 #2
NMULT=$7 #0
DEPTH=$8 #2

echo "#define NIF $NIF
#define NLT $NLT
#define NNUM $NNUM
#define NVAR $NVAR
#define NPLUS $NPLUS
#define NMULT $NMULT
#define DEPTH $DEPTH" > ./config.skh

runfile=./OUT/run$rnum.txt
probfile=./OUT/prob$rnum.out

skimmu -V 10 newtest_17_may.sk &> $runfile

echo -n "" > $probfile
grep PRINT $runfile  | grep -v void | sed 's/(/ /g' | sed 's/,/ /g' | sed 's/);//g' |sed 's/PRINT_//g' | awk 'BEGIN {x=0} { a[$1] =$1; a[$2] =x; x++; if($1=="VAR" || $1=="CONST") print a[$2]" = "$1,$3; else { printf a[$2]" = "$1" "; for(i=3;i<=NR+1;i++){ printf a[$i]" ";} print "";} }' >> $probfile 

grep "print_inp" $runfile | grep -v void  | sed 's/print_inp(/ /g' | sed 's/,/ /g' | sed 's/);//g' |sed 's/PRINT_//g' | awk '{print "("$1","$2","$3") -> "$4;}' >> $probfile

cat $probfile

