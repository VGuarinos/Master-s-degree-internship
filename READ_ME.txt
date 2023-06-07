Description des versions du modèle :

BoxModel_v1 : Entrée des flux et des concentrations en oxygène directement sur le script.
Le modèle calcule la variation de concentration en oxygène dans les 4 compartiments pouvant varier (WMIW, WMDW, EMIW, EMDW). La consommation d'O2 est calculée à chaque étape selon Ks (O2 half-saturation concentration) et [O2]. Attention, le mélange turbulent entre les compartiments est considéré constant. Les flux affectants WMIW ne sont pas à l'équilibre pour le scénario Pre_EMT (flux issus du papier Powley et al. 2016).




BoxModel_v2 : Entrée des flux et des concentrations en oxygène automatisée selon un scénario définit dans les tableaux excel. La selection du scénario se fait dans le script. Pour créer un scénario, il faut créer une nouvelle colonne dans LES DEUX tableurs et entrer les flux entre les compartiments. Les flux doivent être à l'équilibre. Il ne faut pas oublier de définir la concentration en oxygène de départ (fichier boxmodel_oxygen_input).

Le modèle calcule la variation de concentration en oxygène dans les 4 compartiments pouvant varier (WMIW, WMDW, EMIW, EMDW). La consommation d'O2 est calculée à chaque étape selon Ks (O2 half-saturation concentration) et [O2]. Attention, le mélange turbulent entre les compartiments est considéré constant. Les flux affectants WMIW ne sont pas à l'équilibre pour le scénario Pre_EMT (flux issus du papier Powley et al. 2016). Ils sont cependant compris dans une gamme de variation de 5%.




BoxModel_v3 : Entrée des flux et des concentrations en oxygène automatisée selon un scénario définit dans les tableaux excel. La selection du scénario se fait dans le script. Pour créer un scénario, il faut créer une nouvelle colonne dans LES DEUX tableurs et entrer les flux entre les compartiments. Les flux doivent être à l'équilibre. Il ne faut pas oublier de définir la concentration en oxygène de départ (fichier boxmodel_oxygen_input).

Le modèle calcule la variation de concentration en oxygène dans les 4 compartiments pouvant varier (WMIW, WMDW, EMIW, EMDW). La consommation d'O2 est calculée à chaque étape selon Ks (O2 half-saturation concentration) et [O2]. Attention, le mélange turbulent entre les compartiments est considéré constant. Tous les flux sont à l'équilibre pour le scénario Pre_EMT (conformément aux attentes) avec une gamme de variation inférieure à 0,5% pour la mise à l'équilibre (mélange turbulent différent du papier Powley et al. 2016).




BoxModel_v4 : Entrée des flux et des concentrations en oxygène automatisée selon un scénario définit dans les tableaux excel. La selection du scénario se fait dans le script. Pour créer un scénario, il faut créer une nouvelle colonne dans LES DEUX tableurs et entrer les flux entre les compartiments. Les flux doivent être à l'équilibre. Il ne faut pas oublier de définir la concentration en oxygène de départ (fichier boxmodel_oxygen_input).

Le modèle calcule la variation de concentration en oxygène dans les 4 compartiments pouvant varier (WMIW, WMDW, EMIW, EMDW). La consommation d'O2 est calculée à chaque étape selon Ks (O2 half-saturation concentration) et [O2]. Attention, le mélange turbulent est calculé en admettant un flux d'O2 retrouvé à partir d'un modèle linéaire. Tous les flux sont à l'équilibre pour le scénario Pre_EMT (conformément aux attentes) avec une gamme de variation inférieure à 5% pour la mise à l'équilibre (mélange turbulent différent du papier Powley et al. 2016).




BoxModel_v5 : Entrée des flux et des concentrations en oxygène automatisée selon un scénario définit dans les tableaux excel. La selection du scénario se fait dans le script. Pour créer un scénario, il faut créer une nouvelle colonne dans LES DEUX tableurs et entrer les flux entre les compartiments. Les flux doivent être à l'équilibre. Il ne faut pas oublier de définir la concentration en oxygène de départ (fichier boxmodel_oxygen_input).

Le modèle calcule la variation de concentration en oxygène dans les 4 compartiments pouvant varier (WMIW, WMDW, EMIW, EMDW). La consommation d'O2 est calculée à chaque étape selon Ks (O2 half-saturation concentration) et [O2]. Le mélange turbulent est calculé en admettant un flux d'O2 retrouvé à partir d'un modèle linéaire. Ce mélange turbulent prend en compte le coefficient de diffusion effective Kz, la différence de concentration en O2 entre deux boites, la distance moyenne des boites, la surface de contact (surface du bassin). Tous les flux sont à l'équilibre pour le scénario Pre_EMT (conformément aux attentes) avec une gamme de variation inférieure à 5% pour la mise à l'équilibre (Inférieure à 5% par rapport à Powley et al. 2016).




BoxModel_v6 : Entrée des flux et des concentrations en oxygène automatisée selon un scénario définit dans les tableaux excel. La selection du scénario se fait dans le script. Pour créer un scénario, il faut créer une nouvelle colonne dans LES DEUX tableurs et entrer les flux entre les compartiments. Les flux doivent être à l'équilibre. Il ne faut pas oublier de définir la concentration en oxygène de départ (fichier boxmodel_oxygen_input).

Le modèle calcule la variation de concentration en oxygène dans les 4 compartiments pouvant varier (WMIW, WMDW, EMIW, EMDW). La consommation d'O2 est calculée à chaque étape selon Ks (O2 half-saturation concentration) et [O2] pour les compartiments intermédiaires. La consommation d'O2 dans les boites profondes est calculé selon l'équation (2) de Powley et al. 2016. Cette équation prend en compte le flux de Carbone Organique Particulaire (POC) et le Carbone Organique Dissous (DOC). La concentration en DOC est remplacée par la proportion de [O2] pouvant réagir avec le DOC afin d'éviter de calculer les variations de [DOC]. Le KDOC, demie saturation du DOC est converti en demie saturation de O2 à l'aide du ratio O2:C = 172:122 (Takahashi 1985). 
Le mélange turbulent est calculé en admettant un flux d'O2 retrouvé à partir d'un modèle linéaire. Ce mélange turbulent prend en compte le coefficient de diffusion effective Kz, la différence de concentration en O2 entre deux boites, la distance moyenne des boites, la surface de contact (surface du bassin). Tous les flux sont à l'équilibre pour le scénario Pre_EMT (conformément aux attentes) avec une gamme de variation inférieure à 5% pour la mise à l'équilibre (Inférieure à 5% par rapport à Powley et al. 2016).

NE MARCHE PAS, CORRESPOND PLUTOT A Eq 1 MAIS MODIFIEE.