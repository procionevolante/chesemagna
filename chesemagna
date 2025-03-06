#!/bin/sh

# nota: deve essere dell'anno corrente
rifGiorno='2025-01-27'
# in rifGiorno che settimana del menu era?
rifSettMenu=3
# durata ciclo del menu (in settimane)
durataCiclo=5

# - - -

if [ -d ~/docs/chesemagna-data ]; then
    dataDir="$HOME/docs/chesemagna-data"
elif [ -d ./chesemagna-data ]; then
    dataDir="$PWD/chesemagna-data"
elif [ -d "$(dirname "$0")/chesemagna-data" ]; then
    dataDir="$(dirname "$0")/chesemagna-data"
else
    echo Non trovo la cartella chesemagna-data
    exit 1
fi

if [ -z "$1" ]; then
    # che giorno e' oggi?
    data=$(date '+%F')
else
    # usa $1 come data da analizzare
    data=$(date '+%F' -d "$1")
fi

# 1 = Lunedi', 5 = Venerdi'
giorno="$(date '+%-u' -d "$data")"
sett="$(date '+%-W' -d "$data")"
rifSett="$(date '+%-W' -d "$rifGiorno")"

# settimane passate dalla settimana di riferimento
settMenu=$((($sett - $rifSett) % $durataCiclo ))

# offset della settimana del menu (a base 1 ma a noi serve a base 0)
settMenu=$((($settMenu + $rifSettMenu - 1) % $durataCiclo + 1))
fileSett="${dataDir}/sett${settMenu}.csv"

intestaz="$(head -n 1 -- "$fileSett")"
menu="$(tail -n +$(($giorno + 1)) -- "$fileSett" | head -n 1)"

numCampi="$(($(head -n 1 "$fileSett" | tr -cd ';' | wc -c) + 1))"

echo " --- GIORNO $(date '+%F' -d "$data") ---"
echo " --- SETTIMANA $settMenu ---"
for idx in $(seq "$numCampi"); do
    nomeCampo="$(echo "$intestaz" | cut -d ';' -f $idx)"
    echo -n "$nomeCampo: "
    valoreCampo="$(echo "$menu" | cut -d ';' -f $idx)"
    echo "$valoreCampo" | sed -E "$(printf "s;o ;\\\\n% ${#nomeCampo}s-;g" " ")"
done
